import os

class LsReceiver(object):
    def show_current_dir(self):
        """
        실제 ls 동작 메소드
        :return:
        """
        cur_dir = './'
        filenames = []
        for filename in os.listdir(cur_dir):
            if os.path.isfile(os.path.join(cur_dir, filename)):
                filenames.append(filename)
        print('content dir', ' '.os.path.join(filenames))
