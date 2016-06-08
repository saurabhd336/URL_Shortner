from django.shortcuts import render
from django.http import HttpResponseRedirect
import random, string
from .models import Link

# TODO Add view all urls
# Create your views here.

def index(request):
	if request.method == "POST":
		status = False
		url = request.POST.get('url')
		shortner = ''.join(random.choice(string.uppercase + string.lowercase + string.digits) for i in range(5))
		new_link = Link(url = url, shortner = shortner)
		try :
			new_link.save()
			status = True
		except Exception, e:
			print e
			status = False
		return render(request, "final.html", {'status' : status, 'new_url' : "http://" + str(request.get_host()) + "/" + shortner})
	return render(request, "index.html")

def redirect(request, short):
	x = Link.objects.get(shortner = short)
	return HttpResponseRedirect(x.url)