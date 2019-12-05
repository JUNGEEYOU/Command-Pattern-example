from nintendo.Command import *


class GoForwardCommand(Command):
    """
    앞으로 나가는 커맨드
    """
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        """
        리시버로 앞으로 가기  호출
        :return:
        """
        self.receiver.forward()

    def undo(self):
        """
        리시버로 앞으로 가기 취소
        :return:
        """
        self.receiver.back()