import flet
from flet import IconButton, Page, Row, TextField, icons, ElevatedButton, FloatingActionButton, Text, View, AppBar, Container, alignment

from pages.show_info import ShowInfoPage
from services.page import PageClass


# HomePage Class
class HomePage(PageClass):
    def build(self, e=None):
        self.page.views.clear()
        # Set the Pages
        self.page.title = '康康你的学号'
        self.page.vertical_alignment = "center"
        # set the Controls
        self.stu_id = TextField(text_align="left", width=210, hint_text='请输入您的学号', prefix=Text(value='E'))
        confirm_btn = FloatingActionButton(icon=icons.SEARCH, on_click=self.show_info)
        row = Row(
            [self.stu_id, confirm_btn],
            alignment='center'
        )
        servive_guide_btn = Container(ElevatedButton(text='新生生存指南', icon=icons.BOOK, on_click=self.go_guide), alignment=alignment.center)
        # Set Views
        appbar = AppBar(title=Text(value='查询分班', style='titleMedium'),
                        center_title=False,
                        elevation=100,
                        leading=IconButton(icon=icons.SEARCH, disabled=True),
                        leading_width=25)
        view = View('/',
                    [row,
                     servive_guide_btn],
                    appbar=appbar,
                    vertical_alignment='center')
        self.page.views.append(view)
        self.update()

    # Show Info
    def show_info(self, e):
        show_info_page = ShowInfoPage(self.page)
        show_info_page.build(self)

    # Go Chat
    def go_guide(self, e):
        self.go('/guide')
