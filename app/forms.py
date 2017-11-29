# -*- coding: utf-8 -*- 
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import validators
from wtforms.fields import TextField, TextAreaField, SubmitField, StringField
from wtforms.validators import Required
from wtforms import DateField,DateTimeField,IntegerField
import localsettings



class OrderTable(FlaskForm):
	 name = TextField("name",[validators.Required("Please enter your name .")],description=u"Ім'я*")
	 email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("check your email address")],description="Email*")
	 phone=TextField("Phone",[validators.Required("Please enter your phone.")],description=u"Телефон*")
	 #time=TextField("Time",[validators.Required("Please enter your time.")],description=u"Час*")
	 dt = TextField("Date",[validators.Required("Please enter your phone.")],description=u"Дата*")
	 time=TextField(validators=[Required()],description=u"Час*")
	 message = TextAreaField("Message",description=u"Додаткові побажання")
	 quant = IntegerField([validators.Required("")],description=u"К-ть людей*")
	 #recaptcha = RecaptchaField()
	 submit = SubmitField("Готово")
class ContactForm(FlaskForm):
	 name = TextField("name",[validators.Required("Please enter your name .")],description=u"Ім'я*")
	 email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("check your email address")],description="Email*")
	 message = TextAreaField("Message",description=u"Додаткові побажання")
	 subject = TextField("subject",[validators.Required("Please enter your name .")],description=u"Тема*")
	 #recaptcha = RecaptchaField()
	 submit = SubmitField("Відправити")

class MyForm(FlaskForm):
     name = StringField('name', validators=[Required()])
     submit = SubmitField('Register')
class DateForm(FlaskForm):
    dt = TextField(validators=[Required()])
    time=TextField(validators=[Required()])