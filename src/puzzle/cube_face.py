from typing import List


class CubeFace:
    def __init__(self, size: int, color: int):
        self.__size = size
        self.__facelets = [[color]*size for _ in range(size)]

    @property
    def facelets(self) -> List[List[int]]:
        return self.__facelets[:]

    def getLine(self, line_number: int) -> List[int]:
        line = [0, 0, 0]

        if line_number < self.__size:
            line = self.__facelets[line_number][:]
        else:
            for row in range(self.__size):
                line[row] = self.__facelets[row][line_number-self.__size]

        return line

    def setLine(self, line_number: int, line: List[int]) -> None:
        if line_number < self.__size:
            self.__facelets[line_number] = line
            return
        for row in range(self.__size):
            self.__facelets[row][line_number-self.__size] = line[row]

    def rotate(self, clockwise: bool = True) -> None:
        if clockwise:
            self.__facelets = list(zip(*self.__facelets[::-1]))
        else:
            self.__facelets = list(zip(*self.__facelets))[::-1]

        self.__facelets = [list(row) for row in self.__facelets]
