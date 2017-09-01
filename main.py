from flask import Flask
from flask import request
from flask import render_template
from send_mail import EmailFunctions
import os




app = Flask(__name__)
@app.route('/')
def my_form():
    return render_template("index.html")

@app.route('/send_mail',methods=['POST'])
def my_form_post():

    email = request.form['to_address']
    count = int(request.form['count'])
    msg =   request.form['text']

    obj = EmailFunctions()
    obj.send_emails(count=count, receiver=email,msg=msg)

    return str(count)+' Emails Sent!'+ ' To '+email

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
