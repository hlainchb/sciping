
from zoom import App, system

class MyApp(App):

    def __call__(self, *a, **k):
        return repr((a,k))

app = App()

system.app.menu = [
    ('index','Dashboard','index'),
    ('sciops','SciOps','sciops'),
    ('scientists','Scientists','scientists'),
    ('agents','Agents','agents'),
    ('settings','Settings','settings')]

