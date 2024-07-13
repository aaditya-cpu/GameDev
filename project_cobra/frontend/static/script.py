from browser import document, html, timer
import random

# Define the board and player pieces
class MatchingPosition:
    def find_snake_or_ladder(self, block, turn, position):
        x = 35*(turn>=3)
        y = (turn%3)*35
        if(block == 3):
            return 305+x, 150+y, 22
        elif(block == 5):
            return 545+x, 390+y, 8
        elif(block == 11):
            return 185+x, 30+y, 26
        elif(block == 20):
            return 545+x, 30+y, 29
        elif(block == 17):
            return 425+x, 510+y, 4
        elif(block == 19):
            return 665+x, 390+y, 7
        elif(block == 21):
            return 425+x, 390+y, 9
        elif(block == 27):
            return 65+x, 510+y, 1
        else:
            return position[0], position[1], block

class GameBoard:
    def __init__(self, canvas):
        self.canvas = canvas
        self.ctx = canvas.getContext('2d')
        self.width = canvas.width
        self.height = canvas.height
        self.color = ["#FFF", "#F00", "#0F0", "#00F", "#FF0", "#0FF"]
        self.x = 65
        self.y = 510
        self.num_player = 0
        self.players = []
        self.positions = []
        self.turn = 0
        self.blocks = []
        self.dice_number = 1
        self.m = []
        self.start_game_button = document["startButton"]
        self.roll_button = document["rollButton"]
        self.start_game_button.bind('click', self.start_game)
        self.roll_button.bind('click', self.play_game)

    def start_game(self, event):
        self.num_player = 2  # Example with 2 players
        self.start_game_button.style.display = "none"
        self.roll_button.style.display = "block"
        self.create_pieces()
        self.draw_board()

    def draw_board(self):
        self.ctx.fillStyle = "brown"
        self.ctx.fillRect(0, 0, self.width, self.height)
        # Draw the game board image (replace with your image path)
        # img = document["gameBoardImage"]
        # self.ctx.drawImage(img, 0, 0, self.width, self.height)

    def create_pieces(self):
        for i in range(self.num_player):
            self.players.append(self.create_circle(self.x, self.y, 15, self.color[i]))
            self.positions.append([self.x, self.y])
            self.m.append(1)
            self.blocks.append(1)
            self.y += 35

    def create_circle(self, x, y, r, color):
        self.ctx.beginPath()
        self.ctx.arc(x, y, r, 0, 2 * 3.14)
        self.ctx.fillStyle = color
        self.ctx.fill()
        self.ctx.strokeStyle = color
        self.ctx.stroke()
        return {"x": x, "y": y, "r": r, "color": color}

    def update_circle(self, circle, x, y):
        self.ctx.clearRect(circle["x"]-circle["r"], circle["y"]-circle["r"], circle["r"]*2, circle["r"]*2)
        circle["x"] = x
        circle["y"] = y
        self.create_circle(x, y, circle["r"], circle["color"])

    def rolling_dice(self):
        return random.randint(1, 6)

    def play_game(self, event):
        if self.dice_number == 6:
            turn = self.turn
        else:
            turn = self.turn % self.num_player
            self.turn += 1
        position = self.positions[turn]
        dice_number = self.rolling_dice()
        new_position = self.move_player(position, dice_number, turn)
        self.positions[turn] = new_position

    def move_player(self, position, dice_number, turn):
        x, y = position
        for i in range(dice_number):
            x += 120 * self.m[turn]
            if x > 665 and turn < 3:
                y -= 120
                x = 665
                self.m[turn] = -1
            elif x > 700 and turn >= 3:
                y -= 120
                x = 700
                self.m[turn] = -1
            if x < 65 and turn < 3:
                x = 65
                y -= 120
                self.m[turn] = 1
            elif x < 100 and turn >= 3:
                x = 100
                y -= 120
                self.m[turn] = 1
            if y < 30:
                y = 30
            self.update_circle(self.players[turn], x, y)
            timer.sleep(0.25)
        x, y, block = MatchingPosition().find_snake_or_ladder(self.blocks[turn], turn, [x, y])
        self.blocks[turn] = block
        self.update_circle(self.players[turn], x, y)
        return [x, y]

canvas = document["gameCanvas"]
game_board = GameBoard(canvas)
