from flask import Flask, render_template, request
import random
import os


app = Flask(__name__)

choices = ['rock', 'paper', 'scissors']

def get_result(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "You lose!"

@app.route('/', methods=['GET', 'POST'])
def index():
    user_choice = None
    computer_choice = None
    result = None

    if request.method == 'POST':
        user_choice = request.form['choice']
        computer_choice = random.choice(choices)
        result = get_result(user_choice, computer_choice)

    return render_template('index.html', user_choice=user_choice, computer_choice=computer_choice, result=result)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
