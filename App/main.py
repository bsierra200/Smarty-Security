from __future__ import division, print_function
from flask import (
    Flask,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
   
)
import sys
import os
import glob
import re
from werkzeug.utils import secure_filename
from werkzeug.utils import secure_filename
from models import TextApp
from flask import flash
from datetime import datetime
import forms

app = Flask(__name__)
app.secret_key = 'somesecretkeythatonlyishouldknow'  #llave secreta para manejo de sesiones
app.config["DEBUG"] = True


#Clase utilizada para el manejo de sesiones y login de la aplicacion
class User:
    def __init__(self, id, username, password,email,image):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.image = image

    def __repr__(self):
        return f'<User: {self.username}>'

users = []
users.append(User(id=1, username='Bryan', password='123456', email='bsierra@smartydreams.com', image= 'src=/static/assets/img/prof1.png'))
users.append(User(id=2, username='Daniel', password='123456', email='dsierra@smartydreams.com',image= 'src=/static/assets/img/prof2.png'))
users.append(User(id=3, username='Dylan', password='123456', email='dylan@example.com',image= 'src=/static/assets/img/Logo.png'))
users.append(User(id=4, username='Estela Arreola', password='123456', email='estelabry36@gmail.com',image= 'src=/static/assets/img/Logo.png'))
#****************************************************************************************Fin clase User


#Datos estaticos  para etiquetas en pantallas de la aplicacion
textTransaction = TextApp(TextApp.tituloSale,TextApp.tituloCheckIn,TextApp.tituloCan,TextApp.tituloDev,TextApp.tituloCheRe,TextApp.btnIng,TextApp.btnAc,TextApp.btnReg,
                            TextApp.referencia,TextApp.monto,TextApp.fecha,TextApp.aprobacion,TextApp.saludo,TextApp.tituloReport,TextApp.tituloConf,TextApp.usuario,TextApp.searchReports,TextApp.tituloLoginFaces) 



#Funcion para mostrar error de url's 
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error404.html'),404
    
@app.errorhandler(500)
def base_error_handler(e):
    return render_template('error404.html'),500 



#Funcion que se utiliza para el manejo de login correcto
@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user
        
        


#Funcion para el manejo de ruta de pantalla login
@app.route('/', methods=['GET', 'POST'])
def login():
   
    #Creamos un objeto de Formulario
    formulario = forms.FormLogin(request.form)
    if request.method == 'POST' and formulario.validate():
        session.pop('user_id', None)
       
        username = request.form['username']
        password = request.form['password']
        
        
        user = [x for x in users if x.username == username][0]
        
      
        if user and user.password == password:
            session['user_id'] = user.id
            os.system('python capture.py' + '  ' + username )
            
        flash("Contraseña invalida ",  "ERROR")
        return redirect(url_for('login'))

    return render_template('login.html', form = formulario,textTransaction = textTransaction)        




@app.route('/registro')
def registro():
    formulario = forms.FormLogin(request.form)
    return render_template('login2.html', form = formulario,textTransaction = textTransaction) 



@app.route('/home')
def index():
    return render_template('index1.html')



app.run()