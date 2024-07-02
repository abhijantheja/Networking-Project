
PROJECT NAME:             "" Handcricket Battles in the Networking Arena ""

Welcome to "Handcricket Battles in the Networking Arena"! This project is an exciting implementation of the classic and famous handcricket game, enhanced with networking capabilities and web sockets. Now, you can enjoy the thrill of handcricket matches against opponents within the same server, all within a seamless online environment.
This project comprises four Python (.py) files: client.py, server.py, game.py, and network.py.Here is the explanation of each in brief:

client.py

Imports: This file imports necessary modules like pygame, pickle, and the Network class from network.py.
Button Class: Defines a class for buttons that will be used in the game interface.
redrawWindow Function: Function to redraw the game window based on game state.
Main Function:
Sets up the game window and network connection.
Enters a loop where it continuously updates the game state, handles events like button clicks, and redraws the window accordingly.
menu_screen Function:
Displays a simple menu screen prompting the user to click to play.
If the user clicks, it starts the main game loop.

network.py

Network Class:
Sets up a socket connection to communicate with the server.
Has methods to get the player number (get_player_number), connect to the server (connect), and send/receive data (send).

game.py

CricketGame Class:
Defines the game logic.
Tracks player moves, scores, and game state.
Has methods to play a move, determine the winner, reset the game, etc.

server.py

Imports: Imports necessary modules like socket, _thread, and the Game class from game.py.
Threaded Client Function:
Handles communication with a single client in a separate thread.
Receives player moves from the client and updates the game state accordingly.
Main Loop:
Accepts incoming connections from clients.
Assigns players to games and starts a new game when two players are connected.
Creates a new thread for each client connection to handle communication independently.

Overall Flow:

The server waits for connections from clients.
When two clients are connected, the server starts a new game for them.
Each client runs its game loop, where it sends moves to the server and receives updated game states.
The server handles game logic and distributes game states to clients.
The clients display the game state to the players and handle player input.
This process continues until one player wins or the game is terminated.