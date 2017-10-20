from flask import Flask, render_template, request, flash, json



application = Flask(__name__)

application.secret_key = 'development key'

#mail.init_app(app)

@application.route('/')
def home():
  return render_template('changes.html')
  
if __name__ == '__main__':
  #application.run(debug=True)
  application.run(debug=True)

