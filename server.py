from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
def index():
    session['number'] = random.randrange(0,101)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    if request.form['action'] == 'reset':
        session.pop('number')
        return redirect('/')
    else:
        session['guess'] = int(request.form['guess'])
        if session['guess'] > session['number']:
            return render_template('tooHigh.html')
        elif session['guess'] < session['number']:
            return render_template('tooLow.html')
        else:
            return render_template('justRight.html')

app.run(debug=True)
