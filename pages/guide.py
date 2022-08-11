from cgitb import text
import flet
from flet import IconButton, Page, Row, TextField, icons, ElevatedButton, FloatingActionButton, Text, View, AppBar, Tab, Tabs

from services.page import PageClass
import functions


class GuidePage(PageClass):
    def build(self):
        # Declare Controls
        appbar = AppBar(title=Text(value='新生生存指南', style='titleMedium'), elevation=100)
        tabs = Tabs(selected_index=1,
                    animation_duration=300,
                    tabs=[
                        Tab(text='综合', content=Text(value='This is a test')),
                        Tab(text='宿舍', content=Text(value='宿舍'))
                    ])
        # Declare View
        view = View('/guide', [tabs], appbar=appbar)
        self.page.views.append(view)
        self.update()
