
from model import *

class MyView(zoom.mvc.View):

    def index(self):

        content = '<br>'.join(s[1] for s in agents)

        return zoom.page(content, title='Agents')

class MyCollection(zoom.mvc.Controller):
    pass


collection = MyCollection()
view = MyView()
