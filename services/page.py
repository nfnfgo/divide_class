import flet
from flet import Page


class PageClass():
    def __init__(self, page: Page = None):
        if page is not None:
            self.page:Page = page

    def update(self):
        '''Update A Page'''
        self.page.update()

    def clean(self):
        '''Clean A Page'''
        self.page.clean()