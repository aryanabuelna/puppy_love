import webapp2
import jinja2
import os
from models import User_Profile

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
def run_query(prof_pic, name, animal, loc, contact, bio_):
    animal_prof = User_Profile(pet_name = name,animal_type = animal,location = loc, contact_info = contact, bio = bio_)
    prof_key = animal_prof.put()
    
class HomePageHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('please work!')
        # home_page = the_jinja_env.get_template('templates/home.html')
        # self.response.write(home_page)
        
class UserProfileHandler(webapp2.RequestHandler):
    def get(self):
       signup_template = the_jinja_env.get_template('templates/sign_up.html')
        
    #   pro_pic = self.request.get('profile_pic')
       animal_name = self.request.get('user_pet_name')
       a_type = self.request.get('animal-type')
       location = self.request.get('state_location')
       c_info = self.request.get('user_contact_info')
       a_bio = self.request.get('user_bio')
    
    #   run_query(pro_pic, animal_name, a_type, location, c_info, a_bio)
       
       signup_template = the_jinja_env.get_template('templates/sign_up.html')
       self.response.write(signup_template.render())


app = webapp2.WSGIApplication([
    ('/', HomePageHandler),
    ('/signup', UserProfileHandler ),
    ('/results'), 
    
], debug=True)