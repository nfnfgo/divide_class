import asyncio
import time

import flet
from flet import IconButton, Page, Row, TextField, icons, ElevatedButton, FloatingActionButton, Text

import functions
from pages.home import HomePage


def main(page:Page):
    home_page = HomePage(page)
    home_page.build()

# flet.app(port=30005, target=main,view=flet.WEB_BROWSER)

flet.app(port=30005, target=main)