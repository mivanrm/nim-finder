import flask
from flask import render_template,request,flash,redirect,url_for,session,logging,Flask,jsonify
from flask_mysqldb import MySQL
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from wtforms.fields.html5 import EmailField
from passlib.hash import sha256_crypt
from data import articles

Articles=articles()


app = flask.Flask(__name__)
app.config["DEBUG"]=True
mysql = MySQL()
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'nim'
mysql = MySQL(app)
@app.route('/')
def main():
    return render_template('main.html')

@app.route('/testing',methods=["GET", "POST"])
def nim():
    if request.method == "POST":
        '''a=request.form['testquery']+"%"'''
        req=request.json
        a=req['testquery']+"%"
        print(a)
        cur=mysql.connection.cursor()
        result=cur.execute("SELECT * FROM mahasiswa WHERE (nimtpb LIKE %s OR LOWER(nama) LIKE LOWER(%s) OR nimjurusan LIKE %s)",(a,a,a,) )
        dbresult=cur.fetchall()
        return jsonify(dbresult)
    return render_template('nim.html')
    
@app.route('/articles')
def article():
    return render_template('article.html',articles=Articles)
    
class RegisterForm(Form):
    Name = StringField('Name', validators=[validators.input_required()])
    Email  = EmailField('Email', validators=[validators.input_required()])
    Username= StringField('Username', validators=[validators.input_required()])
    Password=PasswordField('Password',validators=[validators.length(min=8,max=20),validators.input_required()])
@app.route('/register',methods =['GET','POST'])
def register():
    regForm=RegisterForm(request.form)
    if request.method == 'POST' and regForm.validate():
        return render_template('register.html')
    return render_template('register.html',form=regForm)
if __name__ == '__main__':
    app.run()