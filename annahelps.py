from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

from log_pass import acces_data


app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.mail.yahoo.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = acces_data['login']
app.config['MAIL_PASSWORD'] = acces_data['password']
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/')
def welcome():
     return render_template('home_page.html')


@app.route('/qestions')
def about_page():
     return render_template('about.html')


@app.route('/posts')
def posts_page():
     return render_template('articles.html')


@app.route('/articles')
def articles_page():
     return render_template('articles.html')


@app.route('/confirmed')
def confirmation():
     return render_template('confirmed.html')


@app.route('/buy', methods=['GET', 'POST'])
def buy_page():
     if request.method == 'POST':
          # getting the html inputs and referencing them
          name = request.form.get('name')
          phone = request.form.get('phone')
          message = request.form.get('message')
          the_whole_message ='Client`s name:'+ name +' Phone:'+ phone +' Message:'+ message
          # inputing the message in the correct order
          msg = Message("Психологическая консультация", sender='anna_ostapenko@yahoo.com', recipients=['maxarmyk@gmail.com', 'annaostapenkowork@gmail.com'])
          msg.body = the_whole_message
          mail.send(msg)
          return redirect(url_for('confirmation'))
     return render_template('buy.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0') #5000 
