from django.shortcuts import render,get_object_or_404
from django.conf import settings
from chp.models import Complain
from chp.forms import *
from users.forms import *
from users.models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.views.generic import TemplateView,ListView,UpdateView
from .charts import DeptComplainBarChart,ResidenceComplainPieChart,StatusComplainBarChart
from pygal.style import CleanStyle
from django.contrib.auth.models import User
from django.contrib.auth.mixins import UserPassesTestMixin



class IndexBarView(TemplateView):
  
  def get_context_data(self, **kwargs):
    context = super(IndexBarView, self).get_context_data(**kwargs)

        # Instantiate our chart. We'll keep the size/style/etc.
        # config here in the view instead of `charts.py`.
    cht_complain = DeptComplainBarChart(
      height=600,
      width=600,
      explicit_size=True,
      style=CleanStyle
      )

        # Call the `.generate()` method on our chart object
        # and pass it to template context.
    context['cht_complain'] = cht_complain.generate()
    return context



class IndexPieView(TemplateView):
  
  def get_context_data(self, **kwargs):
    context = super(IndexPieView, self).get_context_data(**kwargs)

        # Instantiate our chart. We'll keep the size/style/etc.
        # config here in the view instead of `charts.py`.
    Piecht_complain = ResidenceComplainPieChart(
      height=700,
      width=700,
      explicit_size=True,
      style=CleanStyle
      )

        # Call the `.generate()` method on our chart object
        # and pass it to template context.
    context['Piecht_complain'] = Piecht_complain.generate()
    return context

class IndexStatusBarView(TemplateView):
  
  def get_context_data(self, **kwargs):
    context = super(IndexStatusBarView, self).get_context_data(**kwargs)

        # Instantiate our chart. We'll keep the size/style/etc.
        # config here in the view instead of `charts.py`.
    Scht_complain = StatusComplainBarChart(
      height=600,
      width=600,
      explicit_size=True,
      style=CleanStyle
      )

        # Call the `.generate()` method on our chart object
        # and pass it to template context.
    context['Scht_complain'] = Scht_complain.generate()
    return context


def homepage(request):
	return render(request,'chp/homepage.html')


def about(request):
	return render(request,'chp/about.html')

def dept(request):
	return render(request,'chp/dept.html')

@login_required
def Acomplain(request):
    if request.method == 'POST':
        c_form = Acomplainform(request.POST)
        if c_form.is_valid():
          subject = c_form.cleaned_data['complain_subject']
          message = c_form.cleaned_data['complain_description']
          sender = settings.EMAIL_HOST_USER
          recepient = c_form.cleaned_data['recepient']
          cuser = Complain.objects.get('complain_user').filter(recepient = recepient)
          to = []
          to.append(recepient)
          user = c_form.cleaned_data['complain_user']
          if (request.user == cuser):
            return HttpResponse("user can not log complain to his own department")
          elif (request.user == user):
            c_form.save();
          else:
            return HttpResponse("user is not logged in ")
          send_mail(subject, message, sender, to)
          return HttpResponseRedirect('thank')

    else:
        c_form = Acomplainform()
        context = {
        	'c_form': c_form
    		}
        return render(request, 'chp/complain.html', context)


@login_required
def Adcomplain(request):
    if request.method == 'POST':
        c_form = Adcomplainform(request.POST)
        if c_form.is_valid():
          subject = c_form.cleaned_data['complain_subject']
          message = c_form.cleaned_data['complain_description']
          sender = settings.EMAIL_HOST_USER
          recepient = c_form.cleaned_data['recepient']
          to = []
          to.append(recepient)
          user = c_form.cleaned_data['complain_user']
          if (request.user == user):
            c_form.save();
          else:
            return HttpResponse("user is not logged in")
          c_form.save()
          send_mail(subject, message, sender, to)
          return HttpResponseRedirect('thank')

    else:
        c_form = Adcomplainform()
        context = {
          'c_form': c_form
        }
        return render(request, 'chp/complain.html', context)

@login_required
def Ccomplain(request):
    if request.method == 'POST':
        c_form = Ccomplainform(request.POST)
        if c_form.is_valid():
          subject = c_form.cleaned_data['complain_subject']
          message = c_form.cleaned_data['complain_description']
          sender = settings.EMAIL_HOST_USER
          recepient = c_form.cleaned_data['recepient']
          to = []
          to.append(recepient)
          user = c_form.cleaned_data['complain_user']
          if (request.user == user):
            c_form.save();
          else:
            return HttpResponse("user is not logged in")
          send_mail(subject, message, sender, to)
          return HttpResponseRedirect('thank')

    else:
        c_form = Ccomplainform()
        context = {
          'c_form': c_form
        }
        return render(request, 'chp/complain.html', context)

@login_required
def Ecomplain(request):
    if request.method == 'POST':
        c_form = Ecomplainform(request.POST)
        if c_form.is_valid():
          subject = c_form.cleaned_data['complain_subject']
          message = c_form.cleaned_data['complain_description']
          sender = settings.EMAIL_HOST_USER
          recepient = c_form.cleaned_data['recepient']
          to = []
          to.append(recepient)
          user = c_form.cleaned_data['complain_user']
          if (request.user == user):
            c_form.save();
          else:
            return HttpResponse("user is not logged in")
          c_form.save()
          send_mail(subject, message, sender, to)
          return HttpResponseRedirect('thank')

    else:
        c_form = Ecomplainform()
        context = {
          'c_form': c_form
        }
        return render(request, 'chp/complain.html', context)

@login_required
def Mcomplain(request):
    if request.method == 'POST':
        c_form = Mcomplainform(request.POST)
        if c_form.is_valid():
          subject = c_form.cleaned_data['complain_subject']
          message = c_form.cleaned_data['complain_description']
          sender = settings.EMAIL_HOST_USER
          recepient = c_form.cleaned_data['recepient']
          to = []
          to.append(recepient)
          user = c_form.cleaned_data['complain_user']
          if (request.user == user):
            c_form.save();
          else:
            return HttpResponse("user is not logged in")
          c_form.save()
          send_mail(subject, message, sender, to)
          return HttpResponseRedirect('thank')

    else:
        c_form = Mcomplainform()
        context = {
          'c_form': c_form
        }
        return render(request, 'chp/complain.html', context)

@login_required
def Scomplain(request):
    if request.method == 'POST':
        c_form = Scomplainform(request.POST)
        if c_form.is_valid():
          subject = c_form.cleaned_data['complain_subject']
          message = c_form.cleaned_data['complain_description']
          sender = settings.EMAIL_HOST_USER
          recepient = c_form.cleaned_data['recepient']
          to = []
          to.append(recepient)
          user = c_form.cleaned_data['complain_user']
          if (request.user == user):
            c_form.save();
          else:
            return HttpResponse("user is not logged in")
          c_form.save()
          send_mail(subject, message, sender, to)
          return HttpResponseRedirect('thank')

    else:
        c_form = Scomplainform()
        context = {
          'c_form': c_form
        }
        return render(request, 'chp/complain.html', context)

@login_required
def Rcomplain(request):
    if request.method == 'POST':
        c_form = Rcomplainform(request.POST)
        if c_form.is_valid():
          subject = c_form.cleaned_data['complain_subject']
          message = c_form.cleaned_data['complain_description']
          sender = settings.EMAIL_HOST_USER
          recepient = c_form.cleaned_data['recepient']
          to = []
          to.append(recepient)
          user = c_form.cleaned_data['complain_user']
          if (request.user == user):
            c_form.save();
          else:
            return HttpResponse("user is not logged in")
          c_form.save()
          send_mail(subject, message, sender, to)
          return HttpResponseRedirect('thank')

    else:
        c_form = Rcomplainform()
        context = {
          'c_form': c_form
        }
        return render(request, 'chp/complain.html', context)


def AdminComplainCheck(request):
    if request.method == 'POST':
       c_form = AdminComplainCheckForm(request.POST)
       if c_form.is_valid():
          status = c_form.cleaned_data['status']
          complain_department = c_form.cleaned_data['complain_department']
          q = Complain.objects.filter(status = status,complain_department = complain_department).order_by('date_posted')
          return render(request,'chp/checkallcomplain.html',{'q':q})
    else:
        c_form = AdminComplainCheckForm()
        context = {
        'c_form': c_form
        }
        return render(request, 'chp/searchcomplain.html', context)


def DeptComplainCheck(request):
  current_user = request.user
  email = current_user.email
  if request.method == 'POST':
      c_form = StaffComplainCheckForm(request.POST)
      if c_form.is_valid():
        status = c_form.cleaned_data['status']
        q = Complain.objects.filter(recepient = email,status = status).order_by('date_posted')
        return render(request,'chp/checkdeptcomplain.html',{'q':q})
  else:
      c_form = StaffComplainCheckForm()
      context = {
      'c_form': c_form
      }
      return render(request, 'chp/searchcomplain.html', context)


def UserComplainCheck(request):
  current_user = request.user
  if request.method == 'POST':
      c_form = UserComplainCheckForm(request.POST)
      if c_form.is_valid():
        status = c_form.cleaned_data['status']
        q = Complain.objects.filter(complain_user = current_user, status = status).order_by('date_posted')
        return render(request,'chp/checkyourcomplain.html',{'q':q})
  else:
      c_form = UserComplainCheckForm()
      context = {
      'c_form': c_form
      }
      return render(request, 'chp/searchcomplain.html', context)


class ComplainUpdateView(UserPassesTestMixin, UpdateView):
  model = Complain
  fields = ['status']
  success_url = '/'

  def form_valid(self, form):
    form.instance.complain_user != self.request.user
    return super().form_valid(form)

  def test_func(self):
    complain = self.get_object()
    if self.request.user != complain.complain_user:
      return True
    return False


def user_detail(request,username):
  #if request.user.username != username:
  u1 = User.objects.get(username = username),
  p1 = Profile.objects.filter(user__username = username)
  return render(request,'chp/detail.html',{'u1':u1,'p1':p1})

def thank(request):
	return render(request,'chp/thank.html')



#def chart(request):
 # queryset = Complain.objects.all()
 # data_source = ModelDataSource(queryset,fields=['Complain_User', 'ComplainDepartment'])
 # chart = gchart.LineChart(data_source)
  #context = {'chart' : chart}
 # return render_to_response('chp/chart.html',context)




