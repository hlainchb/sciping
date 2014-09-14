
from model import *

css = """
.our-team {
    margin-top: 2em;
}
.person {
    height: 150px;
    margin-bottom: 50px;
}
.headshot {
    width: 100px;
    height: 100px;
    display: inline;
    float: left;
    margin-right: 10px;
    border-radius: 75px;
    -webkit-border-radius: 75px;
    -moz-border-radius: 75px;
}
.bio {
    float: left;
    margin-top: 20px;
}
.bio h3 {
    color: #444;
    font-size: 1.4em;
    font-weight: bold;
    margin: 0;
    padding: 0;
}
.bio h4 {
    font-weight: normal;
    font-size: 1.0em;
    margin: 0;
    padding: 0;
    margin-bottom: 5px;
}
.bio p {
    font-weight: normal;
    font-size: 0.9em;
    margin: 0;
}
"""

tpl =  """
<div class="row">

    <div class="col-md-6 person">
        <img src="http://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Marie_Curie_c1920.jpg/225px-Marie_Curie_c1920.jpg" alt="photo" class="headshot">
        <div class="bio">
            <h3>
                <a href="/team/marie-curie">Marie Curie</a>
            </h3>
            <h4>Physicict and Chemist</h4>
            <p>
                <a target="_window" href="http://www.twitter.com/">@mariecurie</a>
            </p>
        </div>
    </div>

    <div class="col-md-6 person">
        <img src="http://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Ada_Lovelace_in_1852.jpg/220px-Ada_Lovelace_in_1852.jpg" alt="photo" class="headshot">
        <div class="bio">
            <h3>
                <a href="/team/marie-curie">Ada Lovelace</a>
            </h3>
            <h4>Mathematician and Computer Scientist</h4>
            <p>
                <a target="_window" href="http://www.twitter.com/">@mariecurie</a>
            </p>
        </div>
    </div>

    <div class="col-md-6 person">
        <img src="http://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Albert_Einstein_1947.jpg/220px-Albert_Einstein_1947.jpg" alt="photo" class="headshot">
        <div class="bio">
            <h3>
                <a href="/team/marie-curie">Albert Einstien</a>
            </h3>
            <h4>Physicist</h4>
            <p>
                <a target="_window" href="http://www.twitter.com/">@mariecurie</a>
            </p>
        </div>
    </div>

</div>
"""

class MyView(zoom.mvc.View):

    def index(self):

        #content = '<br>'.join(tpl for s in scientists)
        content = tpl

        return zoom.page(content, title='Scientists', css=css)

class MyCollection(zoom.mvc.Controller):
    pass


collection = MyCollection()
view = MyView()
