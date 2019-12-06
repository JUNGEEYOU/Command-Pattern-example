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
        print('File 생성됨\n')

    def delete_file(self):
        print ('파일 제거중')
        for command in self.delete_file_commands:
            command.execute()
            self.history.append(command)
        print('File 제거됨.\n')

    def undo_all(self):
        print('Undo all')
        for command in reversed(self.history):
            command.undo()
        print('Undo all finished.')

    def show_history(self):
        """ 히스토리 print """
        for his in self.history:
            print("history", his)