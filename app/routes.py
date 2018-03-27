from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
    user = {'username': "Michelangelo"}

    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beuatiful day in Vancouver!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)
