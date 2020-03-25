from flask import Flask, escape, request,render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template ("index.html")

@app.route('/about')
def about():
    return render_template ("about.html")

@app.route('/picture')
def picture():
    return render_template ("picture.html")

@app.route('/blog')
def blog():
    return render_template ("blog.html")

@app.route('/hello')
def hea():
    a = request.args.get("a",0)
    b = request.args.get("b",0)
    return render_template ("index.html",a=a,b=b)