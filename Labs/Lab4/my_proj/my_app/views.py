from django.views import View
from django.shortcuts import render, redirect
from . import my_functions,my_objects


def title_names(the_name:str):
    #new_names 
    return the_name.lower()



class HomePageView(View):
    def get(self, request):

        my_name = "MATT!"

        new_name = title_names(my_name)

        the_names = ["MATT", "LOUIS", "MATT"]

        new_names = [ x.title() for x in the_names ]

        car1 = my_objects.car('green', 'honk honk')
        car2 = my_objects.car('blue','beep beep')








        the_names.append("TIM")

        other_names = the_names

        the_context = {'hi':'hello CLASS!',
                       'name':new_name,
                       'names_list':other_names,
                       'car1':car1,
                       'car2':car2
                       }
     
        return render(request, 'my_app/index.html', the_context)