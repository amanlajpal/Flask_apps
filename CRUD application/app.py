from flask import render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

from flask import Flask
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fly2.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']='False'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first = db.Column(db.String(80), nullable=False)
    last = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    social_handle = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.first

Data=[{'first':'aman','last':'lajpal','email':'aman lajpal','social_handle':'@aman'},{'first':'aman','last':'lajpal','email':'aman lajpal','social_handle':'@aman'}]


@app.route('/',methods=['GET','POST'])
def homepage():
    if request.method=='POST':
        first=request.form['First']
        last=request.form['Last']
        email=request.form['Email']
        social=request.form['Social']
        Users=User(first=first,last=last,email=email,social_handle=social)
        db.session.add(Users)
        db.session.commit()
    allusers=User.query.all()
    return render_template('form.html',allusers=allusers,Data=Data)

@app.route('/edit/<int:id>',methods=['GET','POST'])
def edit(id):
    if request.method=='POST':
        first=request.form['First']
        last=request.form['Last']
        email=request.form['Email']
        social=request.form['Social']
        Useredit=User.query.filter_by(id=id).first()
        Useredit.first=first
        Useredit.last=last
        Useredit.email=email
        Useredit.social_handle=social
        db.session.add(Useredit)
        db.session.commit()
        return redirect('/')
        
    Useredit=User.query.filter_by(id=id).first()
    return render_template('edit.html',Useredit=Useredit)


@app.route('/delete/<int:id>')
def delete(id):
    Userdel=User.query.filter_by(id=id).first()
    db.session.delete(Userdel)
    db.session.commit()
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True,port=8000)
