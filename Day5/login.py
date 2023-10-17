from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
   return 'Welcome %s on Skillologies Computer' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   user = request.form['nm']
   return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(host='192.168.39.165')
