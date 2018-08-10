class ResponseCode:
    # 成功的状态
    SUCCESS_CODE = 200
    FAIL_CODE = 404
    BAD_REQUEST_CODE = 400
    LOGIN_USER_CODE = -1
    USER_NOEXIST_CODE = -2


class ResponseMsg:
    SUCCESS_MSG = 'success'
    FAIL_MSG = 'no find'
    LOGIN_PASSWORD_ERROR_MSG = '账号密码错误'


class Result:
    @staticmethod
    def generate_result_success(data=None, msg=ResponseMsg.SUCCESS_MSG, status=ResponseCode.SUCCESS_CODE):
        return {'msg': msg,
                'status': status,
                'data': data
                }

    @staticmethod
    def generate_result_error(msg=ResponseMsg.FAIL_MSG, status=ResponseCode.FAIL_CODE):
        return {'msg': msg,
                'status': status,
                }
