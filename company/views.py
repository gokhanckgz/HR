from django.contrib.postgres.search import SearchVector
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.http import *
from usermanage.models import User
from usermanage.forms import UserCreateForm
from .tables import *
from . import models
from .forms import ProfileEditForm, ServiceUseForm


def index(request):
    if not request.user.user_type == 'Company':
        return HttpResponseForbidden('Nope U\'re not COMPANY!')
    company = models.Company.objects.get(user_id=request.user.id)
    employes = Employe.objects.filter(company_id=company.id).all()
    benefits = models.Benefit.objects.filter(employe_id__in=employes.values("id")).all()
    services = Service.objects.all()
    choosen_services = models.Company_Service.objects.filter(company_id=company.id).all()
    used_services = Service.objects.filter(id__in=choosen_services.values("service_id"))
    return render(request, 'company/index.html', locals())


def profile(request):
    company = models.Company.objects.get(user_id=request.user.id)
    form = ProfileEditForm(instance=company)
    if request.method == 'POST':
        if request.user.id:
            form = ProfileEditForm(request.POST, request.FILES, instance=company)
        else:
            form = ProfileEditForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/company', locals())
    return render(request, 'company/profile.html', locals(), RequestContext(request))


def employes(request):
    company = models.Company.objects.get(user_id=request.user.id)
    data = Employe.objects.filter(company_id=company.id).all()
    if request.GET:
        search_value = request.GET.get('q')
        data = Employe.objects.annotate(search=SearchVector('name', 'surname', 'phone_number'), ).filter(
            search=search_value)
    return render(request, 'company/employes.html', locals())


def employe_info(request, pk):
    company = models.Company.objects.get(user_id=request.user.id)
    employe = Employe.objects.get(id=pk)
    bnf = models.Benefit.objects.filter(employe_id=employe.id).all()
    services = Service.objects.filter(id__in=bnf.values("service_id")).all()
    return render(request, 'company/employe_info.html', locals(), RequestContext(request))


def emp_add(request):
    form = UserCreateForm()
    if request.method == 'POST':
        form = UserCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(company_user_id=request.user.id)
            return redirect('/company/employes', locals())
    return render(request, 'company/emp_add.html', locals(), RequestContext(request))


def emp_edit(request, pk):
    employe = Employe.objects.get(id=pk)
    form = ProfileEditForm(instance=employe)
    if request.method == 'POST':
        if pk:
            form = ProfileEditForm(request.POST, request.FILES, instance=employe)
        else:
            form = ProfileEditForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/company/employes', locals())
    return render(request, 'company/emp_add.html', locals(), RequestContext(request))


def emp_delete(request, pk):
    User.objects.filter(id=pk).delete()
    Employe.objects.filter(id=pk).delete()
    return redirect('/company/employes', locals())


def services(request):
    company = models.Company.objects.get(user_id=request.user.id)
    choosen_services = models.Company_Service.objects.filter(company_id=company.id).all()
    used_services = Service.objects.filter(id__in=choosen_services.values("service_id"))
    data = Service.objects.all()
    if request.GET:
        search_value = request.GET.get('q')
        data = Service.objects.annotate(search=SearchVector('name'), ).filter(search=search_value)
    return render(request, 'company/services.html', locals(), RequestContext(request))

def service_info(request, pk):
    company = models.Company.objects.get(user_id=request.user.id)
    service = Service.objects.get(id=pk)
    return render(request, 'company/service_info.html', locals(), RequestContext(request))

def service_choose(request, pk):
    company = models.Company.objects.get(user_id=request.user.id)
    benefit = models.Company_Service(company_id=company.id, service_id=pk)
    benefit.save()
    return redirect('/company/services', locals())


def service_delete(request, pk):
    company = models.Company.objects.get(user_id=request.user.id)
    benefit = models.Company_Service.objects.get(company_id=company.id, service_id=pk)
    benefit.delete()
    return redirect('/company/services', locals())


def employe_service_use(request, pk):
    company = models.Company.objects.get(user_id=request.user.id)
    employe = Employe.objects.get(id=pk)
    form = ServiceUseForm()
    choosen_services = models.Company_Service.objects.filter(company_id=company.id).all()
    if request.method == 'POST':
        form = ServiceUseForm(request.POST, request.FILES)
        form.fields["supplier_service"].queryset = Service.objects.filter(
            id__in=choosen_services.values(("service_id")))
        if form.is_valid():
            form.save(employe_id=employe.id)
            return redirect('company_employe_info', employe.id)
    return render(request, 'company/employe_info.html', locals(), RequestContext(request))


def employe_service_delete(request, pk, pk2):
    employe = Employe.objects.get(id=pk)
    benefit = models.Benefit.objects.get(employe_id=employe.id, supplier_service_id=pk2)
    benefit.delete()
    return redirect('company_employe_info', employe.id)
