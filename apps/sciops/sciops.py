
from model import *
from zoom.mvc import View, Controller
from zoom.collect import CollectionView, CollectionController

testform = Form(
    TextField('name'),
    ButtonField('Create', cancel='cancel'),
    )


class MyView(CollectionView):
    pass

class MyController(CollectionController):
    pass

collection = SciopCollection()
view = MyView(collection)
controller = MyController(collection)

