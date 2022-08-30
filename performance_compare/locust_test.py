# coding=utf-8
import requests
from locust import HttpUser, TaskSet, task, events
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import sys
import action_pb2
import grpc
import action_pb2_grpc
from google.protobuf import empty_pb2
import inspect
import time

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def stopwatch(func):
    """To be updated"""

    def wrapper(*args, **kwargs):
        """To be updated"""
        # get task's function name
        previous_frame = inspect.currentframe().f_back
        _, _, task_name, _, _ = inspect.getframeinfo(previous_frame)

        start = time.time()
        result = None
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            total = int((time.time() - start) * 1000)
            events.request_failure.fire(request_type="TYPE",
                                        name=task_name,
                                        response_time=total,
                                        response_length=0,
                                        exception=e)
        else:
            total = int((time.time() - start) * 1000)
            events.request_success.fire(request_type="TYPE",
                                        name=task_name,
                                        response_time=total,
                                        response_length=0)
        return result

    return wrapper

class MyTaskSet(TaskSet):
    # get flask health check
    @task(1)
    def get_flask_api(self):
        # r = self.client.get("https://template-flask-for-workshop-jimmy-5uvz3vc6ga-de.a.run.app/", name = "flask_health_check")
        r = self.client.get("http://127.0.0.1:5000/", name = "flask_health_check")
        return r
    
    @task(1)
    @stopwatch
    def get_grpc_api(self):
        """To be updated"""
        try:
            creds = grpc.ssl_channel_credentials()
            with grpc.secure_channel('{}:{}'.format('template-grpc-for-workshop-jimmy-5uvz3vc6ga-de.a.run.app', 443), creds) as channel:

                stub = action_pb2_grpc.ToDoServiceStub(channel)
                response = stub.HealthCheck(empty_pb2.Empty(), 3600)
                # print(response)
        except (KeyboardInterrupt, SystemExit):
            sys.exit(0)
        # try:
        #     creds = grpc.ssl_channel_credentials()
        #     with grpc.insecure_channel('{}:{}'.format('localhost', 8080)) as channel:

        #         stub = action_pb2_grpc.ToDoServiceStub(channel)
        #         response = stub.HealthCheck(empty_pb2.Empty(), 3600)
        #         # print(response)
        #         return response
        # except (KeyboardInterrupt, SystemExit):
        #     sys.exit(0)

class webUser(HttpUser):
    host = '/'
    tasks = [MyTaskSet]
    min_wait = 3000
    max_wait = 6000
