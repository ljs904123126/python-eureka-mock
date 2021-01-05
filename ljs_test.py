from py_eureka_mock import eureka_rest_server,manage_server
from py_eureka_client import eureka_client
from py_eureka_client import logger
import threading
import time
from flask import Flask, render_template

logger.set_level("DEBUG")
log = logger.get_logger("MOCK")

log.info("123")
log.info(123)
server_list = manage_server.get_config('D:/workspace/py_workspace/python-eureka-client/test_config')
#
# server_list = [{"name": "ljs-python-test", "host": "127.0.0.1", "port": "9090"},
#                {"name": "ljs-python-test1", "host": "127.0.0.1", "port": "9091"},
#                {"name": "ljs-python-test2", "host": "127.0.0.1", "port": "9092"}]

eureka_server = "http://localhost:8762/eureka/"
server_set = {}
eureka_client._RENEWAL_INTERVAL_IN_SECS = 10

for ser in server_list:
    app_name = ser["name"]
    eur = eureka_rest_server.RestServer(host=ser["host"], port=int(ser["port"]), name=app_name,
                                        eureka_server=eureka_server)
    server_set[app_name] = eur
    eur.start()

app = Flask('manage')


@app.route("/")
def index():
    res = []
    for d in server_set:
        res.append(server_set[d])
    return render_template("manage/index.html", res=res)


app.run(host='0.0.0.0', port=9099)

#
# print(server_set)
#
# app = Flask("test")
#
#
# @app.route("/")
# def hello_world():
#     return "HelloWorld"
#
#
# app.run("127.0.0.1", 8081)

print("main over")
# eur.start()


#
# from py_eureka_client.eureka_client import EurekaClient
# client = EurekaClient(eureka_server="http://localhost:8762/eureka/", app_name="python_module_1", instance_port=9090)
# client.start()
# res = client.do_service("OTHER-SERVICE-NAME", "/service/context/path")
# print("result of other service" + res)
# # when server is shutted down:
# client.stop()
