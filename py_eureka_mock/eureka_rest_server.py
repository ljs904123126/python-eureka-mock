import threading
import time
from py_eureka_client import eureka_client
import logging
from flask import Flask


class RestServer:

    def __init__(self, host: str, port: int, name: str, eureka_server: str):
        self.host = host
        self.port = port
        self.name = name
        self.eureka_server = eureka_server

        # self.regist: SimpleRegistThread = None
        self.eureka_client: eureka_client.EurekaClient = None
        self.app: AppThread = AppThread(port=port)
        # self.app.setDaemon(False)

    def start(self):
        # self.regist = SimpleRegistThread(host=self.host, port=self.port, name=self.name,
        #                                  eureka_server=self.eureka_server)
        # self.regist.start()
        self.eureka_client = eureka_client.EurekaClient(eureka_server=self.eureka_server,
                                                        app_name=self.name,
                                                        instance_host=self.host,
                                                        instance_port=self.port)
        self.eureka_client.start()
        self.app.start()

    def stop(self):
        self.eureka_client.stop()
        pass

    def do_service(self):
        pass


class AppThread(threading.Thread):

    def __init__(self, port: int):
        super(AppThread, self).__init__()
        self.port = port
        self.app = Flask("app-server-" + str(port))
        self.app.add_url_rule("/<path:dummy>", view_func=self.handle)

    def setDaemon(self, daemonic: bool) -> None:
        super().setDaemon(daemonic)

    def run(self) -> None:
        super().run()
        self.app.run(host="0.0.0.0", port=self.port)

    def handle(self, dummy):
        return "Hello World!! path = " + dummy

# class SimpleRegistThread(threading.Thread):
#
#     def __init__(self, host: str, port: int, name: str, eureka_server: str):
#         super(SimpleRegistThread, self).__init__()
#         self.host = host
#         self.port = port
#         self.name = name
#         self.eureka_server = eureka_server
#         self.start_status = False
#
#     def start(self) -> None:
#         super().start()
#         self.start_status = True
#
#     def stop(self) -> None:
#         self.start_status = False
#
#     def run(self) -> None:
#         super().run()
#         eur = eureka_client.EurekaClient(eureka_server=self.eureka_server,
#                                          app_name=self.name,
#                                          instance_host=self.host,
#                                          instance_port=self.port)
#         eur.start()
#         while self.start_status:
#             eur.send_heartbeat()
#             print("send_heartbeat : ", self.name, self.host, self.port)
#             time.sleep(3)
