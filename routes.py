from flask import Flask, render_template, request, flash, json



app = Flask(__name__)

app.secret_key = 'development key'

#mail.init_app(app)

@app.route('/')
def home():
  return render_template('changes.html')
  
if __name__ == '__main__':
  app.run(debug=True)
