from django.shortcuts import render_to_response
from django.core.context_processors import csrf

from pygithub3 import Github
from pygithub3.services.repos import Commits


def login(request):

    if request.method == 'GET':
        c = {}
        c.update(csrf(request))
        return render_to_response('login.html', c)
        
    if request.method == 'POST':
    
        gh = Github(login=request.POST['username'], password=request.POST['password'])
        print request.POST['username']
        print gh
        
        user = gh.users.get()
        print user
        
        
        user_repos = gh.repos.list().all()
        print user_repos
        
        c = {'user_repos':user_repos, 'user_name':request.POST['username']}
        
        return render_to_response('home.html', c)

