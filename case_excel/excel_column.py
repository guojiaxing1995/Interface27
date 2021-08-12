class excel_column:
    # 用例ID
    CASE_ID = 1
    # 用例名称
    CASE_NAME = 2
    # 是否执行
    IS_RUN = 3
    # 请求方法
    METHOD = 4
    # url
    URL = 5
    # header
    HEADER = 6
    # 数据处理
    DATA_DEAL = 7
    # 依赖用例
    DEPEND_CASE = 8
    # 依赖用例所属字段
    DEPEND_KEY = 9
    # 请求数据表单提交
    DATA = 10
    # 请求数据json提交
    JSON = 11
    # 预期结果
    EXPEND_RESULT = 12
    # 实际结果
    ACTUAL_RESULT = 13
    # 接口返回
    INTERFACE_RETURN = 14

    @classmethod
    def getcolumn_case_id(cls):
        return cls.CASE_ID

    @classmethod
    def getcolumn_case_name(cls):
        return cls.CASE_NAME

    @classmethod
    def getcolumn_isrun(cls):
        return cls.IS_RUN

    @classmethod
    def getcolumn_method(cls):
        return cls.METHOD

    @classmethod
    def getcolumn_URL(cls):
        return cls.URL

    @classmethod
    def getcolumn_header(cls):
        return cls.HEADER

    @classmethod
    def getcolumn_data_deal(cls):
        return cls.DATA_DEAL

    @classmethod
    def getcolumn_depend_case(cls):
        return cls.DEPEND_CASE

    @classmethod
    def getcolumn_depend_key(cls):
        return cls.DEPEND_KEY

    @classmethod
    def getcolumn_data(cls):
        return cls.DATA

    @classmethod
    def getcolumn_json(cls):
        return cls.JSON

    @classmethod
    def getcolumn_expend_result(cls):
        return cls.EXPEND_RESULT

    @classmethod
    def getcolumn_actual_result(cls):
        return cls.ACTUAL_RESULT

    @classmethod
    def getcolumn_interface_return(cls):
        return cls.INTERFACE_RETURN
