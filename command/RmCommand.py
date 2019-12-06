from command.Command import *

class RmCommand(Command):
    """유닉스 명령어 rm 실제 커맨드"""
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.delete_file()

    def undo(self):
        self.receiver.undo()