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

@app.route('/your_budget',  methods = ['GET','POST'])
def your_stats():
    if request.method == 'GET':
       return render_template('viewer_budget.html')
    else:
        food_budget = int(request.form['food_budget'])
        clothing_budget = int(request.form['clothing_budget'])
        entertainment_budget = int(request.form['entertainment_budget'])
        total_budget = (food_budget + clothing_budget + entertainment_budget)
        food_percent = food_budget / total_budget
        clothing_percent = clothing_budget / total_budget
        entertainment_percent = entertainment_budget / total_budget
