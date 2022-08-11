import asyncio
import time

import flet
from flet import IconButton, Page, Row, TextField, icons, ElevatedButton, FloatingActionButton, Text

from pages.home import HomePage
from pages.guide import GuidePage


def route_change(page: Page):
    page.views.clear()
    home_page = HomePage(page)
    home_page.build()
    if page.route == '/guide':
        guide_page = GuidePage(page)
        guide_page.build()
