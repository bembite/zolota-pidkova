# -*- coding: utf-8 -*- 
from flask import Flask, render_template, request, flash, json
from forms import ContactForm,MyForm, DateForm
from flask_mail import Mail, Message
from datetime import date
from flask_wtf.recaptcha import RecaptchaField
import localsettings





application = Flask(__name__)

application.secret_key = 'development key'
#for mail
mail = Mail()
application.config["MAIL_SERVER"] = "smtp.gmail.com"
application.config["MAIL_PORT"] = 465
application.config["MAIL_USE_SSL"] = True
application.config["MAIL_USERNAME"] = 'volodya.ternopil1997@gmail.com'
application.config["MAIL_PASSWORD"] = localsettings.MAIL_PASSWORD
 
mail.init_app(application)
#for capcha
application.config['RECAPTCHA_PRIVATE_KEY']=localsettings.PRIVATE_KEY
application.config['RECAPTCHA_PUBLIC_KEY']=localsettings.PUBLIC_KEY




@application.route('/')
def home():
  return render_template('changes.html')

@application.route('/kek')
def maitanance():
  return render_template('maitanance.html')

@application.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()
 
  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('contact.html', form=form)
    else:
      msg = Message(form.phone.data, sender='volodya.ternopil1997@gmail.com', recipients=['volodya.ternopil1997@gmail.com'])
      msg.body = """
      From: %s <%s>
      %s
      """ % (form.name.data, form.email.data, form.message.data)
      mail.send(msg)
      return render_template('contact.html', success=True)
  elif request.method == 'GET':
    return render_template('contact.html', form=form)

@application.route('/test',methods=['GET','POST'])
def index():
	name1 = None
	form1 = MyForm(prefix='form1')
	name2 = None
	form2 = MyForm(prefix='form2')
	if form1.validate_on_submit() and form1.submit.data:
		print "form1"
		return render_template('multiforms.html',form1=form1,form2=form2)
	if form2.validate_on_submit() and form2.submit.data:
		print "form2"
		return render_template('multiforms.html',form1=form1,form2=form2)
	return render_template('multiforms.html',form1=form1,form2=form2)

@application.route('/time', methods=['post','get'])
def time():
    form = DateForm()
    if form.validate_on_submit():
        return form.dt.data.strftime('%x')
    return render_template('datepicker.html', form=form)

@application.route('/main', methods=['GET', 'POST'])
def main():
  form = ContactForm()
  print request
  if request.method == 'POST':
    if form.validate() == False:
      print form.validate()
      flash('All fields are required.')
      print "some fields not validated"
      return render_template('main.html', form=form, scroll=True)
    else:
      msg = Message(form.phone.data, sender='volodya.ternopil1997@gmail.com', recipients=['volodya.ternopil1997@gmail.com'])
      msg.body = """
      From: %s <%s>
      %s
      """ % (form.name.data, form.email.data, form.message.data)
      mail.send(msg)																																																																																																																																																																																																																																					
      return render_template('main.html', success=True, scroll=True)
  elif request.method == 'GET':
	return render_template('main.html', form=form)



  
if __name__ == '__main__':
  #application.run(debug=True)
  application.run(debug=True)

