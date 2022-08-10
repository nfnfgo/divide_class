import asyncio
from cgitb import text
from ctypes import alignment
import time

import flet
from flet import IconButton, Page, Row, TextField, icons, ElevatedButton, FloatingActionButton, Text

import functions

glo_page = None
glo_stu_id = ''


def main(page: Page):
    page.clean()
    global glo_page
    glo_page = page
    page.title = '康康你的学号'
    page.vertical_alignment = "center"
    stu_id = TextField(text_align="left", width=210, hint_text='请输入您的学号',prefix=Text(value='E'))
    global glo_stu_id
    glo_stu_id = stu_id
    confirm_btn = FloatingActionButton(icon=icons.SEARCH, on_click=show_info)
    row = Row(
        [stu_id, confirm_btn],
        alignment='center'
    )
    page.add(row)


def show_info(e):
    page: Page = glo_page
    stu_id: TextField = glo_stu_id
    if (len(stu_id.value)!=8) or (stu_id.value.isdigit()==False):
        stu_id.value = ''
        stu_id.hint_text='学号不正确，请重新输入'
        page.update()
        return
    page.clean()
    back_btn = FloatingActionButton(icon=icons.HOME_FILLED, on_click=back_main)
    re_text = functions.get_info(stu_id.value)
    text = Text(value=re_text, size=30, text_align='justify')
    page.add(Row([text], alignment='center'))
    page.add(Row([back_btn],
                 alignment='center', vertical_alignment='end'))


def back_main(e):
    main(glo_page)


flet.app(port=8500, target=main)
