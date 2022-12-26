from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

'''
src:
https://www.youtube.com/watch?v=71EU8gnZqZQ
'''
app = Flask(__name__)

'''inizializzazione db '''
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET KEY'] = 'thisisasecretkey' #vedere come cambiare la pw in chiaro


'''
sintassi si sqlite per creare una tabella di databse con 3 colonne. 
per creare la tabella, da terminale entrare nel terinale python e usre i comandi:
from app import db
db.create_all()
exit()
a questo punto il file databsde.db si è riempito con la tabella 
da terminale normale usare :
sqlite3 database.db --> entra nel terminale sqlite
.tables --> verifica le tabelle create

'''
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)


@app.route('/')
def  home():
    return render_template ('home.html')

@app.route('/login')
def  login():
    return render_template ('login.html')


@app.route('/register')
def  register():
    return render_template ('register.html')


if __name__=='__main__':
    app.run(debug=True)