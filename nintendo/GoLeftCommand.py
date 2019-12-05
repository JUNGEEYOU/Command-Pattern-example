from nintendo.Command import *


class GoLeftCommand(Command):
    """
    앞으로 나가는 커맨드
    """
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        """
        리시버로 왼쪽으로 가기  호출
        :return:
        """
        self.receiver.left()

    def undo(self):
        """
        리시버로 왼쪽으로 가기 취소
        :return:
        """
        self.receiver.right()