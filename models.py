from google.appengine.ext import ndb

class User_Profile(ndb.Model):
    pet_name = ndb.StringProperty(required=True)
    animal_type = ndb.StringProperty(required=False)
    location = ndb.StringProperty(required=False)
    contact_info = ndb.StringProperty(required=True)
    bio = ndb.TextProperty(required=True)
    