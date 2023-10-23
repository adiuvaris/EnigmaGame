
import arcade

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 1280
SCREEN_TITLE = "Enigma Discs"

COLORS = [arcade.color.DARK_GREEN, arcade.color.GOLD, arcade.color.DARK_ORANGE, arcade.color.TEAL,
          arcade.color.PURPLE, arcade.color.BROWN, arcade.color.DARK_BLUE, arcade.color.WHITE, arcade.color.DIM_GRAY]

LEVELS = ["Baby", "Pupil", "Beginner", "Novice", "Amateur", "Challenger",
          "Advanced", "Semiprofessional", "Professional", "Original", "Superman"]

GAMES = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
     1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
     1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 1, 0, 2, 1, 1, 2, 2, 2, 0, 1],
    [3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2,
     2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 3, 3, 3, 3, 2, 3],
    [1, 1, 1, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 2,
     2, 2, 2, 2, 2, 2, 2, 4, 4, 3, 3, 3, 3, 3, 4, 4, 4, 0, 4, 1, 1, 3, 3, 4, 2, 4],
    [0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 1, 1, 1, 1, 1, 1, 1, 1, 6, 6, 2, 2, 2, 2, 2, 2, 2, 2, 6, 6, 6, 6, 3, 3, 3, 3, 3, 3,
     3, 3, 6, 6, 4, 4, 4, 4, 4, 4, 4, 4, 6, 6, 6, 6, 0, 6, 1, 6, 6, 6, 6, 4, 6, 3],
    [2, 0, 5, 2, 0, 3, 0, 2, 3, 0, 2, 0, 3, 2, 0, 5, 0, 2, 5, 0, 1, 0, 5, 1, 0, 5, 0, 1, 5, 0, 1, 5, 6, 5, 1, 1, 6, 3,
     6, 1, 1, 3, 6, 3, 1, 1, 6, 5, 6, 1, 1, 5, 0, 1, 2, 3, 2, 5, 5, 5, 5, 6, 3, 6],
    [2, 0, 5, 2, 0, 3, 0, 2, 3, 0, 4, 0, 3, 4, 0, 5, 0, 4, 5, 0, 1, 0, 5, 1, 0, 5, 0, 1, 5, 0, 1, 5, 4, 5, 1, 1, 4, 3,
     4, 1, 1, 3, 2, 3, 1, 1, 2, 5, 2, 1, 1, 5, 0, 1, 2, 3, 4, 5, 5, 5, 5, 2, 3, 4],
    [2, 0, 5, 2, 0, 3, 0, 2, 3, 0, 4, 0, 3, 4, 0, 6, 0, 4, 6, 0, 1, 0, 6, 1, 0, 5, 0, 1, 5, 0, 1, 5, 4, 5, 1, 1, 4, 3,
     4, 1, 1, 3, 2, 3, 1, 1, 2, 6, 2, 1, 1, 6, 0, 1, 2, 3, 4, 5, 5, 6, 6, 2, 3, 4]
]