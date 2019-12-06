from abc import ABCMeta

class Command(object):
    """
    커맨드 인터페이스
    """

    __metaclass__ = ABCMeta

    @ABCMeta.abstractclassmethod
    def execute(self):
        """
        커맨드를 실행하기 위한 추상 메소드
        :return:
        """
        pass

    @ABCMeta.abstractclassmethod
    def undo(self):
        """
        커맨드를 실행하기 취소하기 위한 메소드
        :return:
        """
        pass

