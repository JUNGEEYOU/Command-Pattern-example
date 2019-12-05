from nintendo.AnimalForest import AnimalForest
from nintendo.GoForwardCommand import *
from nintendo.GoRightCommand import *
from nintendo.GoLeftCommand import *
from nintendo.GoBackCommand import *
from nintendo.NintendoMachine import *

if __name__ == '__main__':
    """
    클라이언트 
    """
    # 1. 리시버 정의
    animal_game = AnimalForest()

    # 2. 커맨드 정의
    go_forward_command = GoForwardCommand(receiver=animal_game)
    go_back_command = GoBackCommand(receiver=animal_game)
    go_left_command = GoLeftCommand(receiver=animal_game)
    go_right_command = GoRightCommand(receiver=animal_game)



    # 3. 인보커 정의 = 리모컨 정의 및 커맨드와 연결
    remote_nintendo = NitendoMachine()
    remote_nintendo.set_command(0, go_forward_command)
    remote_nintendo.set_command(1, go_back_command)
    remote_nintendo.set_command(2, go_left_command)
    remote_nintendo.set_command(3, go_right_command)

    # 4. 실제 게임 진행
    remote_nintendo.button_was_pushed(1)
    remote_nintendo.button_was_pushed(0)
    remote_nintendo.button_was_pushed(2)
    remote_nintendo.button_was_pushed(3)


