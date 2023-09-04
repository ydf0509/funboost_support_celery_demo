# -*- coding: utf-8 -*-
# @Author  : ydf
# @Time    : 2020/1/16 0016 9:40
from dddd.e.taske import add
from dddd.f.dirf4.taskf import sub
from funboost.assist.celery_helper import CeleryHelper

if __name__ == '__main__':
    add.consume()
    sub.consume()
    CeleryHelper.realy_start_celery_worker()
