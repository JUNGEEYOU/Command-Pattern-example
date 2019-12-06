from command.Command import *

class TouchCommand(Command):
    """ 유닉스 명령어 touch 실제 커맨드"""

    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.create_file()

    def undo(self):
        self.receiver.delete_file()