
import zoom
import random
import json

index_content = """
    <ul>
        <li><a href="/feeds/operations">operations</a></li>
    </ul>
"""

class DefaultRecord(zoom.Record):
    def __getitem__(self, name):
        try:
            return Record.__getitem__(self, name)
        except KeyError:
            return ''

class ScipingSciop(DefaultRecord):
    key = property(lambda self: id_for(self.name))
    url = property(lambda self: url_for_page('sciops', self.key))
    link = property(lambda self: link_to(self.name, self.url))
    linked_name = property(lambda self: self.link)
Sciop = ScipingSciop
sciops = zoom.store(Sciop)

class MyView(zoom.mvc.View):

    def index(self):
        return zoom.page(index_content, title='Feeds')

    def operations(self):
        print sciops
        f = [dict(id=r.id) for r in sciops]
        print f
        return zoom.page('%s' % json.dumps(sciops, indent=4))

class MyController(zoom.mvc.Controller):
    pass
    
controller = MyController()
view = MyView()
