#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from requests import codes
from locust import task, constant, TaskSet
from locust.contrib.fasthttp import FastHttpUser


# Fasthttp相比较HTTPsession速度快,产生的TPS高,但是功能却没有HTTPsession全面

class SearchPage(TaskSet):
    @task
    def search_locust(self):
        payload = {'wd': 'locust'}
        with self.client.get('/s?wd=locust', params=payload,
                             name="百度搜索locust", catch_response=True) as r:
            if r.status_code == codes.ok:
                r.success()
            else:
                r.failure("搜索locust失败：{}".format(r.text))

    @task
    def stop(self):
        self.interrupt()


class DemoTest(FastHttpUser):
    host = 'https://www.baidu.com'
    wait_time = constant(3)
    network_timeout = 60
    tasks = {SearchPage: 1}
