# -*- coding: utf-8 -*-
# @Author  : ydf
# @Time    : 2020/1/16 0016 9:51
import time
from funboost import boost, BrokerEnum


@boost(queue_name='sub',broker_kind=BrokerEnum.CELERY)
def sub(a,b):
    print(f'{a} - {b} = {a - b }')
    time.sleep(4)