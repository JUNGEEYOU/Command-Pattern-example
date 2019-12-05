from nintendo.Command import *


class GoRightCommand(Command):
    """
    오른쪽으로 가는 커맨드
    """
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        """
        리시버로 오른쪽 가기  호출
        :return:
        """
        self.receiver.right()

    def undo(self):
        """
        리시버로 오른쪽 가기 취소
        :return:
        """
        self.receiver.left()