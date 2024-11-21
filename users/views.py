from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.conf import settings
from users.models import OAuthCredential
from users.forms import OAuthCredentialForm
from django.contrib.sites.models import Site
from django.contrib import messages
from users.helpers import set_site_id, send_invite_email
from allauth.socialaccount.models import SocialApp
# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return redirect('/tasks/')
    return render(request, "users/index.html")

def admin_view(request):
    if request.method == "POST":
        pass
    oauth_credentials = OAuthCredential.objects.all().order_by("-created_at")
    context = { 
        "oauth_credentials" : oauth_credentials
    }
    return render(request, "users/admin_page.html", context=context)

def addedit_credential(request, id = None):
    try:
        credential = OAuthCredential.objects.get(id = id)
        form = OAuthCredentialForm(instance = credential)
    except Exception as e:
        form = OAuthCredentialForm()

    if request.method == "POST":
        form = OAuthCredentialForm(data = request.POST, instance = credential if id else None)
        if form.is_valid():
            form.save()
            msg = "OAuth Credentials Edited Successfully" if id else "New OAuth Credentials Created Successfully" 
            messages.success(request, msg)

            if id is not None and OAuthCredential.objects.get(id = id).is_default :
                return redirect(f'/adminpanel/change/{id}')
        else:
            context ={
                "form" : form
            }
            return render(request, "users/addedit_cred.html", context=context)
        return redirect("/adminpanel/")
    context ={
        "form" : form
    }
    return render(request, "users/addedit_cred.html", context=context)


def change_credential(request, id):
    credential = OAuthCredential.objects.get(id = id)

    OAuthCredential.objects.all().update(is_default = False)
    credential.is_default = True
    credential.save()

    status = set_site_id(credential.domain_name)
    if status:
        messages.success(request, "OAuth Credentials for Project changed Successfully")
    else:
        messages.error(request, "OAuth Credentials Can't be Set")

    return redirect("/adminpanel/")

def delete_credential(request, id):
    credential = OAuthCredential.objects.get(id = id)

    if credential.is_default:
        messages.success(request, "OAuth Credential can't be Deleted Because this is in use")
    else:
        site = Site.objects.get(domain = credential.domain_name)
        socialapp = SocialApp.objects.get(sites = site)

        socialapp.delete()
        site.delete()
        credential.delete()

        messages.success(request, "OAuth Credential is Deleted Successfully")
    return redirect("/adminpanel/")


def invite_users(request):
    if request.method == "POST":
        email_to = request.POST.get("email")
        send_invite_email(email_to)
        messages.success(request, "Email Sent Successfully")
        return redirect("/adminpanel/")
    return render(request, "users/invite_users.html")


def logout_view(request):
    logout(request)
    return redirect('/')