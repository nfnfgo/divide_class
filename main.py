import asyncio
from cgitb import text
from ctypes import alignment
import time
from turtle import back, onclick

import flet
from flet import IconButton, Page, Row, TextField, icons, ElevatedButton, FloatingActionButton, Text

glo_page = None
glo_stu_id = ''


def main(page: Page):
    page.clean()
    global glo_page
    glo_page = page
    page.title = '康康你的学号'
    page.vertical_alignment = "center"
    stu_id = TextField(text_align="left", width=200, hint_text='请输入您的学号')
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
    page.clean()
    back_btn = FloatingActionButton(icon=icons.HOME_FILLED, on_click=back_main)
    value_text = f'''学号:{stu_id.value}'''
    text = Text(value=value_text, size=30, text_align='center')
    page.add(Row([text], alignment='center'))
    page.add(Row([back_btn],
                 alignment='center', vertical_alignment='end'))


def back_main(e):
    main(glo_page)


flet.app(port=8500, target=main)
