from flask import Flask
import random

generated_number = random.randint(0, 10)

app = Flask(__name__)


@app.route('/')
def create_page():
    return "<h1>Guess the number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/xUn3CftPBajoflzROU/giphy-downsized-large.gif'>"


@app.route('/<int:number>')
def guess_number(number):
    if number < generated_number:
        return "<h1 style='color:red'>Too low,try again!</h1>" \
               "<img src='https://media.giphy.com/media/yFQ0ywscgobJK/giphy.gif'>"
    elif number > generated_number:
        return "<h1 style='color:red'>Too High,try again!</h1>" \
               "<img src='https://media.giphy.com/media/phJ6eMRFYI6CQ/giphy.gif'>"
    else:
        return "<h1 style='color:green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/Pnb5GTXdF54QxEaiLZ/giphy.gif'>"


if __name__ == '__main__':
    app.run(debug=True)
