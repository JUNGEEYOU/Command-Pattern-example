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
        print("앞으로 나간다")

    def back(self):
        """
        뒤로 가기
        :return:
        """
        print("뒤로 간다.")

    def left(self):
        """
        오른쪽으로 이동
        :return:
        """
        print("왼쪽으로 간다.")

    def right(self):
        """
        오른쪽으로 이동
        :return:
        """
        print("오른쪽으로 간다.")