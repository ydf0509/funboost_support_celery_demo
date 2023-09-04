# -*- coding: utf-8 -*-
# @Author  : ydf
# @Time    : 2020/1/16 0016 9:5
import time
from funboost import boost,BrokerEnum


@boost(queue_name='add',broker_kind=BrokerEnum.CELERY)
def add(x, y):
    time.sleep(3)
    print(f'{x} + {y} = {x + y}')
    time.sleep(3)


if __name__ == '__main__':
    add(1, 2)
