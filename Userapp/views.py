from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Reg,Dashboard
from .forms import Regform,Loginform,Taskform

class Home(View):
    def get(self,request):
        return render(request,"home.html")
class RegInput(View):
    def get(self,request):
        con_dic={'regform':Regform()}
        return render(request,'reginput.html', context=con_dic)
class LoginInput(View):
    def get(self, request):
        con_dic = {'loginform': Loginform()}
        return render(request,'logininput.html', context = con_dic)
class Regview(View):
    def post(self,request):
        rf = Regform(request.POST)
        if rf.is_valid():
            r1=Reg(FirstName=rf.cleaned_data["FirstName"],
                   LastName=rf.cleaned_data["LastName"],
                   UserName=rf.cleaned_data["UserName"],
                   Password=rf.cleaned_data["Password"],
                   CPassword=rf.cleaned_data["CPassword"],
                   EmailId=rf.cleaned_data["EmailId"],
                   MobileNumber=rf.cleaned_data["MobileNumber"])
            r1.save()
        return HttpResponse("registration completed successfully")
class Loginview(View):
    def post(self,request):
        lf=Loginform(request.POST)
        if lf.is_valid():
            res=Reg.objects.filter(UserName=lf.cleaned_data["UserName"],
                                   Password=lf.cleaned_data["Password"])
            if res:
                return render(request,"user.html")
            else:
                return HttpResponse('User name or password incorrect')


def create_view(request):
    context = {}
    form = Taskform(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "create_view.html", context)


def list_view(request):
    context = {}
    context["dataset"] = Dashboard.objects.all()
    return render(request, "list_view.html", context)


def detail_view(request, id):
    context = {}
    context["data"] = Dashboard.objects.get(id=id)

    return render(request, "detail_view.html", context)

def update_view(request, id):
    context = {}
    obj =object.get(Dashboard, id = id)
    form = Taskform(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponse("/" + id)

    # add form dictionary to context
    context["form"] = form

    return render(request, "update_view.html", context)


def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = object.get(Dashboard, id = id)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponse("/")

    return render(request, "delete_view.html", context)


