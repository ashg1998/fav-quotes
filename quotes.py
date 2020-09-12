from flask import Flask, render_template, request,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:qwerty@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI']  = 'postgres://uiysmzrpbebndt:5ddc604df36cdfb8914a5c326b9e1e1d351f6ed543b3bd6a14d464f0e8a95c2b@ec2-34-232-212-164.compute-1.amazonaws.com:5432/d1q3t8smgvbits'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Favquotes(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(120), nullable=True)
    email = db.Column(db.String(120), nullable=False)

@app.route('/')
def index():
    result = Favquotes.query.all()
    return render_template('index.html',result = result)



@app.route("/quotes")
def quotes():
    return render_template('quotes.html')

@app.route("/process",methods = ['GET','POST'])

def process():
    if (request.method == 'POST'):
        
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Favquotes(name=name, phone_num = phone, msg = message, date= datetime.now(),email = email )
        db.session.add(entry)
        db.session.commit()



    return redirect(url_for('index'))

if __name__=="__main__":
    app.run(debug=True)