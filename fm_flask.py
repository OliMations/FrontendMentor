import flask, os

page = flask.Blueprint('frontendmentor', __name__, static_folder="/", static_url_path="/view", subdomain="frontendmentor")


@page.route("/")
@page.route("/home")
def fm_home():
    files = os.listdir("FrontendMentor")
    browser = [file + "/index.html" for file in files if file.startswith("FM")]
    
    return flask.render_template("fm_index.html", browser=browser) 

# @page.route("/view/<location>")
# def fm_display(location):
#     return flask.redirect(flask.url_for("static", filename=f"{location}/index.html"))
    