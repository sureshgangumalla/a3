from flask import Flask, render_template, request, redirect, flash, url_for, session, send_from_directory
from controller.user import User
from controller.owner import Owner
from controller.apartment import Apartment
import os

app = Flask(__name__)
app.secret_key = "super secret key"

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = User()
        user.parse_user(request.form)
        reg_result = user.add_user()
        print('insidePostRegister')
        if 1 == reg_result:
            print('User already exists')
            flash('User already exists, please login or try with another email')
            return render_template("signupStudent.html")
        elif 3 == reg_result:
            print('Confirm password does not match with password')
            flash('Confirm password does not match with password')
            return render_template("signupStudent.html")
        elif 2 == reg_result:
            print('new user added')
            session['email'] = request.form['email']
            return redirect(url_for("editprofile"))
    if request.method == 'GET':
        print('InsideGetRegister')

    return render_template("signupStudent.html")

@app.route('/signupowner', methods=['GET', 'POST'])
def registerowner():
    if request.method == 'POST':
        owner = Owner()
        reg_result = owner.registerOwner(request.form)
        if 1 == reg_result:
            print('User already exists')
            flash('User already exists, please login or try with another email')
            return render_template("signupOwner.html")
        elif 3 == reg_result:
            print('Confirm password does not match with password')
            flash('Confirm password does not match with password')
            return render_template("signupOwner.html")
        elif 2 == reg_result:
            session['owner_email'] = request.form['owner_email']
            return redirect(url_for("homeOwner"))
    return render_template("signupOwner.html")

@app.route('/loginowner', methods=['GET', 'POST'])
def loginowner():
    if request.method == 'POST':
        owner = Owner()
        if 1 == owner.isalready_Owner(request.form):
            session['logged_in'] = True
            session['owner_email'] = request.form['owner_email']
            return redirect(url_for("homeOwner"))
        elif 2 == owner.isalready_Owner(request.form):
            error = "Invalid Password"
            return render_template("loginOwner.html", error=error)
        elif 3 == owner.isalready_Owner(request.form):
            error = "User does not exist"
            return render_template("loginOwner.html", error=error)
    return render_template('loginOwner.html')


@app.route('/addApartment', methods=['GET', 'POST'])
def addApartment():
    if request.method == 'POST':
        apartment = Apartment()
        apartment.addApartment(request.form)
        return redirect(url_for("homeOwner"))
    return render_template('addNewApartment.html')


@app.route('/editprofile', methods=['GET', 'POST'])
def editprofile():
    print('editprofile entered')
    user = User()
    if request.method == 'POST':
        print('inside editprofile')
        user.update_profile_details(request.form)
        print('end of edit profile')
        return redirect(url_for("profile"))
    if request.method == 'GET':
        data = user.get_userDetails(session['email'])
        if data:
            firstname = data[0][0]
            print(firstname)
            lastname = data[0][1]
            gender = data[0][2]
            phone = data[0][3]
            university = data[0][4]
            branch = data[0][5]
            isSmoking = data[0][6]
            isVegetarian = data[0][7]
            isAlcoholic = data[0][8]
            print('GET entered')
            return render_template('profile-edit.html', firstname=firstname, lastname=lastname, phone=phone, university=university, branch=branch)
    print('No Get No Post')
    return render_template('profile-edit.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User()
        print('I am from Login')
        if 1 == user.is_already_user(request.form):
            session['logged_in'] = True
            session['email'] = request.form['email']
            print('user authenticated')
            return redirect(url_for("home"))
        elif 2 == user.is_already_user(request.form):
            error = "Invalid Password"
            return render_template("login.html", error=error)
        elif 3 == user.is_already_user(request.form):
            error = "User does not exist"
            return render_template("login.html", error=error)
    return render_template('login.html')


@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html')

@app.route('/homeOwner', methods=['GET', 'POST'])
def homeOwner():
    if request.method == 'GET':
        print('home owner get')
        owner = Owner()
        apartments = owner.get_apartments(session['owner_email'])
        print(len(apartments))
        if 0 == len(apartments):
            print('no apartments')
            return render_template('homeOwner.html')
        else:
            print('has apartments')
            return render_template('apartment_list.html', apartments=apartments)
    print('home owner not get')
    return render_template('homeOwner.html')


#
# @app.route('/apartmentlist', methods=['GET', 'POST'])
# def apartmentlist():
#     print('apartmentlist')
#     if request.method == 'GET':
#         return render_template('apartment_list.html')


@app.route('/profile', methods=['GET'])
def profile():
    if request.method == 'GET':
        user = User()
        email = session['email']
        data = user.get_userDetails(email)
        firstname = data[0][0]
        print(firstname)
        lastname = data[0][1]
        gender = data[0][2]
        phone = data[0][3]
        university = data[0][4]
        branch = data[0][5]
        isSmoking = data[0][6]
        isVegetarian = data[0][7]
        isAlcoholic = data[0][8]
        return render_template('profile.html', firstname=firstname, lastname=lastname, branch=branch, university=university, phone= phone)
    return render_template('profile.html')


if __name__ == '__main__':
    app.run(debug = True)