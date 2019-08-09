import webapp2
import jinja2
import os
from models import User_Profile

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
    
def run_query(name, animal, pic, loc, contact, bio_):
    animal_prof = User_Profile(pet_name = name, a_type = animal, p_pic = pic, location = loc, contact_info = contact, bio = bio_)
    prof_key = animal_prof.put()
    
class HomePageHandler(webapp2.RequestHandler):
    def get(self):
        home_template = the_jinja_env.get_template('templates/home.html')
        self.response.write(home_template.render())
        
class AboutPageHandler(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/about.html')
        self.response.write(about_template.render())
        
class UserProfileHandler(webapp2.RequestHandler):
    def get(self):
       
       signup_template = the_jinja_env.get_template('templates/sign_up.html')
       self.response.write(signup_template.render())

class ResultsHandler(webapp2.RequestHandler):
   
    def post(self):
       
        results_template = the_jinja_env.get_template('templates/results.html')
      
        pet_name = self.request.get('user_pet_name')
        contact_info = self.request.get('user_contact_info')
        bio = self.request.get('user_bio')
        location = self.request.get('city_location')
        
        a_type = self.request.get('animal-type')
        if a_type == 'dog':
            p_pic = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQpXf5XHQ9kgHbMrm0UDsGfdnLpY0eCImg8NsbLrEPBemBjHXR-pg'
        elif a_type == 'cat':
            p_pic = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTX2GdKFh11u7YQKsF9zrFqO1XqiLPkE9sGhGWWZEEs5hBjlXwb'
        elif a_type == 'bird':
            p_pic = 'https://s3.amazonaws.com/iconbros/icons/icon_pngs/000/000/647/original/bird.png?1512755589'
        elif a_type == 'small_pet':
            p_pic = 'https://png.pngtree.com/svg/20161120/b19f2ce58b.svg'
        elif a_type == 'reptile':
            p_pic = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTAQEBUeSIahIzR0ojOYIQPWSu0gfKiBPqh0HOeJuyjZP2U2df2Og'
            

        run_query(pet_name,a_type,p_pic,location,contact_info,bio)
            
        the_variable_dict = {
            "username": pet_name,
            "contacting": contact_info,
            "_bio_": bio,
            "place": location,
            "t_o_animal": a_type,
            "img_pic": p_pic,
        }
      
        self.response.write(results_template.render(the_variable_dict))
        
class AllProfilesHandler(webapp2.RequestHandler):
    def get(self):
        
        all_profiles_template = the_jinja_env.get_template('templates/all_profiles.html')
        
        all_profiles = User_Profile.query().fetch()
        
        the_variable_dict = {
            'all_profiles': all_profiles
        }
        
        self.response.write(all_profiles_template.render(the_variable_dict))
        
def clear_userprofiles():
    
        all_profiles = User_Profile.query().fetch()
        
        for entity in all_profiles:
            entity.key.delete()
            
class ClearDBHandler(webapp2.RequestHandler):
    
    def get(self):
        clear_userprofiles()
        self.response.write("Database cleared.")

class SeedDBHandler(webapp2.RequestHandler):
    
    def get(self):
        run_query("fluffy","dog",'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQpXf5XHQ9kgHbMrm0UDsGfdnLpY0eCImg8NsbLrEPBemBjHXR-pg',"Salinas","1234567","blah blah blaqh")
        run_query("cat name","cat",'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTX2GdKFh11u7YQKsF9zrFqO1XqiLPkE9sGhGWWZEEs5hBjlXwb',"Salinas","56789","aieufefiusiefiheifsiehfih blah blaqh")
        
app = webapp2.WSGIApplication([
    ('/', HomePageHandler),
    ('/about', AboutPageHandler),
    ('/signup', UserProfileHandler),
    ('/results', ResultsHandler),
    ('/search', AllProfilesHandler),
    ('/cleardatabase', ClearDBHandler),
    ('/seeddatabase', SeedDBHandler)
    
], debug=True)