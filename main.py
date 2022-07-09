from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    color = "#addabc"
    user_colors = ["#adb23","#346bdd","#dcd534","#ad523","#90876"]
    return render_template("user.html",user_name=name,user_colors=user_colors,color=color)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"),500