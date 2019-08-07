from google.appengine.ext import ndb

class User_Profile(ndb.Model):
    pet_name = ndb.StringProperty(required=True)
    a_type = ndb.StringProperty(required=False)
    p_pic = ndb.StringProperty(required=False)
    location = ndb.StringProperty(required=False)
    contact_info = ndb.StringProperty(required=True)
    bio = ndb.TextProperty(required=True)
    
    def get_propic_url(self):
        if self.img_choice == 'dog':
            url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQpXf5XHQ9kgHbMrm0UDsGfdnLpY0eCImg8NsbLrEPBemBjHXR-pg'
        elif self.img_choice == 'cat':
            url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTX2GdKFh11u7YQKsF9zrFqO1XqiLPkE9sGhGWWZEEs5hBjlXwb'
        elif self.img_choice == 'bird':
            url = 'https://s3.amazonaws.com/iconbros/icons/icon_pngs/000/000/647/original/bird.png?1512755589'
        elif self.img_choice == 'small_pet':
            url = 'https://png.pngtree.com/svg/20161120/b19f2ce58b.svg'
        elif self.img_choice == 'reptile':
            url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTAQEBUeSIahIzR0ojOYIQPWSu0gfKiBPqh0HOeJuyjZP2U2df2Og'
        return url