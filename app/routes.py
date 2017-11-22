# -*- coding: utf-8 -*- 
from flask import Flask, render_template, request, flash, json
from forms import ContactForm



application = Flask(__name__)

application.secret_key = 'development key'
#mail.init_app(app)
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
    return 'Form posted.'
 
  elif request.method == 'GET':
    return render_template('contact.html', form=form)

  
if __name__ == '__main__':
  #application.run(debug=True)
  application.run(debug=True)

