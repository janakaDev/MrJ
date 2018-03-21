from django.http import HttpResponse
from django.template import loader
import Pyro4
    

def index(request):
	p = Pyro4.Proxy("PYRO:ch.x@localhost:3574")
	velo = p.response("i dont feel happy")
	template = loader.get_template('polls/index.html')
	context = {
        'velo': velo,
    }
	return HttpResponse(template.render(context, request))