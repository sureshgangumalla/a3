from .database import Assign3Database as Db
from .passwordhasher import PasswordHasher
from flask import session, flash

class Owner:

    def __init__(self, owner_email=None, owner_password=None,
                 owner_cpassword=None):
        self.owner_email = owner_email
        self.owner_password = owner_password
        self.owner_cpassword = owner_cpassword

    def registerOwner(self,ownerRegForm):
        self.owner_email = ownerRegForm['owner_email']
        self.owner_password = ownerRegForm['owner_password']
        self.owner_cpassword = ownerRegForm['owner_cpassword']
        hasher = PasswordHasher()
        self.owner_password = hasher.hash(self.owner_password)
        self.owner_cpassword = hasher.hash(self.owner_cpassword)
        cnx = Db().data_connect()
        try:
            cur = cnx.cursor()
            print(self.owner_email)
            cur.execute("SELECT COUNT(1) FROM owner_registration WHERE owner_email = %s;", [self.owner_email])
            if cur.fetchone()[0]:
                return 1
            if self.owner_password == self.owner_cpassword:
                cur.execute("INSERT INTO owner_registration(owner_email,owner_password) VALUES(%s,%s)",
                            (self.owner_email, self.owner_password))
                cnx.commit()
                return 2
            else:
                return 3

            
            cnx.close()
        except Exception as e:
            flash("Error while registering a new owner %s",)


    def isalready_Owner(self, ownerLoginForm):
        self.owner_email = ownerLoginForm['owner_email']
        self.owner_password = ownerLoginForm['owner_password']
        cnx = Db().data_connect()
        hasher = PasswordHasher()

        try:
            cur = cnx.cursor()
            print(self.owner_email)
            self.owner_password = hasher.hash(self.owner_password)
            cur.execute("SELECT COUNT(1) FROM owner_registration WHERE owner_email = %s;", [self.owner_email])
            if cur.fetchone()[0]:
                print('User present')
                cur.execute("SELECT owner_password FROM owner_registration WHERE owner_email = %s;", [self.owner_email])
                for row in cur.fetchall():
                    if self.owner_password == row[0]:
                        session['owner_email'] = self.owner_email
                        return 1
                    else:
                        return 2
            else:
                return 3

        except Exception as e:
            # logging.error(e, "Error while adding a executing add_user()")
            flash("Error while validating the owner %s")

        finally:
            cnx.close()
            flash("Database connection closed")



    def get_apartments(self,owner_email):
        self.owner_email = owner_email
        print(self.owner_email)
        cnx = Db().data_connect()
        cur = cnx.cursor()
        cur.execute("SELECT * FROM apartment WHERE owner_email = %s;", [self.owner_email])
        apartments = cur.fetchall()
        return apartments
