#encoding=utf-8
import requests
import json

class RunMethod:
    def get_main(self,url,header=None,data=None):
        if header!= '':
           res = requests.get(url=url,data=data,headers=header)
        else:
            res = requests.get(url=url,data=data)
        return res

    def post_main(self,url,header=None,data=None,json_str=None):
        if header != '':
            res = requests.post(url=url,data=data,json=json_str,headers=header)
        else:
            res = requests.post(url=url,data=data,json=json_str)

        return res

    def put_main(self,url,data):
        res = requests.put(url=url,data=data)

    def delete_main(self,url,data):
        res = requests.delete(url=url,data=data)

    def run_main(self,method,url,header,data,json_str):
        res = None
        if method == 'get' or method == 'GET':
            res = self.get_main(url,header,data)
        elif method =='post' or method == 'POST':
            res = self.post_main(url,header,data,json_str)
        elif method == 'put' or method == 'PUT':
            res = self.put_main(url,data)
        elif method == 'delete' or method == 'DELETE':
            res = self.delete_main(url,data)

        #return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)
        return res


