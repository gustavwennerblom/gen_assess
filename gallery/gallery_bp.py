from flask import Blueprint, render_template
from gallery.forms import DemoForm

bp = Blueprint('gallery', __name__, template_folder='templates')


@bp.route('/', methods=['GET', 'POST'])
def index():
    form = DemoForm()
    if form.validate_on_submit():
        return "Form submitted"

    return render_template('index.html', form=form, idx=1)
