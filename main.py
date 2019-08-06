import webapp2
import jinja2
import os
from models import User_Profile

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
def run_query(prof_pic, name, animal, loc, contact, bio_):
    animal_prof = User_Profile(profile_pic = prof_pic,pet_name = name,animal_type = animal,location = loc, contact_info = contact, bio = bio_)
    prof_key = animal_prof.put()
    
class UserProfileHandler(webapp2.RequestHandler):
    def get(self):
   
        signup_template = the_jinja_env.get_template('templates/sign_up.html')
        self.response.write(signup_template.render())


app = webapp2.WSGIApplication([
    ('/signup', UserProfileHandler )
    
    
    ], debug=True)