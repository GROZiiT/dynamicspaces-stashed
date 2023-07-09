from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .models import *
from cryptography.fernet import Fernet
import random
import datetime
import requests
from django import template

register = template.Library()
client_id = 'AZbjl24UxpurpCWivsPxyAYCbHNkoTgoPxMcHXp0vlEWItKQ_s1PY9YTAXqk540STaqwzKrzihlMCnw0'
client_key = 'EDXoiu_RvG2otCBFGTHbfM2z08LnGLzEKGFpFQt22HpS2RWG1ADutj9PIJ-xCWnrBe-ynERD_stCPAP_'

def get_access_token():
    data = {
        'grant_type': 'client_credentials',
    }

    response = requests.post('https://api-m.sandbox.paypal.com/v1/oauth2/token', data=data, auth=(
        client_id,client_key))
    return response.json()["access_token"]

def payment(request):
    if not logged_in(request):
        return HttpResponseRedirect('pages-login')
    try:
        user = Profiles.objects.get(email=request.session['email'])
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + get_access_token(),
        }
        print("Hiiiiiiiii", request.POST['subscriptionID'])
        subscriptions_response = requests.get(
            'https://api-m.sandbox.paypal.com/v1/billing/subscriptions/' + request.POST['subscriptionID'],
            headers=headers)

        print("rggdf",request.POST['subscriptionID'])
        user.subscriber_id = request.POST['subscriptionID']
        user.subscriber = True
        user.save()

        request.session['message'] = 'Payment Successful..!'
        return HttpResponseRedirect("users-profile")

    except Exception as e:
        request.session['message'] = 'Payment Unsuccessful..!Please contact admin or try again.'
        return HttpResponseRedirect("users-profile")

@register.simple_tag
def split(string):
    return string.split()

def logged_in(request):
    try:
        profile = Profiles.objects.get(email=request.session['email'])
        fernet = Fernet(profile.key.encode('utf-8'))
        if(profile.password == fernet.decrypt(request.session['password']).decode()):
            return True
    except Exception as e:
        print(e)
        return False

def register(request):
    try:
        profile = Profiles()
        profile.name= request.POST['name']
        profile.email = request.POST['email']
        profile.username = request.POST['username']
        profile.password = request.POST['password']
        profile.job = request.POST['job']
        profile.name = request.POST['name']
        profile.key = Fernet.generate_key().decode('utf-8')
        profile.save()
        return HttpResponseRedirect('pages-login')
    except Exception as e:
        print(e)
        return render(request, "pages-register.html")

def login(request):
    try:
        profile = Profiles.objects.get(email=request.POST['email'])
        if(profile.password == request.POST['password']):
            request.session['email']= profile.email
            fernet = Fernet(profile.key.encode('utf-8'))
            request.session['password'] = fernet.encrypt(profile.password.encode()).decode('utf-8')
            return HttpResponseRedirect('index')
        else:
            raise Exception
    except Exception as e:
        print(e)
        request.session['message'] = "The Username or password is incorret, please try again"
        return HttpResponseRedirect('pages-login')

def logout(request):
    try:
        request.session.flush()
    except:
        pass
    return HttpResponseRedirect('pages-login')

def handler404(request, exception):
    return render(request, 'pages-error-404.html', status=404)


def handler500(request):
    return render(request, 'pages-error-404.html', status=500)


def index(request):
    if not logged_in(request):
        return HttpResponseRedirect('pages-login')

    jobs=Jobs.objects.filter(posted_by=request.session['email'])
    return render(request, "index.html",{'jobs':jobs})

def add_post(request):
    if not logged_in(request):
        return HttpResponseRedirect('pages-login')
    return render(request, "add-post.html")

def adding_job(request):
    if not logged_in(request):
        return HttpResponseRedirect('pages-login')
    try:
        job =Jobs()
        job.title=request.POST['title']
        job.sdescription = request.POST['sdescription']
        job.description = request.POST['description']
        job.location = request.POST['location']
        job.eemail = request.POST['eemail']
        job.company = request.POST['company']
        job.logo_img_url = request.POST['logo_img_url']
        job.expire_in_days = request.POST['expire_in_days']
        job.background_img_url = request.POST['background_img_url']
        job.keywords = request.POST['keywords']
        job.posted_by= request.session['email']
        job.save()
        return HttpResponseRedirect('index')
    except Exception as e:
        print(e)
        return HttpResponseRedirect('add-post')


def GroziitDynamicSpace(request):
    if not logged_in(request):
        return HttpResponseRedirect('pages-login')
    jobs = Jobs.objects.filter(posted_by=request.session['email'])
    return render(request, "GroziitJobs.html",{'jobs':jobs})

def postdetail(request):
    if not logged_in(request):
        return HttpResponseRedirect('pages-login')
    job = Jobs.objects.get(id=request.GET['job'],posted_by=request.session['email'])
    # job.time = tim
    return render(request, "detail.html",{"job":job})

def charts_apexcharts(request):
    return render(request, "charts-apexcharts.html")


def charts_chartjs(request):
    return render(request, "charts-chartjs.html")


def charts_echarts(request):
    return render(request, "charts-echarts.html")


def components_accordion(request):
    return render(request, "components-accordion.html")


def components_alerts(request):
    return render(request, "components-alerts.html")


def components_badges(request):
    return render(request, "components-badges.html")


def components_breadcrumbs(request):
    return render(request, "components-breadcrumbs.html")


def components_buttons(request):
    return render(request, "components-buttons.html")


def components_cards(request):
    return render(request, "components-cards.html")


def components_carousel(request):
    return render(request, "components-carousel.html")


def components_list_group(request):
    return render(request, "components-list-group.html")


def components_modal(request):
    return render(request, "components-modal.html")


def components_pagination(request):
    return render(request, "components-pagination.html")


def components_progress(request):
    return render(request, "components-progress.html")


def components_spinners(request):
    return render(request, "components-spinners.html")


def components_tabs(request):
    return render(request, "components-tabs.html")


def components_tooltips(request):
    return render(request, "components-tooltips.html")


def forms_editors(request):
    return render(request, "forms-editors.html")


def forms_elements(request):
    return render(request, "forms-elements.html")


def forms_layouts(request):
    return render(request, "forms-layouts.html")


def forms_validation(request):
    return render(request, "forms-validation.html")


def icons_bootstrap(request):
    return render(request, "icons-bootstrap.html")


def icons_boxicons(request):
    return render(request, "icons-boxicons.html")


def icons_remix(request):
    return render(request, "icons-remix.html")


def pages_blank(request):
    return render(request, "pages-blank.html")


def pages_contact(request):
    return render(request, "pages-contact.html")


def pages_faq(request):
    return render(request, "pages-faq.html")


def pages_login(request):
    try:
        if request.session["message"]!="":
            message= request.session["message"]
            request.session["message"] = ""
            return render(request, "pages-login.html", {"message":message})
    except:
        pass
    return render(request, "pages-login.html")


def pages_register(request):
    return render(request, "pages-register.html")


def tables_data(request):
    return render(request, "tables-data.html")


def tables_general(request):
    return render(request, "tables-general.html")


def users_profile(request):
    if not logged_in(request):
        return HttpResponseRedirect('pages-login')

    if "message" not in request.session.keys():
        request.session["message"]=""
    msg,request.session["message"]=request.session["message"],""
    return render(request, "users-profile.html",{"msg":msg,"profile":Profiles.objects.get(email=request.session['email'])})

def cancelsub(request):
    if not logged_in(request):
        return HttpResponseRedirect('pages-login')
    try:
        user = Profiles.objects.get(username=request.session['email'])

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + get_access_token(),
        }

        json_data = {
            'reason': 'NA',
        }

        response = requests.post(
            'https://api-m.sandbox.paypal.com/v1/billing/subscriptions/' + user.subscriber_id + '/cancel',
            headers=headers,
            json=json_data,
        )

        if response.status_code != 204:
            raise Exception

        user.subscriber = False
        user.subscriber_id = ""
        user.save()

        request.session['message'] = 'Successfully cancelled Subscription'
        return HttpResponseRedirect("users-profile")

    except Exception as e:
        request.session['message'] = 'There is an error cancelling the Subscription, please try again or Contact us'
        return HttpResponseRedirect("users-profile")