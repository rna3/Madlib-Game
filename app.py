from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story, story2

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"
debug = DebugToolbarExtension(app)


@app.route('/')
def home_page():
    """Return homepage, shows form to select stories."""

    prompts = story.prompts

    return render_template("home_page.html", prompts = prompts)

@app.route('/story')
def story_page():
    """Return madlib story_page."""

    text = story.generate(request.args)
    return render_template("story_page.html", text = text)







    