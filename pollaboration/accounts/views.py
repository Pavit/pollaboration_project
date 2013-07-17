from accounts.models import MyUser
from facepy import GraphAPI
from questions.models import Question, Answer, Vote
from django.contrib.auth.decorators import login_required
from django.http import *
from django.shortcuts import render_to_response,redirect,render
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django import forms
from accounts.admin import UserCreationForm
from datetime import date
from django.core.urlresolvers import reverse

def registration(request):
    years = [y for y in range(date.today().year-80,date.today().year-10)]
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print form.errors
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password1'])
            login(request, new_user)
            current_question = Question.objects.all().order_by('?')[:1].get()
            return redirect(current_question)
    else:
        form = UserCreationForm()
    return render(request, "registration.html", {'form': form, 'years':years})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('questions.views.index'))

def login_view(request):
    logout(request)
    email = password = ''
    if request.method == 'POST':
        print request.POST.get('email')
        print request.POST.get('password')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        print user
        if user is not None:
            if user.is_active:
                login(request, user)
                print request.user.is_authenticated()
    current_question = Question.objects.all().order_by('?')[:1].get()
    return redirect(current_question)


def facebook_login_success(request):
    access_token = request.GET.get("access_token")
    fb_id = GraphAPI(access_token).get('me/')["id"]
    try:
        user = User.objects.get(username=fb_id)
        print "got use"
    except:
        user = User.objects.create_user(fb_id)
    user.userprofile.fb_access_token=access_token
    print "ok"
    user.userprofile.populate_graph_info()
    user.save()
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    login(request, user)
    print user.userprofile
    current_question = Question.objects.all().order_by('?')[:1].get()
    return HttpResponseRedirect(reverse('questions.views.current_question', args=(current_question.id,)))

@login_required
def profile(request):
    user = request.user.userprofile
    grid_data = []
    for q in user.answered.all():
        #### IN REAL LIFE, this is supposed to return only 1 answer choice.
        #### Since we have repeats enabled for testing purposes, this also has to be modified.
        #### For testing I am being lazy and just grabbing the first choice returnede
        a = user.selections.filter(question_id=q.id)[0]
        #### Real life version uses .get(), which bombs if there's more than 1 item
        #### a = user.selections.get(question_id=q.id)
        answerlist = list(q.answer_set.values("id","answer").annotate(value=Count("votes")))
        for item in answerlist:
            item["label"] = item.pop("answer")
        grid_data.append({
            'question': q.question,
            'answers': answerlist,
            'chosen': a.id,
            })
    context = {
        'grid_data':grid_data,
    }
    return render_to_response("profile.html", context, context_instance = RequestContext(request))