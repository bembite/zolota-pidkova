# -*- coding: utf-8 -*- 
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import validators
from wtforms.fields import TextField, TextAreaField, SubmitField, StringField
from wtforms.validators import Required
from wtforms import DateField
import localsettings



class ContactForm(FlaskForm):
	 name = TextField("name",[validators.Required("Please enter your name .")])
	 email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("check your email address")])
	 phone=TextField("Phone",[validators.Required("Please enter your phone.")])
	 time=TextField("Time",[validators.Required("Please enter your time.")])
	 message = TextAreaField("Message",[validators.Required("Please enter your message.")])
	 #recaptcha = RecaptchaField()
	 submit = SubmitField("Send")

class MyForm(FlaskForm):
     name = StringField('name', validators=[Required()])
     submit = SubmitField('Register')
class DateForm(FlaskForm):
    dt = DateField('Pick a Date', format="%m/%d/%Y")