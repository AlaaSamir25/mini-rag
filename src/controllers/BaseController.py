from helpers.config import get_setings,Settings

class BaseController:
    def __init__(self):
        self.app_settings=get_setings()