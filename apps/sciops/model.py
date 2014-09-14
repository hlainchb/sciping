
import zoom
from zoom.collect import *
import collections
import random

# Useful classes and functions
#--------------------------------------------------------------
class Collection:
    name_column = 'name'
    order = lambda t,a: a.name
    can_edit = lambda a: True

    @classmethod
    def locate(cls, key):
        def scan(store, key):
            for rec in store:
                if rec.key == key:
                    return rec
        return key.isdigit() and cls.store.get(key) or cls.store.find(key=key) or scan(cls.store,key)

    @classmethod
    def match(cls, text):
        return list(cls.store.search(text))

def link_to_item(item):
    return '<a href="/%s/%s">%s</a>' % (system.app.name, item.key, item.name)

def tsbrowse(*a, **k):
    t = browse(*a, **k)
    return t

# Types and Constants
#--------------------------------------------------------------
project_statuses = [
        'Draft',
        'In Progress',
        'On Hold',
        'Completed',
        'Cancelled',
        ]

# Validators
#--------------------------------------------------------------

def number_valid(s):
    if s == '': return True
    try:
        float(s)
        return True
    except:
        return False
valid_number = Validator("numbers only", number_valid)

def latitude_valid(s):
    if s == '': return True
    try:
        v = float(s)
        if v >= -90 and v <= 90:
            return True
    except:
        return False
valid_latitude = Validator("requires a number between -90 and 90", latitude_valid)

def longitude_valid(s):
    if s == '': return True
    try:
        v = float(s)
        if v >= -180 and v <= 180:
            return True
    except:
        return False
valid_longitude = Validator("requires a number between -180 and 180", longitude_valid)

def get_observations(a): return str(random.randint(10,40))
def get_scientist(a): return random.choice(['M. Curie','A. Lovelace','A. Einstien','K. Marx'])

# Models
#--------------------------------------------------------------
class DefaultRecord(Record):
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
    scientist = property(get_scientist)
    observations = property(get_observations)
Sciop = ScipingSciop
sciops = store(Sciop)

class ScipingOperative(DefaultRecord):
    key = property(lambda self: id_for(self.name))
    url = property(lambda self: url_for_page('operative', self.key))
    link = property(lambda self: link_to(self.name, self.url))
    linked_name = property(lambda self: self.link)
Operative = ScipingOperative
operatives = store(Operative)

reserved_users = ['admin','user','guest']
scientists = [r for r in system.db('select * from dz_users') if r[1] not in reserved_users]
agents = [r for r in system.db('select * from dz_users') if r[1] not in reserved_users]

# Forms
#--------------------------------------------------------------
location_fields = Section('Location',[
            TextField('Latitude', required, valid_latitude, size=6, default=49.25),
            TextField('Longitude', required, valid_longitude, size=6, default=-123.1),
            ])

sciop_fields = Fields(
        TextField('Name', required, maxlength=80),
        MemoField('Description', required),
        Section('Operation Details',[
            TextField('Start Date', size=12),
            TextField('End Date', size=12),
            PulldownField('Status', default=project_statuses[0], options=project_statuses),
            ]),
        location_fields,
        )

settings_fields = Form(
        Section('Roles',[
            CheckboxField('List me as a scientist!', name='is_scientist'),
            CheckboxField('List me as an agent!', name='is_agent'),
        ]),
        Section('Notifications',[
            CheckboxField('Tweet at me when a new Op is entered', name='ping_new_op'),
            CheckboxField('Email me whenever a new Op is entered', name='ping_new_op'),
        ]),
        ButtonField('Save', cancel='settings/cancel'),
)

# Collections
#--------------------------------------------------------------
class SciopCollection(Collection):
    name = 'Science Ops'
    item_name = 'Science Op'
    labels = 'Name', 'Description', 'Scientist', 'Status', 'Observations'
    columns = 'linked_name', 'description', 'scientist', 'status', 'observations'
    entity = Sciop
    store = sciops
    url = '/%s/sciops' % system.app.name
    fields = sciop_fields
    order = lambda a,b: b.name.lower()
    can_edit = lambda a: user.is_member(['managers'])



