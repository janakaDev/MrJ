from django.http import HttpResponse
from django.template import loader
from django import http
import json
import Pyro4
    
global message
def index(request):
	template = loader.get_template('polls/index.html')
	#if request.method == 'POST':
		# message = request.POST.get['message']
	p = Pyro4.Proxy("PYRO:ch.x@localhost:2246")
	velo0 = p.response("hello")
	velo1 = p.response("i feel alone")
	velo2= p.response("what should i give my mother as a gift")
	context = {
        'velo': velo1,
		'velo2':velo2,
		'velo0':velo0,
		#'message':message,
    }
	return HttpResponse(template.render(context, request))

	


def mygetview(request):
    if request.method == 'GET':
        p = Pyro4.Proxy("PYRO:ch.x@localhost:2246")
        data = request.GET['mydata']
        velo0 = p.response(data)
        astr = velo0
        return HttpResponse(astr)
    return render(request)