
import zoom
import random
from zoom.vis.leaflet import Marker, Map, Icon
from zoom.vis.jqplot import line, hbar
from collections import Counter

def randmetric():
    return random.randint(5,50)

css = """
.metric {
    height: 90px;
    border: solid black thin;
    border-radius: 8px;
    padding: 10px;
    spadding-left: 15px;
    background: white;
    }
.metric-number{
    font-size: 30px;
    display: block;
    }
.dashboard {
    background: #8ec741;
    padding: 5px;
    border-radius: 8px;
}
.dashboard .row {
    smargin-bottom: 10px;
    margin: 10px 0;
}
div.leaflet-map {
    width: 100%;
    height: 350px;
    }
.chart {
    height: 235px;
    }
"""

twitter_widget = open('twitter_widget.html').read()

metric_template = """
    <div class="col-sm-2">
        <div class="metric">
            <div class="metric-number">%s</div>
            <div class="metric-text">%s</div>
        </div>
    </div>
"""

page_template = """
<div class="dashboard">
    <div class="row">
        %(metrics)s
    </div>
    <div class="row">
        <div class="col-md-8">
            <div id="opsmap">%(opsmap)s</div>
            <div class="row">
                <div class="col-md-8">
                    <div id="vis1">%(vis1)s</div>
                </div>
                <div class="col-md-4">
                    <div id="vis2">%(vis2)s</div>
                </div>
            </div>
        </div>
        <div class="col-md-4">
            <div id="livefeed">%(feed)s</div>
        </div>
    </div>
</div>
"""


# Map
#---------------------------------------------------------------------
BC_LL = [55,-125]
CANADA_LL = [55,-95]

VANCOUVER_MARKER = Marker([49.25, -123.1],'Vancouver')
EDMONTON_MARKER = Marker([53.53, -113.5],'Edmonton')
CALGARY_MARKER = Marker([51.5, -114],'Calgary')
REGINA_MARKER = Marker([50.5, -104.6],'Regina')
WINNIPEG_MARKER = Marker([49.9, -97.1],'Winnipeg')
TORONTO_MARKER = Marker([43.7, -79.4],'Toronto')
OTTAWA_MARKER = Marker([45.4, -75.7],'Ottawa')

opsmap_vis = Map(center=CANADA_LL, zoom=3,
        markers=[
            VANCOUVER_MARKER,
            EDMONTON_MARKER,
            CALGARY_MARKER,
            REGINA_MARKER,
            WINNIPEG_MARKER,
            TORONTO_MARKER,
            OTTAWA_MARKER,
            ]).render()

# Charts
#---------------------------------------------------------------------
def get_traffic_graph():
    labels = 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    data   = [(m, random.randint(1,100), random.randint(1,100)) for m in labels]
    graph = line(data, title='observations')#[['a','b','c','d'],[1,2,3,4]])
    return str(graph)

def get_operation_type_graph():
    types = ['Photo','Video','Sound','Number']
    stats = Counter(random.choice(types) for n in range(20))
    graph = hbar(stats.items())
    return str(graph)

vis1data = [randmetric() for n in range(10)]

class MyView(zoom.mvc.View):

    def index(self):

        metric_labels = [
            'operations',
            'observations',
            'projects',
            'operatives',
            'scientists',
            'operatives',
            ]

        opsmap = opsmap_vis
        vis1 = get_traffic_graph()
        vis2 = get_operation_type_graph()
        feed = twitter_widget
        metrics = ''.join(metric_template % (randmetric(), t) for i,t in enumerate(metric_labels))

        content = page_template % locals()
        return zoom.page(content, css=css)

class MyCollection(zoom.mvc.Controller):
    
    def create_button(self):
        return page('test')


collection = MyCollection()
view = MyView()
