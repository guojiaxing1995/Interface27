# Interface27
python接口自动化测试工具


项目包含两套接口自动化测试工具，可分别独立运行。一套为requests+unnitest，一套为通过填写excel表格测试。


### python+requests+unnitest
```
params = {
            "token": globalvar.get_value('token'),
            "random": random.randint(0, 99999999),
        }
        url = self.url + 'XXXXX'
        r = requests.post(url, data=params)

        self.assertEqual(r.status_code, 200)
```
利用requests库做接口请求，unnitest框架整合运行测试用例。依赖数据存放在一个全局的字典中。


### excel表格填写测试用例

![excel case](https://github.com/guojiaxing1995/Interface27/blob/master/readme/excel.png)

excel表格中一行为一条用例。执行顺序则是按照行顺序从上往下执行。对于一条用例是否执行为是则执行，否不执行，但当一条用例作为其余用例的依赖用例时，则强制
执行。

数据处理有2种处理方法：1.deal_default，默认处理。如果方法不传参数则利用递归获取接口返回的所有键值对并存在全局字典中，传参数则参数为要存储的key，将key以及
对应的value存在全局字典中。2.支持自定义处理方法，在多数的情况下，接口的参数依赖前一个接口返回，但是返回数据并不能直接使用，需要对接口返回数据进行特定的
处理。项目支持在代码中自定义处理方法，只需在表格中填写方法名称。

依赖用例所属字段的作用则是选取全局变量字典中的目标值作为当前用例接口请求的参数。

data和json为两种提交方式。通过预期结果是否在接口的返回值中来判断是否执行成功。运行完毕后会将实际结果和接口返回回写到表格中。




_项目中删除了所有接口地址和部分注释。_
