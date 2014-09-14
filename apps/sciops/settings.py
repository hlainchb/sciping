
from model import *

class MyView(zoom.mvc.View):

    def index(self):
        content = settings_fields.edit()
        return zoom.page(content, title='Settings')

class MyController(zoom.mvc.Controller):

    def save_button(self):
        message('settings saved')


    def cancel(self):
        return redirect_to('/%s' % system.app.name)

controller = MyController()
view = MyView()
