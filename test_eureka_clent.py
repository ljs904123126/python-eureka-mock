from py_eureka_client import eureka_client
import time
eureka_server = "http://localhost:8762/eureka/"

eur = eureka_client.EurekaClient(eureka_server=eureka_server,
                                 app_name="ljs",
                                 instance_host="127.0.0.1",
                                 instance_port=9090,
                                 renewal_interval_in_secs=1,
                                 zone='http://localhost:8762/test/eureka/')
eur.start()
eur.do_service('ljs',"test")
time.sleep(10000)
