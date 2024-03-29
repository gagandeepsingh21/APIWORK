from flask import Flask, render_template,request,url_for,redirect,flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'bigkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appdata.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= True
db = SQLAlchemy(app)


#Creating model table for our CRUD database
class data(db.Model):
   id = db.Column(db.Integer, primary_key = True, autoincrement=True)
   Fname=db.Column(db.String(100), nullable=False)
   Lname=db.Column(db.String(100), nullable=False)
   Email=db.Column(db.String(100), nullable=False)
   message=db.Column(db.String(100), nullable=False)
 
   
  
   def __init__(self, Fname, Lname, Email, message):
      self.Fname=Fname
      self.Lname=Lname
      self.Email=Email
      self.message=message
      
#this route is for inserting data to mysql database via html forms
@app.route('/insert', methods = ['POST','GET'])
def insert():
 
    if request.method == 'POST':
 
        Fname=request.form['Fname']
        Lname=request.form['Lname']
        Email=request.form['Email']
        message=request.form['Message']
 
 
        my_data = data(Fname,Lname,Email,message)
        db.session.add(my_data)
        db.session.commit()
 
        flash("Message sent Successfully")
 
        return render_template("contact.html")
      
      

@app.route("/")
def home():
   return render_template("index.html")

@app.route("/index.html")
def home_1():
   return render_template("index.html")

@app.route("/portfolio-page.html")
def second():
   return render_template("portfolio-page.html")

@app.route("/portfolioII-page.html")
def third():
   return render_template("portfolioII-page.html")

@app.route("/contact.html")
def contact():
   return render_template("contact.html")


if __name__ == "__main__":
   app.run(debug=True)