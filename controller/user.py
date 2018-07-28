from .database import Assign3Database as Db
from .passwordhasher import PasswordHasher
from flask import session, flash



class User:

    def __init__(self, name=None, email=None, password=None,
                 cpassword=None, dob=None, country=None, firstname=None,
                 lastname=None, gender=None, phone=None, university=None,
                 branch=None, isSmoking=None, isVegetarian=None, isAlcoholic=None,
                 image=None):
        self.name = name
        self.email = email
        self.password = password
        self.cpassword = cpassword
        self.dob = dob
        self.country = country
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.phone = phone
        self.university = university
        self.branch = branch
        self.isSmoking = isSmoking
        self.isVegetarian = isVegetarian
        self.isAlcoholic = isAlcoholic
        self.image = image

    def parse_user(self, register_form):
        # logging.info("classes.user.parse_user()")
        self.name = register_form['name']
        print(self.name)
        self.email = register_form['email']
        self.password = register_form['password']
        self.cpassword = register_form['cpassword']
        hasher = PasswordHasher()
        self.password = hasher.hash(self.password)
        self.cpassword = hasher.hash(self.cpassword)
        self.dob = register_form['dob']
        self.country = register_form['country']

    def is_already_user(self, login_form):
        # could do this with just the primary key of the user, rest_name
        # logging.info("classes.user.get_user()")
        # todo make the password hashed
        # print('already_user called')
        cnx = Db().data_connect()
        hasher = PasswordHasher()

        try:
            print('inside try of already_user called')
            cur = cnx.cursor()
            self.email = login_form['email']
            self.email = login_form['email']
            print(self.email)
            self.password = login_form['password']
            self.password = hasher.hash(self.password)
            print(self.password)
            cur.execute("SELECT COUNT(1) FROM registration WHERE email = %s;", [self.email])
            if cur.fetchone()[0]:
                print('User present')
                cur.execute("SELECT password FROM registration WHERE email = %s;", [self.email])
                for row in cur.fetchall():
                    if self.password == row[0]:
                        print('User password is correct')
                        session['email'] = self.email
                        cnx.close()
                        return 1
                    else:
                        return 2
            else:
                return 3

        except Exception as e:
            # logging.error(e, "Error while adding a executing add_user()")
            flash("Error while validating the owner %s")

    def add_user(self):
        cnx = Db().data_connect()
        try:
            cur = cnx.cursor()
            cur.execute("SELECT COUNT(1) FROM registration WHERE email = %s;", [self.email])
            if cur.fetchone()[0]:
                return 1
            if self.password == self.cpassword:
                print('before execute')
                cur.execute("INSERT INTO registration(name,email,password,dob,country) VALUES(%s,%s,%s,%s,%s)", (self.name, self.email,self.password, self.dob, self.country))
                cnx.commit()
                cnx.close()
                print('after execute')
                return 2
            else:
                return 3

        except Exception as e:
            flash("Error while registering a new owner %s",)
        return 0

    def get_userDetails(self, email):
        cnx = Db().data_connect()
        try:
            cur = cnx.cursor()
            self.email = email
            cur.execute("SELECT * FROM user_profile WHERE email = %s;", [self.email])
            result = cur.fetchall()
            print(result)
            return result
        finally:
            cnx.close()

    def update_profile_details(self,editprofileform):
        cnx = Db().data_connect()
        try:
            cur = cnx.cursor()
            self.email = session['email']
            self.firstname = editprofileform['firstname']
            self.lastname = editprofileform['lastname']
            self.gender = 'Dummy'#editprofileform['gender']
            self.phone = editprofileform['phone']
            self.university = editprofileform['university']
            self.branch = editprofileform['branch']
            self.isSmoking = 'Dummy'#editprofileform['isSmoking']
            self.isVegetarian = 'Dummy'#editprofileform['isVegetarian']
            self.isAlcoholic = 'Dummy'#editprofileform['isAlcoholic']
            self.image = 'Dummy'#editprofileform['image']

            cur.execute("SELECT * FROM user_profile WHERE email = %s;", [self.email])
            result = cur.fetchall()
            if result:
                print('tried for update')
                cur.execute("UPDATE user_profile SET firstname=%s,lastname=%s,gender=%s,phone=%s,university=%s,branch=%s,isSmoking=%s,isVegetarian=%s,isAlcoholic=%s,image=%s WHERE email = %s;", [self.firstname, self.lastname, self.gender, self.phone, self.university, self.branch, self.isSmoking, self.isVegetarian, self.isAlcoholic, self.image, self.email])
            else:
                print('Insert in profile')
                cur.execute("INSERT INTO user_profile (firstname,lastname,gender,phone,university,branch,isSmoking,isVegetarian,isAlcoholic,image,email) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (self.firstname, self.lastname, self.gender, self.phone, self.university, self.branch, self.isSmoking, self.isVegetarian, self.isAlcoholic, self.image, self.email))
        finally:
            cnx.commit()
            cnx.close()

    def is_valid(self):
        if self.restaurant_password:
            return True
        return False

    def set_session_if_valid(self, login_form):
        session['logged_in'] = True
        session['rest_name'] = login_form['restaurant_name']

    def printname(self):
        print(self.name)

