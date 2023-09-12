## 演示不规范的celery项目目录结构的funboost自动操作celery的使用：

funboost 自动配置和操作celery来执行用户函数,不用用户亲自配置和操作celery.
无论文件夹结构多么复杂乱七八糟,都不需要用户亲自配置celery的includes和task_routes
```
funboost支持30种消息队列,例如 rabbitmq nsq kafka redis queue.Queue sqlite mysql tcp 等作为消息队列,
funboost也能支持 dramatiq rq hury celery等分布式函数调度框架直接接管funboost的调度核心
funboost能支持将celery整体作为 funboost的消息队列,
使用户既能享受funboost的极简api和配置方式,又能利用celery的调度核心来执行用户函数
```

不规则的celery目录结果如下,使用funboost操作celery比直接操作celery,代码大大简化
```

D:\CODES\FUNBOOST_SUPPORT_CELERY_DEMO
├─aaaa
│  └─b
│      └─c
├─dddd
│  ├─e
│  │  └─taske.py
│  └─f
│      └─dirf4
│          └─taskf.py
├─gggg
└─publish.py

```

## 使用funboost 能 轻松自动化配置和操作celery,用户无需手写配置celery.

funboost_config.py  配置 CELERY_BROKER_URL 的值
[![pPDjy6O.png](https://s1.ax1x.com/2023/09/04/pPDjy6O.png)](https://imgse.com/i/pPDjy6O)

dddd/e/taske.py 使用boost装饰器,并设置 broker_kind=BrokerEnum.CELERY
[![pPDj6XD.png](https://s1.ax1x.com/2023/09/04/pPDj6XD.png)](https://imgse.com/i/pPDj6XD)

dddd/f/dirf4/taskf.py 使用boost装饰器,并设置 broker_kind=BrokerEnum.CELERY
[![pPDj20H.png](https://s1.ax1x.com/2023/09/04/pPDj20H.png)](https://imgse.com/i/pPDj20H)


gggg/publish.py  发布任务,可以使用delay或者push发布任务都可以.
[![pPDjfAA.png](https://s1.ax1x.com/2023/09/04/pPDjfAA.png)](https://imgse.com/i/pPDjfAA)


aaaa/b/c/celery_app_inatcance.py  # 启动消费. 相当于你在cmd 敲击了 celery worker 命令行启动了celery消费
[![pPDj4ht.png](https://s1.ax1x.com/2023/09/04/pPDj4ht.png)](https://imgse.com/i/pPDj4ht)


运行截图:

从运行截图可以看出,funboost+celery 绝对是原汁原味的celery执行核心来执行用户写的函数.

[![pPDjL7j.png](https://s1.ax1x.com/2023/09/04/pPDjL7j.png)](https://imgse.com/i/pPDjL7j)


```
使用funboost 能轻松配置和操作celery,无视用户的项目目录结构多么复杂和不规则.
```

## 对比celery亲自操作不规则项目目录

相比较比celery亲自操作不规则项目目录,让funboost代为操劳自动使用celery,代码大大简化了.

[https://github.com/ydf0509/celery_demo](https://github.com/ydf0509/celery_demo)



funboost支持celery设置celery的app config和函数app.task的入参,更详细的说明见文档
[https://funboost.readthedocs.io/zh/latest/articles/c11.html](https://funboost.readthedocs.io/zh/latest/articles/c11.html)






