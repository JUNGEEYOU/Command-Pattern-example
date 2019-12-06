import os

class RmReceiver(object):

    def __init__(self, filename):
        self.filename = filename
        self.backup_name = None

    def delete_file(self):
        """파일 삭제를 실제하는 메소드"""
        self.backup_name = '.' + self.filename
        os.rename(self.filename, self.backup_name)

    def undo(self):
        """파일 삭제 복구 매소드"""
        original_name = self.backup_name[1:]
        os.rename(self.backup_name, original_name)
        self.backup_name = None