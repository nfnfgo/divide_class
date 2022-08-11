'''Declare the show_info class'''

import flet
from flet import IconButton, Page, Row, TextField, icons, ElevatedButton, FloatingActionButton, Text, View,AppBar

from services.page import PageClass
import functions


class ShowInfoPage(PageClass):
    def build(self, home_page):
        if (len(home_page.stu_id.value) != 8) or (home_page.stu_id.value.isdigit() == False):
            home_page.stu_id.value = ''
            home_page.stu_id.hint_text = '学号不正确'
            self.page.update()
            return
        self.page.views.clear()
        back_btn = FloatingActionButton(icon=icons.HOME_FILLED, on_click=home_page.build)
        re_text = functions.get_info(home_page.stu_id.value)
        text = Text(value=re_text, size=20, text_align='justify')
        # Create View
        appbar = AppBar(title=Text(value='查询结果', style='titleMedium'),
                        center_title=False,
                        elevation=100,
                        leading=IconButton(icon=icons.ARROW_BACK,on_click=home_page.build))
        view = View('/',
                    [Row([text], alignment='center'), Row([back_btn], alignment='center', vertical_alignment='end')],
                    appbar=appbar)
        self.page.views.append(view)
        self.update()
