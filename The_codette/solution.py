from crypt import methods
from flask import Flask, render_template,request,redirect,flash,url_for

app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def welcome():
    return render_template("welcome.html")

@app.route('/register')
def reg():
    return render_template("register.html")

@app.route('/boards')
def board():
    return render_template("boards.html")  

@app.route('/attitude')
def attitude():
    return render_template("attitude.html") 

@app.route('/speed')
def speed():
    return render_template("speed.html") 

@app.route('/softSkill')
def softSkill():
    return render_template("softSkills.html") 

@app.route('/question')
def question():
    return render_template("question.html") 

@app.route('/login_validation', methods=['POST']) 
def login_validation():
    email=request.form.get('email')
    password=request.form.get('password')   
    return render_template("boards.html".format(email,password))  

@app.route('/registration_validation' ,methods=['POST']) 
def registration_validation():
    name=request.form.get('name')
    surname=request.form.get('surname')
    gender=request.form.get('gender')
    age=request.form.get('age')
    qualiification=request.form.get('qualification')
    return render_template("boards.html".format(name,surname,gender,age,qualiification))  


if __name__=="__main__":
    app.run(debug=True)