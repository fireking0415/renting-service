class ResponseCode(object):
    """请求结果Code公共配置"""
    # 请求成功
    SUCCESS = 0
    # 请求失败
    FAIL = 1
    # 参数无效
    INVALID_PARAMETER = 2


class ResponseMessage(object):
    """请求结果Message公共配置"""
    SUCCESS = "请求成功"
    FAIL = "请求失败"
    INVALID_PARAMETER = "参数无效"


class Result(object):
    """封装响应文本"""

    def __init__(self, data=None, code=ResponseCode.SUCCESS,
                 msg=ResponseMessage.SUCCESS):
        self._data = data
        self._msg = msg
        self._code = code

    def update(self, code=None, data=None, msg=None):
        """
        更新默认响应文本
        :param code:响应状态码
        :param data: 响应数据
        :param msg: 响应消息
        :return:
        """
        if code is not None:
            self._code = code
        if data is not None:
            self._data = data
        if msg is not None:
            self._msg = msg

    def add_field(self, name=None, value=None):
        """
        在响应文本中加入新的字段，方便使用
        :param name: 变量名
        :param value: 变量值
        :return:
        """
        if name is not None and value is not None:
            self.__dict__[name] = value

    @property
    def data(self):
        """
        输出响应文本内容
        :return:
        """
        body = self.__dict__
        body["data"] = body.pop("_data")
        body["msg"] = body.pop("_msg")
        body["code"] = body.pop("_code")
        return body
