from python.model.field_x import XYField


class Point(XYField):
    def get_y(self) -> int:
        return self.__y

    def set_y(self, y: int):
        self.__y = y

    def get_x(self) -> int:
        return self.__x

    def set_x(self, x):
        self.__x = x

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
