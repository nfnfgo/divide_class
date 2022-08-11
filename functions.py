from ast import expr_context
import time


def get_info(stu_id: str):
    stu_id = stu_id.upper()
    stu_id = 'E'+stu_id
    # 计算各种数据
    # 专业
    major = ['', '计算机科学与技术\n(共4个班)', '软件工程(共3个班)', '', '信息安全(共2个班)']
    try:
        stu_major = major[int(stu_id[1])]
    except:
        stu_major = '获取失败，请检查学号'
    # 班级
    last_4 = int(stu_id[-4:])
    if int(stu_id[1])==1:
        stu_cls = last_4%4
        if stu_cls==0:
            stu_cls='4'
    elif int(stu_id[1])==2:
        stu_cls = last_4%3
        if stu_cls==0:
            stu_cls='3'
    else:
        stu_cls = last_4%2
        if stu_cls==0:
            stu_cls='2'
    stu_cls = str(stu_cls)
    re_text = ''
    re_text += f'查询时间戳: {int(time.time())}\n'
    re_text += f'学号: {stu_id}\n'
    re_text += f'专业: {stu_major}\n'
    re_text += f'班级: {stu_cls}'
    return re_text
