import pygame
from network import Network
from player import Player

pygame.font.init()

width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")


class Button:
    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 100
        self.height = 50

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("comicsans", 20)
        text = font.render(self.text, 1, (255, 255, 255))
        win.blit(
            text,
            (
                self.x + (round(self.width / 2) - round(text.get_width() / 2)),
                self.y + (round(self.height / 2) - round(text.get_height() / 2)),
            ),
        )

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]

        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False


def redrawWindow(win, game, p):
    win.fill((255, 255, 255))

    if not game.connected():
        font = pygame.font.SysFont("comicsans", 40)
        text = font.render("Waiting for player...", 1, (255, 0, 0), True)
        win.blit(
            text, (width / 2 - text.get_width() / 2, height / 2 - text.get_height() / 2)
        )
    else:
        font = pygame.font.SysFont("comicsans", 30)
        text = font.render("Your Move", 1, (0, 255, 255))
        win.blit(text, (30, 130))

        text = font.render("Opponents", 1, (0, 255, 255))
        win.blit(text, (300, 130))

        move1 = game.get_player_move(0)
        move2 = game.get_player_move(1)

        if game.bothWent():
            text1 = font.render(move1, 1, (0, 0, 0))
            text2 = font.render(move2, 1, (0, 0, 0))
        else:
            if game.p1Went and p == 0:
                text1 = font.render(move1, 1, (0, 0, 0))
            elif game.p1Went:
                text1 = font.render("Locked In", 1, (0, 0, 0))
            else:
                text1 = font.render("Waiting...", 1, (0, 0, 0))

            if game.p2Went and p == 1:
                text2 = font.render(move2, 1, (0, 0, 0))
            elif game.p2Went:
                text2 = font.render("Locked In", 1, (0, 0, 0))
            else:
                text2 = font.render("Waiting...", 1, (0, 0, 0))

        if p == 1:
            win.blit(text2, (80, 250))
            win.blit(text1, (300, 250))
        else:
            win.blit(text1, (80, 250))
            win.blit(text2, (300, 250))

        for btn in btns:
            btn.draw(win)
    pygame.display.update()


btns = [
    Button("Rock", 50, 350, (0, 0, 0)),       
    Button("Paper", 200, 350, (255, 0, 0)),  
    Button("Scissors", 350, 350, (0, 255, 0))  
]


def main():
    run = True

    clock = pygame.time.Clock()
    n = Network()
    player = int(n.getP())
    print("You are player", player)

    while run:
        clock.tick(60)
        try:
            game = n.send("get")
        except Exception as e:
            run = False
            print("Couldn't get game", e)
            break

        if game.bothWent():
            redrawWindow(win, game, player)
            pygame.time.delay(500)

            try:
                game = n.send("reset")
            except:
                run = False
                print("Couldn't get game", e)
                break

            font = pygame.font.SysFont("comicsans", 50)
            if (game.winner() == 1 and player == 1) or (
                game.winner() == 0 and player == 0
            ):
                text = font.render("You Won!", 1, (255, 0, 0))
            elif game.winner() == -1:
                text = font.render("Tie Game!", 1, (255, 0, 0))
            else:
                text = font.render("You Lost...", 1, (255, 0, 0))

            win.blit(
                text,
                (width / 2 - text.get_width() / 2, height / 2 - text.get_height() / 2),
            )
            pygame.display.update()
            pygame.time.delay(2000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for btn in btns:
                    if btn.click(pos) and game.connected():
                        if player == 0:
                            if not game.p1Went:
                                n.send(btn.text)
                        else:
                            if not game.p2Went:
                                n.send(btn.text)

        redrawWindow(win, game, player)


main()
