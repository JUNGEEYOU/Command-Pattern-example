import os

class TouchReceiver(object):

    def __init__(self, filename):
        self.filename = filename

    def create_file(self):
        """실제 파일을 생성하는 메소드"""
        with open(self.filename, 'a'):
            os.utime(self.filename, None)

    def delete_file(self):
        """파일 생성을 취소하는 메소드"""
        os.remove(self.filename)