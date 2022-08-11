import flet
from flet import IconButton, Page, Row, TextField, icons, ElevatedButton, FloatingActionButton, Text, View, AppBar, Tab, Tabs, Container, alignment

from services.page import PageClass
import functions


class GuidePage(PageClass):
    def build(self):
        # Declare Controls
        self.clean()
        appbar = AppBar(title=Text(value='新生生存手册', style='titleMedium'), elevation=100)
        tabs = Tabs(selected_index=1,
                    animation_duration=300,
                    tabs=[
                        Tab(text='综合', content=Container(content=get_guide_zonghe()))
                    ],
                    expand=1)
        # Declare View
        view = View('/guide', [tabs], appbar=appbar)
        self.page.views.append(view)
        self.update()


# Content of Guide_综合
def get_guide_zonghe():
    return Container(content=Text(value='This is a testtttttttttttt'), alignment=alignment.top_left,margin=50)
