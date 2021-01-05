import os
import json


def get_config(path: str):
    sers = []
    r = os.path.join(path)
    print(os.listdir(r))
    for root, dirs, files in os.walk(r):
        for dir in dirs:
            res_info = {}
            with open(os.path.join(root, dir, "info.json"), 'r') as info:
                res_info = json.load(info)
            res_info["methods"] = []
            for root1, dirs1, files1 in os.walk(os.path.join(root, dir)):
                for file in files1:
                    if not file.startswith("method_"):
                        continue
                    with open(os.path.join(root1, file), 'r') as info:
                        file_info = json.load(info)
                        res_info["methods"].append(file_info)
            sers.append(res_info)
    print(sers)
    return sers
    # print(root)  # 当前目录路径
    # print(dirs)  # 当前路径下所有子目录
    # print(files)  # 当前路径下所有非目录子文件


get_config('D:/workspace/py_workspace/python-eureka-client/test_config')
