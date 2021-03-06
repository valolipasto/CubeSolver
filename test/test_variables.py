"""A module to store all of the contant values required by the tests."""

# This determines how many random scrambles are tested in randomized tests
TEST_SIZE = 20

SOLVED_STR = """   WWW
   WWW
   WWW
RRRBBBOOOGGG
RRRBBBOOOGGG
RRRBBBOOOGGG
   YYY
   YYY
   YYY"""

CHECKERBOARD_TURNS = (0, 0, 5, 5, 1, 1, 3, 3, 2, 2, 4, 4)
CHECKERBOARD_NOTATION = "U2 D2 L2 R2 F2 B2"
CHECKERBOARD = "UDUDUDUDULRLRLRLRLFBFBFBFBFRLRLRLRLRBFBFBFBFBDUDUDUDUD"

CUBE_IN_THE_CUBE_NOTATION = "F L F U' R U F2 L2 U' L' B D' B' L2 U"
CUBE_IN_THE_CUBE = "FFFFUUFUUDDDLLDLLDRFFRFFRRRRRURRUUUULLLLBBLBBBBBDDBDDB"
CUBE_IN_THE_CUBE_EDGES = ["UR", "UF", "DF", "FL", "UB", "BR",
                          "DL", "DB", "FR", "DR", "BL", "UL"]
