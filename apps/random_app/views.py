from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string 
def index(request):
    return render(request,'random_app/index.html')

# Create your views here.
# @app.route('/random_word')
def random(request):
    if 'count' in request.session:
	    request.session['count'] += 1
    else:
        request.session['count'] = 1
    request.session['word'] = get_random_string(length = 10)
    return redirect('/')

def clear(request):
    request.session.flush()
    return redirect('/')