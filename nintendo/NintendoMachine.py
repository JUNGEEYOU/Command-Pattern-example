from nintendo.Command import *
from nintendo.NoCommand import *


class NitendoMachine(object):
    """
    인보커 - 닌텐도 기기
    """
    def __init__(self):
        self.array_command = [NoCommand()] *7 # 커맨드 리스트
        self.history =[]         # 명령 히스토리 저장
        # for i in range(7):
        #     self.array_command[i] = NoCommand()


    def set_command(self, slot =int, command = Command):
        """
        버튼 별 커맨드 적용
        :param slot:
        :param command:
        :return:
        """
        self.array_command[slot] = command


    def button_was_pushed(self, slot):
        self.array_command[slot].execute()
        self.history.append(self.array_command[slot])

    def show_history(self):
        print("*******history******")
        for history in self.history:
            print("test")


