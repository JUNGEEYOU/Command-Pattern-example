from nintendo.Command import *


class GoBackCommand(Command):
    """
    뒤로 가는 커맨드
    """
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        """
        뒤로 가기
        :return:
        """
        self.receiver.back()

    def undo(self):
        """
        앞으로 가기
        :return:
        """
        self.receiver.forward()