import abc
class Command(object):
    """
    커맨드 인터페이스
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractclassmethod
    def execute(self):
        """
        커맨드 실행 메소드
        :return:
        """
        pass

    @abc.abstractclassmethod
    def undo(self):
        """
        커맨드 실행 취소 메소드
        :return:
        """
        pass
