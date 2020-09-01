#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from requests import codes
from locust import HttpUser, task, between, TaskSet


class DemoTest(HttpUser):
    host = 'https://www.baidu.com'
    wait_time = between(2, 15)

    @task
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
