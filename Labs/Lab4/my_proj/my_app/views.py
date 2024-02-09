from django.views import View
from django.shortcuts import render, redirect
from . import my_functions, my_objects

#create a function / returning a value
#step 1
def fix_name(name:str):
    new_name = name.title()
    return new_name

#step 2 
class HomePageView(View):
    def get(self, request):

        orig_name = "ASHLEy!"
        name = fix_name(orig_name)

        # Returning a list step 1
        names = ["aSHLEY", "kARLEE", "jORDAN"]
        #step 2 - include code from other files - fix names
        fixed_names = my_functions.fix_names_list(names)

        #initiating an object
        car1 = my_objects.Car('Nissan Kicks','SV','2020', color ='green',sound ='honk honk')
        car2 = my_objects.Car('Toyota','Truck','1998',color ='blue',sound ='beep beep')
        motorcycle1 = my_objects.motorcyle('BMW','speed','2024',color ='red',sound ='VROOOM!')
        
        #step 3
        #dictionary
        #passing data from View to Template
        the_context = {'hi':'hello CLASS!',
                       'name':name,
                       'orig_name':orig_name,
                       'names':names,
                       'fixed_names': fixed_names,
                       'car1':car1,
                       'car2':car2,
                       'motorcycle1': motorcycle1,
                       }
     

        return render(request, 'my_app/index.html',
                       the_context)
    


     #new_names = [ x.title() for x in the_names ]
        #the_names.append("TIM")
        #other_names = the_names