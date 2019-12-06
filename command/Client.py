from command.Invoker import Invoker
from command.LsCommand import LsCommand
from command.LsReceiver import LsReceiver
from command.RmCommand import RmCommand
from command.RmReceiver import RmReceiver
from command.TouchCommand import TouchCommand
from command.TouchReceiver import TouchReceiver

if __name__ == '__main__':
    # Client

    # List files in current directory
    ls_receiver = LsReceiver()
    ls_command = LsCommand(ls_receiver)

    # Create a file
    touch_receiver = TouchReceiver('test_file')
    touch_command = TouchCommand(touch_receiver)

    # Delete created file
    rm_receiver = RmReceiver('test_file')
    rm_command = RmCommand(rm_receiver)

    create_file_commands = [ls_command, touch_command, ls_command]
    delete_file_commands = [ls_command, rm_command, ls_command]

    invoker = Invoker(create_file_commands, delete_file_commands)

    invoker.create_file()
    invoker.delete_file()
    invoker.undo_all()