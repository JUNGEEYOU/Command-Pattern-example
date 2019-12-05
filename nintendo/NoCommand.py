from nintendo.Command import *


class NoCommand(Command):
    """
    아무 작업도 안하는 커맨드
    """
    def __init__(self):
        pass

    def execute(self):
        pass

    def undo(self):
        pass