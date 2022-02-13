from Flask import flask
from flask import render_template


app=Flask(__name__)

@app.route('/')
def mainhome():
  return render_template('mains.html')

if __name__=='__main__':
  app.run()
