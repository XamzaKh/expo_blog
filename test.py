from flask_mail import Mail, Message
from flask import Flask

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'blogexpo001@gmail.com'
app.config['MAIL_DEFAULT_SENDER'] = 'blogexpo001@gmail.com'
app.config['MAIL_PASSWORD'] = 'Expo001blog'


mail = Mail(app)

@app.route('/')
def index():
    msg = Message('Some text', recipients=['hamzat_haciev@mail.ru'])
    mail.send(msg)
    return 'Hello!'

if __name__ == "__main__":
    app.run(debug=True)