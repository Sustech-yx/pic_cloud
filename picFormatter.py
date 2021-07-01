import os
from PIL import Image
from scipy import ndimage
import numpy as np
import scipy


class picFormatter:
    def __init__(self, srcfile='ori_pic', descfile='src_50', height=90, width=120):
        self.srcfile = srcfile
        self.descfile = descfile
        self.height = height
        self.width = width

    def work(self):
        delete_file(os.path.join(os.getcwd(), self.descfile))
        pass


def delete_file(path):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            delete_file(c_path)
        else:
            os.remove(c_path)