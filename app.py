# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    #return render_template('information1.html')
    return render_template('index.html')

@app.route('/your_info', methods = ['GET','POST'])
def your_info():
    if request.method == 'GET':
       return render_template("information1.html")
    else:
        name = request.form['user_name']
        goal_amount = int(request.form['goal_amount'])
        monthly_expenses = int(request.form['monthly_expenses'])
        pay_per_hour = int(request.form['pay_per_hour'])
        hours_worked = int(request.form['hours_worked'])
        savings = ((pay_per_hour*hours_worked) - monthly_expenses)
        if savings >= goal_amount:
            return (f"Hello {name}, you reached your monthly savings goal of {goal_amount} with ${savings-goal_amount} to spare!")
        else:
            return "you did not reach your savings goal"

@app.route('/your_stats')
def your_stats():
    return render_template('viewer_stats.html')
    
