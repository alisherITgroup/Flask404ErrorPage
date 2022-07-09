from flask import Flask,render_template

app = Flask(__name__)


#Filterss
#upper
#lower
#safe
#striptags
@app.route('/')
def index():
    first_name = "Alisher"
    stuf = "This is bold tag <strong>Bold</strong>"
    favorite_pizza = ["Pepperoni","Cheeze","shfisfu","123","1232114"]
    return render_template('index.html',first_name=first_name,
    stuf = stuf,
    favorite_pizza=favorite_pizza
    )

@app.route('/user/<name>')
def user(name):
    return render_template("user.html",user_name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"),500