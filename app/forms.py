# -*- coding: utf-8 -*- 
from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields import TextField, TextAreaField, SubmitField
from wtforms.fields.html5 import EmailField

class ContactForm(FlaskForm):
	 name = TextField("name")
	 #email = TextField('Email address', [validators.DataRequired(), validators.Email("kek")])
	 email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("check your email address")])

	 #email = EmailField("Email",[validators.DataRequired("Please enter your email address."),validators.Email("Please enter your email address.")])
	 phone=TextField("Phone")
	 time=TextField("Time")
	 message = TextAreaField("Message")
	 submit = SubmitField("Send")