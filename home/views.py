from django.shortcuts import render
from django.template.loader import render_to_string
from django.core.mail  import EmailMessage
from django.conf import settings
from .utils import *

# Create your views here.
def index(request):
    # if request.method == "POST":
    #     name = request.POST['name']
    #     email = request.POST['email']
    #     subject = request.POST['subject']
    #     message = request.POST['message']
    #     sendMessage(name,email,subject,message)
    return render(request,"index.html")

def cad2Detail(request):
    return render(request,"cad2Detail.html")

def cad1Detail(request):
    return render(request,"cad1Detail.html")
