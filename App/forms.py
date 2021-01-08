from wtforms   import Form
from flask_wtf import FlaskForm
from wtforms   import TextField , SubmitField , StringField, PasswordField ,SelectField
from wtforms   import validators, ValidationError
from wtforms.fields.html5  import EmailField



    
class FormLogin(Form):
        username = StringField('Usuario',
                            [
                    validators.required(message = 'El campo no debe ir vacio.'),
                     validators.length(min=4, max=30, message='El usuario no debe ser mayo a 20 caracteres.'),
                ])
        password = PasswordField('Password',
                            [ validators.required(message = 'El campo no debe ir vacio.'),
                             
                ])
        
