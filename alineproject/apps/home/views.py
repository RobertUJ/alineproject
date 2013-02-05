from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.mail import EmailMultiAlternatives # Para enviar HTML
from django.http import HttpResponseRedirect



def home(request):
	return render_to_response("home/index.html",context_instance=RequestContext(request)) 
