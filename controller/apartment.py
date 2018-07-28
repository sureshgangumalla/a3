from .database import Assign3Database as Db
from .passwordhasher import PasswordHasher
from flask import session, flash

class Apartment:

    def __init__(self, apartment_Name=None, apartment_Location=None,
                 apartment_Type=None, owner_Contact=None, apartment_Description=None, image_URL=None,owner_Email=None):
        self.apartment_Name = apartment_Name
        self.apartment_Location = apartment_Location
        self.apartment_Type = apartment_Type
        self.owner_Contact = owner_Contact
        self.apartment_Description = apartment_Description
        self.image_URL = image_URL
        self.owner_Email = owner_Email

    def addApartment(self,addApartmentForm):
        self.apartment_Name = addApartmentForm['apartment_Name']
        self.apartment_Location = addApartmentForm['apartment_Location']
        self.apartment_Type = addApartmentForm['apartment_Type']
        self.owner_Contact = addApartmentForm['owner_Contact']
        self.apartment_Description = addApartmentForm['apartment_Description']
        self.image_URL = 'Dummy'   #addApartmentForm['image_URL']
        self.owner_Email = session['owner_email']
        cnx = Db().data_connect()
        print(self.owner_Email)
        try:
            cur = cnx.cursor()
            cur.execute("INSERT INTO apartment(apartment_Name,apartment_Location,apartment_Type,owner_Contact,apartment_Description,owner_Email,image_URL) VALUES(%s,%s,%s,%s,%s,%s,%s)",
                        (self.apartment_Name, self.apartment_Location, self.apartment_Type, self.owner_Contact, self.apartment_Description, self.owner_Email, self.image_URL ))
            cnx.commit()
            cnx.close()
        except Exception as e:
            flash("Error while registering a new owner %s",)