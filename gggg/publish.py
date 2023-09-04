# -*- coding: utf-8 -*-
# @Author  : ydf
# @Time    : 2020/1/16 0016 9:55




from dddd.e.taske import add
from dddd.f.dirf4.taskf import sub


if __name__ == '__main__':
    for i in range(10):
        add.delay(i,i*2)
        sub.delay(i,i*10)