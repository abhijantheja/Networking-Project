import socket
from _thread import *
import pickle
from game import CricketGame  # Import the modified Game class

SERVER_IP = "127.0.0.1"
PORT = 5555

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server_socket.bind((SERVER_IP, PORT))
except socket.error as e:
    print("Failed to bind the server:", str(e))

server_socket.listen()
print("Waiting for a connection... Server is up and running.")

connected_clients = set()
games = {}
game_count = 0


def handle_client_connection(client_conn, player_id, game_id):
    global game_count
    client_conn.send(str.encode(str(player_id)))

    while True:
        try:
            data = client_conn.recv(4096).decode()

            if game_id in games:
                current_game = games[game_id]

                if not data:
                    break
                else:
                    if data == "reset":
                        current_game.reset_player_moves()
                    elif data == "score":
                        print("No issues found.")
                        print("Player 1's batting status:", current_game.batting_done[0], "and Player 2's batting status:", current_game.batting_done[1])
                        if current_game.batting_done[0] == 1 and current_game.have_both_players_played():
                            print("Player 2 is batting now.")
                            current_game.scores[1] = current_game.calculate_batsman_score(1, 0, current_game.scores[1])
                            print("Player 2's batting completed.")
                        elif current_game.have_both_players_played():
                            print("Player 1 is batting now.")
                            current_game.scores[0] = current_game.calculate_batsman_score(0, 1, current_game.scores[0])
                            print("Player 1's batting completed.")
                        current_game.reset_player_moves()
                    elif data != "get":
                        current_game.make_move(player_id, data)

                    client_conn.sendall(pickle.dumps(current_game))
            else:
                break
        except:
            break

    print("Connection lost with client.")
    try:
        del games[game_id]
        print("Closing Game", game_id)
    except:
        pass
    game_count -= 1
    client_conn.close()


while True:
    client_conn, client_addr = server_socket.accept()
    print("Connected to client:", client_addr)

    game_count += 1
    player_id = 0
    game_id = (game_count - 1) // 2
    print("Current number of games:", game_count)
    if game_count % 2 == 1:
        games[game_id] = CricketGame(game_id)
        print("A new game is created.")
    else:
        print("Second player connected.")
        games[game_id].ready_to_start = True
        player_id = 1

    start_new_thread(handle_client_connection, (client_conn, player_id, game_id))