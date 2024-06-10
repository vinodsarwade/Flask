from flask import Flask,render_template, url_for
from forms import RegistrationForm,LoginForm
app = Flask(__name__)


app.config['SECRET_KEY'] = '9ec6e9a6ff41cfb3de5bb95fb2a51c40'
posts = [
    {
        "author":"vinod",
        "title":"Flask APP 1",
        "content":"First post content",
        "date":"june 9,2024"
    },
    {
        "author":"vishal",
        "title":"Flask APP 2",
        "content":"second post content",
        "date":"june 10,2024"
    }
]

@app.route("/")
@app.route("/Home") #here we handling two routes for single function
def home():
    return render_template('home.html', posts=posts) #here in this route we are rendering this posts dict in home and about html page


@app.route("/about")
def about():
    return render_template('about.html',title = 'about') #rendering title of about page 

@app.route("/register")
def register():
    form  = RegistrationForm()
    return render_template('register.html',title ='Register',form=form)



@app.route("/login")
def login():
    form  = LoginForm()
    return render_template('login.html',title ='Login',form=form)

if __name__=="__main__":
    app.run(debug=True)
