from command.Command import *

class LsCommand(Command):
    """
    유닉스 명령어 ls 흉내내는 실제 커맨드
    """

    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        """
        리시버의 행동 호출
        :return:
        """
        self.receiver.show_current_dir()

    def undo(self):
        """
        ls 커맨드는 취소 못함
        :return:
        """
        pass
