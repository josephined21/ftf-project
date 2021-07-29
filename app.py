# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask_pymongo import PyMongo
from flask import redirect
from flask import session, url_for

from datetime import date

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
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    # Are they posting with the form?
    if request.method == 'POST':
        # Connect to database
        users = mongo.db.users
        # Do something with the database - Does anyone have this name?
        existing_user = users.find_one({'name': request.form['user_name']})

        # Does user not exist? Add to the database!
        if existing_user is None:
            # Add the user to the database
            todays_date = date.today()
            todays_month = todays_date.month
            todays_year = todays_date.year

            if todays_month == 1:
                month = 'january'
            elif todays_month == 2:
                month = 'february'
            elif todays_month == 3:
                month = 'march'
            elif todays_month == 4:
                month = 'april'
            elif todays_month == 5:
                month = 'may'
            elif todays_month == 6:
                month = 'june'
            elif todays_month == 7:
                month = 'july'
            elif todays_month == 8:
                month = 'august'
            elif todays_month == 9:
                month = 'september'
            elif todays_month == 10:
                month = 'october'
            elif todays_month == 11:
                month = 'november'
            elif todays_month == 12:
                month = 'december'

            users.insert({'name': request.form['user_name'], 'username': request.form['username'], 'password': request.form['password'], str(todays_year) : {month: {'goal amount': request.form['goal_amount'], 'monthly expenses': request.form['monthly_expenses'],
                         'pay per hour': request.form['pay_per_hour'], 'hours worked': request.form['hours_worked'], 'additional income': request.form['add_income'], 'additional expenses': request.form['add_expenses']}}})
            # Make a session for the user
            session['username'] = request.form['user_name']
            return render_template('index.html')
        return 'The username already exists'
    return render_template('signups.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    # Connect to the database
    users = mongo.db.users
    # Get the login for the user!
    login_user = users.find_one({'username': request.form['username']})
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

@app.route('/login_button')
def login_button():
    return render_template('login_copy.html')

@app.route('/about_us')
def about_us():
   return render_template('about_us.html')

@app.route('/your_info', methods=['GET', 'POST'])
def your_info():
    if request.method == 'GET':
        todays_date = date.today()
        todays_month = todays_date.month
        todays_year = todays_date.year
        year = str(todays_year)

        if todays_month == 1:
            month = 'january'
        elif todays_month == 2:
            month = 'february'
        elif todays_month == 3:
            month = 'march'
        elif todays_month == 4:
            month = 'april'
        elif todays_month == 5:
            month = 'may'
        elif todays_month == 6:
            month = 'june'
        elif todays_month == 7:
            month = 'july'
        elif todays_month == 8:
            month = 'august'
        elif todays_month == 9:
            month = 'september'
        elif todays_month == 10:
            month = 'october'
        elif todays_month == 11:
            month = 'november'
        elif todays_month == 12:
            month = 'december'

        users = mongo.db.users
        user = users.find_one({'username': session['username']})
        print(user)

        goal_amount = user[year][month]['goal amount']
        monthly_expenses = user[year][month]['monthly expenses']
        pay_per_hour = user[year][month]['pay per hour']
        hours_worked = user[year][month]['hours worked']
        add_income = user[year][month]['additional income']
        add_expenses = user[year][month]['additional expenses']

        savings = ((pay_per_hour * hours_worked * 4) + add_income) - (monthly_expenses + add_expenses)
        goal_percent = (savings / goal_amount) * 100

        if savings >= goal_amount:
            return render_template ('savings_goal.html', savings = savings, goal_amount = goal_amount, goal_percent = goal_percent)
        else:
            need_more = (goal_amount - savings)
            return  render_template('need_more.html', savings = savings, goal_amount = goal_amount, goal_percent = goal_percent)
    else:
        goal_amount = int(request.form['goal_amount'])
        monthly_expenses = int(request.form['monthly_expenses'])
        pay_per_hour = int(request.form['pay_per_hour'])
        hours_worked = int(request.form['hours_worked'])
        add_income = int(request.form['add_income'])
        add_expenses = int(request.form['add_expenses'])
        savings = ((pay_per_hour * hours_worked * 4) + add_income) - (monthly_expenses + add_expenses)
        goal_percent = (savings / goal_amount) * 100

        todays_date = date.today()
        todays_month = todays_date.month
        todays_year = todays_date.year
        year = str(todays_year)

        if todays_month == 1:
            month = 'january'
        elif todays_month == 2:
            month = 'february'
        elif todays_month == 3:
            month = 'march'
        elif todays_month == 4:
            month = 'april'
        elif todays_month == 5:
            month = 'may'
        elif todays_month == 6:
            month = 'june'
        elif todays_month == 7:
            month = 'july'
        elif todays_month == 8:
            month = 'august'
        elif todays_month == 9:
            month = 'september'
        elif todays_month == 10:
            month = 'october'
        elif todays_month == 11:
            month = 'november'
        elif todays_month == 12:
            month = 'december'

        users = mongo.db.users
        user = users.find_one({'name': session['username']})

        if month in user[year]:
            user[year][month]['goal amount'] = goal_amount
            user[year][month]['monthly expenses'] = monthly_expenses
            user[year][month]['pay per hour'] = pay_per_hour
            user[year][month]['hours worked'] = hours_worked
            user[year][month]['additional income'] = add_income
            user[year][month]['additional expenses'] = add_expenses

            myquery = {'name': session['username']}
            newvalues = { "$set": { year: user[year] } }
            users.update_one(myquery, newvalues)
        else:
            print("there")
            user[year][month] = {'goal amount': goal_amount, 'monthly expenses': monthly_expenses, 'pay per hour': pay_per_hour, 'hours worked': hours_worked, 'additional income': add_income, 'additional expenses': add_expenses}
            print(user[year])

            myquery = {'name': session['username']}
            newvalues = { "$set": { year: user[year] } }
            users.update_one(myquery, newvalues)
            
        if savings >= goal_amount:
            return render_template ('savings_goal.html', savings = savings, goal_amount = goal_amount, goal_percent = goal_percent)
        else:
            need_more = (goal_amount - savings)
            return render_template('need_more.html', savings = savings, goal_amount = goal_amount, goal_percent = goal_percent)

@app.route('/your_budget',  methods = ['GET','POST'])
def your_budget():
    if request.method == 'GET':
       return render_template('viewer_budget.html')
    else:
        if request.form['food_budget'] == "":
            food_budget = 0
        else: 
            food_budget = int(request.form['food_budget'])
        
        if request.form['clothing_budget'] == "":
            clothing_budget = 0
        else:
            clothing_budget = int(request.form['clothing_budget'])

        if request.form['entertainment_budget'] == "":
            entertainment_budget = 0
        else: 
            entertainment_budget = int(request.form['entertainment_budget'])

        if request.form['tuition_budget'] == "":
            tuition_budget = 0
        else: 
            tuition_budget = int(request.form['tuition_budget'])
        
        if request.form['transportation_budget'] == "":
            transportation_budget = 0
        else: 
            transportation_budget = int(request.form['transportation_budget'])
        
        if request.form['rent_budget'] == "":
            rent_budget = 0
        else: 
            rent_budget = int(request.form['rent_budget'])

        if request.form['essentials_budget'] == "":
            essentials_budget = 0
        else: 
            essentials_budget = int(request.form['essentials_budget'])
        
        if request.form['other_budget'] == "":
            other_budget = 0
        else: 
            other_budget = int(request.form['other_budget'])
        
        return render_template('viewer_budget.html', food_budget = food_budget, clothing_budget = clothing_budget, entertainment_budget = entertainment_budget, tuition_budget = tuition_budget, transportation_budget = transportation_budget, rent_budget = rent_budget, essentials_budget = essentials_budget, other_budget = other_budget)
