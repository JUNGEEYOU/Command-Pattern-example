from nintendo.Command import *


class AnimalForest(object):
    """
    리시버: 실제 동물의 숲 행동 메소드 저장소
    """
    def forward(self):
        """
        앞으로 나가기
        :return:
        """
        print("동물의 숲 - 앞으로 나가는 메소드 호출 ")

    def back(self):
        """
        뒤로 가기
        :return:
        """
        print("동물의 숲 - 뒤로 가는 메소드 호출 ")

    def left(self):
        """
        오른쪽으로 이동
        :return:
        """
        print("동물의 숲 -왼쪽으로 가는 메소드 호출 ")

    def right(self):
        """
        오른쪽으로 이동
        :return:
        """
        print("동물의 숲 -오른쪽으로 가는 메소드 호출")