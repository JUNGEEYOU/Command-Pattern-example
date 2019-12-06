class Invoker(object):
    def __init__(self, create_file_commands, delete_file_commands):
        self.create_file_commands = create_file_commands
        self.delete_file_commands = delete_file_commands
        self.history = []

    def create_file(self):
        print('파일 생성중')

        for command in self.create_file_commands:
            command.execute()
            self.history.append(command)

        print('File created.\n')

    def delete_file(self):
        print ('파일 제거중')
        for command in self.delete_file_commands:
            command.execute()
            self.history.append(command)
        print('File deleted.\n')

    def undo_all(self):
        print('Undo all')

        for command in reversed(self.history):
            command.undo()

        print('Undo all finished.')