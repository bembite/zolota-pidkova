# -*- coding: utf-8 -*- 
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import validators
from wtforms.fields import TextField, TextAreaField, SubmitField, StringField
from wtforms.validators import Required
from wtforms import DateField
import localsettings



class OrderTable(FlaskForm):
	 name = TextField("name",[validators.Required("Please enter your name .")],description=u"Ім'я*")
	 email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("check your email address")],description="Email")
	 phone=TextField("Phone",[validators.Required("Please enter your phone.")],description=u"Телефон*")
	 time=TextField("Time",[validators.Required("Please enter your time.")],description=u"Час*")
	 message = TextAreaField("Message",[validators.Required("Please enter your message.")],description=u"Додаткові побажання")
	 #recaptcha = RecaptchaField()
	 submit = SubmitField("Готово")

class MyForm(FlaskForm):
     name = StringField('name', validators=[Required()])
     submit = SubmitField('Register')
class DateForm(FlaskForm):
    dt = DateField('Pick a Date', format="%m/%d/%Y")