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
        self.response.write('please work!')
        # home_page = the_jinja_env.get_template('templates/home.html')
        # self.response.write(home_page)
        
class UserProfileHandler(webapp2.RequestHandler):
    def get(self):
       
       signup_template = the_jinja_env.get_template('templates/sign_up.html')
       self.response.write(signup_template.render())

class ResultsHandler(webapp2.RequestHandler):
   
    def post(self):
       
        results_template = the_jinja_env.get_template('templates/results.html')
      
        animal_name = self.request.get('user_pet_name')
        c_info = self.request.get('user_contact_info')
        a_bio = self.request.get('user_bio')
        location = self.request.get('city_location')
        
        pic_type_choice = self.request.get('animal-type')
        if pic_type_choice == 'dog':
            pro_pic = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQpXf5XHQ9kgHbMrm0UDsGfdnLpY0eCImg8NsbLrEPBemBjHXR-pg'
        elif pic_type_choice == 'cat':
            pro_pic = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTX2GdKFh11u7YQKsF9zrFqO1XqiLPkE9sGhGWWZEEs5hBjlXwb'
        elif pic_type_choice == 'bird':
            pro_pic = 'https://s3.amazonaws.com/iconbros/icons/icon_pngs/000/000/647/original/bird.png?1512755589'
        elif pic_type_choice == 'small_pet':
            pro_pic = 'https://png.pngtree.com/svg/20161120/b19f2ce58b.svg'
        elif pic_type_choice == 'reptile':
            pro_pic = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTAQEBUeSIahIzR0ojOYIQPWSu0gfKiBPqh0HOeJuyjZP2U2df2Og'
            

        run_query(animal_name,pic_type_choice,pro_pic,location,c_info,a_bio)
            
        the_variable_dict = {
            "username": animal_name,
            "contacting": c_info,
            "_bio_": a_bio,
            "place": location,
            "t_o_animal": pic_type_choice,
            "img_pic": pro_pic,
        }
      
        self.response.write(results_template.render(the_variable_dict))
        
class AllProfilesHandler(webapp2.RequestHandler):
    def get(self):
        
        all_profiles_template = the_jinja_env.get_template('templates/all_profiles.html')
        
        all_profiles = User_Profile.query().fetch()
        
        the_variable_dict = {
            'all_pet_profiles': all_profiles
        }
        
        self.response.write(all_profiles_template.render(the_variable_dict))
        

app = webapp2.WSGIApplication([
    ('/', HomePageHandler),
    ('/signup', UserProfileHandler),
    ('/results', ResultsHandler),
    ('/search', AllProfilesHandler),
    
], debug=True)