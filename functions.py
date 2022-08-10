import time


def get_info(stu_id):
    re_text = ''
    re_text += f'查询时间戳: {int(time.time())}\n'
    re_text += f'学号: {stu_id}\n'
    return re_text