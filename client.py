import pygame
pygame.init()
from network import Network
import pickle

pygame.font.init()

window_width = 700
window_height = 700
window = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption("Cricket Game - Client 1")
background_image = pygame.image.load("Untitled.jpg").convert()

class Button:
    def __init__(self,text,x,y,color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 120
        self.height = 100 

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("comicsans", 40)
        text_surface = font.render(self.text, 1, (0, 0, 0))
        window.blit(text_surface, (self.x + round(self.width / 2) - round(text_surface.get_width() / 2),
                        self.y + round(self.height / 2) - round(text_surface.get_height() / 2)))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False


def redraw_window(window, game, player_number):
    global text1, text2
    window.fill((255, 255, 0))  
    background_image = pygame.image.load("game-backimg.jpeg").convert()
    
    # Resize the background image to fit the window size
    background_image = pygame.transform.scale(background_image, (window.get_width(), window.get_height()))
    
    # Blit the background image onto the window surface
    window.blit(background_image, (0, 0))
    
    if not game.are_both_players_ready():
    # Load the image
        
        waiting_image = pygame.image.load("wait.jpg").convert()
    # Resize the image to fit the window
        waiting_image = pygame.transform.scale(waiting_image, (window_width, window_height))
    # Blit the image onto the window surface
        window.blit(waiting_image, (0, 0))
    
    # Render text
        font = pygame.font.Font(None, 36)  # You can choose your desired font and size
        text = font.render("Waiting for another player...", True, (0, 0, 0))  # Black color text
        text_rect = text.get_rect(center=(window_width // 2, window_height // 4 - 50))  # Adjust position as needed
        window.blit(text, text_rect)
    else:
        font = pygame.font.SysFont("comicsans",35)
        text_surface = font.render("You Are", 1, (0, 0, 0))
        window.blit(text_surface, (80, 165))
        text_surface = font.render("Opponent is ", 1, (0, 0, 0))
        window.blit(text_surface, (380, 165))

        if player_number == 1 and game.batting_done[0] == 1:
            text1 = font.render("Batsman", 1, (0, 0, 0))
            text2 = font.render("Bowler", 1, (0, 0, 0))
        elif player_number == 0 and game.batting_done[0] == 1:
            text1 = font.render("Bowler", 1, (0, 0, 0))
            text2 = font.render("Batsman", 1, (0, 0, 0))
        elif player_number == 1:
            text1 = font.render("Bowler", 1, (0, 0, 0))
            text2 = font.render("Batsman", 1, (0, 0, 0))
        elif player_number == 0:
            text1 = font.render("Batsman", 1, (0, 0, 0))
            text2 = font.render("Bowler", 1, (0, 0, 0))

        window.blit(text1, (80, 200))
        window.blit(text2, (380, 200))

        move1 = game.get_player_move(0)
        move2 = game.get_player_move(1)

        if game.have_both_players_played():
            text1 = font.render(move1, 1, (0, 0, 0))
            text2 = font.render(move2, 1, (0, 0, 0))
        else:
            if game.player1_has_played and player_number == 0:
                text1 = font.render(move1, 1, (0, 0, 0))
            elif game.player1_has_played:
                text1 = font.render("Locked In", 1, (0, 0, 0))
            else:
                text1 = font.render("Waiting...", 1, (0, 0, 0))

            if game.player2_has_played and player_number == 1:
                text2 = font.render(move2, 1, (0, 0, 0))
            elif game.player2_has_played:
                text2 = font.render("Locked In", 1, (0, 0, 0))
            else:
                text2 = font.render("Waiting...", 1, (0, 0, 0))

        score1 = game.get_player_score(0)
        score2 = game.get_player_score(1)

        if player_number == 1:
            window.blit(text2, (100, 350))
            window.blit(text1, (400, 350))
            t_score1 = font.render(str(score2), 1, (255, 75, 75))
            t_score2 = font.render(str(score1), 1, (255, 75, 75))
        else:
            window.blit(text1, (100, 350))
            window.blit(text2, (400, 350))
            t_score1 = font.render(str(score1), 1, (255, 75, 75))
            t_score2 = font.render(str(score2), 1, (255, 75, 75))

        window.blit(t_score1, (100, 250))
        window.blit(t_score2, (400, 250))

        if game.batting_done[0] == 1 and game.batting_done[1] == 1:
            pass
        elif game.batting_done[0] == 1 and game.get_player_score(1) == 0 and player_number == 1:
            text0 = font.render("OPPONENT IS OUT", 1, (255, 75, 75))
            window.blit(text0, (75, 100))
        elif game.batting_done[0] == 1 and game.get_player_score(1) == 0 and player_number == 0:
            text0 = font.render("YOU ARE OUT", 1, (255, 75, 75))
            window.blit(text0, (75, 100))

        for button in buttons:
            button.draw(window)

    pygame.display.update()


buttons = [Button("1", 75, 400, (0, 0, 255)), Button("2", 275, 400,  (0, 0, 255)), Button("3", 475, 400,  (0, 0, 255)),
           Button("4", 75, 525,  (0, 0, 255)), Button("5", 275, 525, (0, 0, 255)), Button("6", 475, 525, (0, 0, 255)), ]


def main():
    run = True
    clock = pygame.time.Clock()
    network = Network()
    player_number = int(network.get_player_number())
    print("You are player", player_number)
    while run:
        clock.tick(60)
        try:
            game = network.send("get")
        except:
            run = False
            print("Couldn't get game")
            break

        if game.have_both_players_played():
            redraw_window(window, game, player_number)
            pygame.time.delay(500)
            try:
                game = network.send("score")
            except:
                run = False
                print("Couldn't get game for score")
                break

        if game.batting_done[0] and game.batting_done[1]:
            redraw_window(window, game, player_number)
            pygame.time.delay(500)
            try:
                game = network.send("reset")
            except:
                run = False
                print("Couldn't get game")
                break

            font = pygame.font.SysFont("comicsans", 90)
            if game.determine_winner() == player_number:
                text = font.render("You Won!", 1, (0,255, 0))
            elif game.determine_winner() == -1:
                text = font.render("Tie Game!", 1, (255, 0, 75))
            else:
                text = font.render("You Lost...", 1, (255, 0, 0))

            window.blit(text, (220, 25))
            pygame.display.update()
            pygame.time.delay(3000)
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for button in buttons:
                    if button.click(pos) and game.are_both_players_ready():
                        if player_number == 0:
                            if not game.player1_has_played:
                                network.send(button.text)
                                print("Button", button.text, "clicked")
                        else:
                            if not game.player2_has_played:
                                network.send(button.text)
                                print("Button", button.text, "clicked")

        redraw_window(window, game, player_number)

def menu_screen():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(5)
        window.fill((255, 255, 255))
        font = pygame.font.SysFont("comicsans", 40)
        text = font.render("Click to Play!", 1, (0, 0, 0))
        window.blit(text, (220, 10))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
        window.blit(background_image, [70, 100])

        pygame.display.update()

    main()


while True:
    menu_screen()