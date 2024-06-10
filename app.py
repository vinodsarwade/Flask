from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '9ec6e9a6ff41cfb3de5bb95fb2a51c40'

posts = [
    {
        "author": "vinod",
        "title": "Flask APP 1",
        "content": "First post content",
        "date": "June 9, 2024"
    },
    {
        "author": "vishal",
        "title": "Flask APP 2",
        "content": "Second post content",
        "date": "June 10, 2024"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login")
def login():
    form  = LoginForm()
    return render_template('login.html',title ='Login',form=form)



if __name__=="__main__":
    app.run(debug=True)
