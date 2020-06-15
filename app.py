from flask import Flask, escape, request,render_template
from jacchlibs.readxls import readxls

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

@app.route('/給麵之人')
def To_the_person():
    return render_template ("To_the_person.html")

@app.route('/undertale')
def undertale():
    return render_template ("undertale.html")

@app.route('/鬼滅之刃')
def Demon_Blade():
    return render_template ("Demon_Blade.html")

@app.route('/choco')
def chocolate():
    return render_template ("chocolate.html")


@app.route('/hello')
def hea():
    a = request.args.get("a",0)
    b = request.args.get("b",0)
    return render_template ("index.html",a=a,b=b)

@app.route('/Minecraft')
def Minecraft():
    return render_template ("Minecraft.html")

@app.route('/deltarune')
def deltarune():
    a = request.args.get("a",0)
    b = request.args.get("b",0)
    return render_template ("deltarune.html",a=a,b=b)

@app.route('/Glitchtale')
def Glitchtale():
    a = request.args.get("a",0)
    b = request.args.get("b",0)
    return render_template ("Glitchtale.html",a=a,b=b)

@app.route('/Light')
def Light():
    a = request.args.get("a",0)
    b = request.args.get("b",0)
    return render_template ("Light.html",a=a,b=b)

@app.route('/Black_Plasma_Studios')
def Black_Plasma_Studios():
    a = request.args.get("a",0)
    b = request.args.get("b",0)
    return render_template ("Black_Plasma_Studios.html",a=a,b=b)

@app.route('/fan')
def fan():
    a = request.args.get("a",0)
    b = request.args.get("b",0)
    return render_template ("fan/index.html",a=a,b=b)

@app.route('/candy')
def candy():
    a = request.args.get("a",0)
    b = request.args.get("b",0)
    return render_template ("candy/index.html",a=a,b=b)

@app.route('/cookie')
def cookie():
    a = request.args.get("a",0)
    b = request.args.get("b",0)
    return render_template ("cookie/index.html",a=a,b=b)

@app.route('/cookie1')
def cookie1():
    a = request.args.get("a",0)
    b = request.args.get("b",0)
    return render_template ("cookie1/index.html",a=a,b=b)

@app.route('/bread')
def bread():
    a = request.args.get("a",0)
    b = request.args.get("b",0)
    return render_template ("bread/index.html",a=a,b=b)


@app.route('/master')
def master():
    a = request.args.get("name",0) 
    xls=readxls("db.xlsx")
    sheet=xls.read(a)  
    sheetnames=xls.sheetnames() 
    return render_template ("master/index.html",a=a,master=sheet,l=sheetnames)

 


