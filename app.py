# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request

from flask_pymongo import PyMongo
from flask import redirect
from flask import session, url_for

from flask import redirect



# -- Initialization section --
app = Flask(__name__)
app.secret_key = '_5#y2L"F4Q8z\n\xec]/'

app.config['MONGO_DBNAME'] = 'login'
app.config['MONGO_URI'] = 'mongodb+srv://admin:cFnNoYnzCu8BGFL5@cluster0.pmjhw.mongodb.net/login?retryWrites=true&w=majority'
mongo = PyMongo(app)

# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    #return render_template('information1.html')
    return render_template('index.html')


@app.route('/signup', methods = ['GET','POST'])
def signup():
    # Are they posting with the form?
    if request.method == 'POST':
        # Connect to database
        users = mongo.db.users
        # Do something with the database - Does anyone have this name?
        existing_user = users.find_one({'name': request.form['username']})

        # Does user not exist? Add to the database!
        if existing_user is None:
            # Add the user to the database
            users.insert({'name': request.form['username'], 'password': request.form['password']})
            # Make a session for the user
            session['username'] = request.form['username']
            return render_template('index.html')
        return 'The username already exists'
    return render_template('signups.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    # Connect to the database
    users = mongo.db.users
    # Get the login for the user!
    login_user = users.find_one({'name': request.form['username']})
    # Check that the password matches
    if login_user:
        # Check does the password they put in match the password in the database
        if request.form['password'] == login_user['password']:
            # start a session
            session['username'] = request.form['username']
            return render_template('index.html')
    # Password or username incorrect?
    return 'Invalid username/password combination'

# LOGOUT ROUTE
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')



@app.route('/your_info', methods = ['GET','POST'])
def your_info():
    if request.method == 'GET':
       return render_template("information1.html")
    else:

        #name = request.form['user_name']
        #date = request.form['date']

        name = request.form['user_name']

        goal_amount = int(request.form['goal_amount'])
        monthly_expenses = int(request.form['monthly_expenses'])
        pay_per_hour = int(request.form['pay_per_hour'])
        hours_worked = int(request.form['hours_worked'])

        add_income = int(request.form['add_income'])
        add_expenses = int(request.form['add_expenses'])
        savings = ((((pay_per_hour*hours_worked)*4) + add_income) - (monthly_expenses + add_expenses))
        goal_percent = (savings / goal_amount) * 100

        # goal_percent = str(goal_percent)
        # print(goal_percent)        
        if savings >= goal_amount:
            return render_template ('savings_goal.html', savings = savings, goal_amount = goal_amount, goal_percent = goal_percent)
            #(f"Hello {name}, you reached your monthly savings goal of {goal_amount} with ${savings-goal_amount} to spare!")
        else:
            need_more = (goal_amount - savings)
            return  render_template('need_more.html', savings = savings, goal_amount = goal_amount, goal_percent = goal_percent)
            #(f"you did not reach your savings goal, you need {need_more} more dollars to reach your goal")

@app.route('/your_budget',  methods = ['GET','POST'])
def your_budget():
    if request.method == 'GET':
       return render_template('viewer_budget.html')
    else:
        food_budget = int(request.form['food_budget'])
        clothing_budget = int(request.form['clothing_budget'])
        entertainment_budget = int(request.form['entertainment_budget'])
        tuition_budget = int(request.form['tuition_budget'])
        transportation_budget = int(request.form['transportation_budget'])
        rent_budget = int(request.form['rent_budget'])
        other_budget = int(request.form['other_budget'])
        # total_budget = (food_budget + clothing_budget + entertainment_budget)
        # food_percent = food_budget / total_budget
        # clothing_percent = clothing_budget / total_budget
        # entertainment_percent = entertainment_budget / total_budget
        return render_template('viewer_budget.html', food_budget = food_budget, clothing_budget = clothing_budget, entertainment_budget = entertainment_budget, tuition_budget = tuition_budget, transportation_budget = transportation_budget, rent_budget = rent_budget, other_budget = other_budget)
