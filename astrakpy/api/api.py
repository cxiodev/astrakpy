from astrakpy.utils.mixins import ContextInstanceMixin
from astrakpy.api.methods import Users, Messages


class API(ContextInstanceMixin):
    def __init__(self, app):
        self.app = app

        self.users = Users(self.app)
        self.messages = Messages(self.app)
