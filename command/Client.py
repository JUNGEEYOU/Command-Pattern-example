from command.Invoker import Invoker
from command.LsCommand import LsCommand
from command.LsReceiver import LsReceiver
from command.RmCommand import RmCommand
from command.RmReceiver import RmReceiver
from command.TouchCommand import TouchCommand
from command.TouchReceiver import TouchReceiver

if __name__ == '__main__':
    # Client

    # 1. LS 관련
    # 1-1. 리시버 정의 : 실제 작업자
    ls_receiver = LsReceiver()
    # 1- 2. 커맨드 정의: 커맨드에 리시버 전달
    ls_command = LsCommand(ls_receiver)

    # 2. Touch 관련
    # 2-1. 리시버 정의
    touch_receiver = TouchReceiver('test.text')
    # 2-2. 커맨드 정의
    touch_command = TouchCommand(touch_receiver)

    # 3. RM 관련
    # 3-1. 리시버 정의
    rm_receiver = RmReceiver('test.text')
    # 3-2. 커맨드 정의
    rm_command = RmCommand(rm_receiver)

    # 매크로 커맨드 정의: 여러 작업을 한번에 진행
    create_file_commands = [ls_command, touch_command, ls_command]
    delete_file_commands = [ls_command, rm_command, ls_command]

    # 인보커 정의: 인보커에게 커맨드 전달
    invoker = Invoker(create_file_commands, delete_file_commands)
    # 인보커가 리시버에게 작업해달라고 요청
    invoker.create_file()
    invoker.delete_file()
    invoker.print_history()
    invoker.undo_all()