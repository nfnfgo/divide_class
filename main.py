import asyncio
import time

import flet
from flet import IconButton, Page, Row, TextField, icons, ElevatedButton, FloatingActionButton, Text

import functions
from services.route_change import route_change
from pages.home import HomePage


def main(page: Page):
    # Define Route Change Handler
    def route_change_home(route):
        route_change(page)

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
    page.on_route_change = route_change_home
    page.on_view_pop = view_pop
    page.go(page.route)

    # StartHomePage
    # home_page = HomePage(page)
    # home_page.build()


flet.app(port=30005, target=main, view=flet.WEB_BROWSER, route_url_strategy="hash")
# flet.app(port=30005, target=main)
