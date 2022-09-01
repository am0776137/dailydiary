from cgitb import reset
import re
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

# diary_data = [
#     {
#         'author':'Abdullah',
#         'title':'My First Day',
#         'content':'    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
#         'date_posted':'August, 15, 2022'
#     },
#     {
#         'author':'Abdullah',
#         'title':'My Second Day',
#         'content':'    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
#         'date_posted':'August, 16, 2022'
#     },
# ]

def home(request):
    """
        This view renders and returns the homepage of the logged-in user
    """
    
    # context = {
    #     'posts':diary_data
    # }
    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'diary/home.html', context=context)

