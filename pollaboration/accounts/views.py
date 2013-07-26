from accounts.models import MyUser
from facepy import GraphAPI
from questions.models import Question, Answer, Vote
from questions.forms import *
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
from django.db.models import Q, Count
from django.forms.models import inlineformset_factory


def registration(request):
    years = [y for y in range(date.today().year-80,date.today().year-10)]
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
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
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
    current_question = Question.objects.all().order_by('?')[:1].get()
    return redirect(current_question)


@login_required
def submit(request):    
    AnswerInlineFormSet = inlineformset_factory(Question, Answer, form=AnswerForm, formset=AnswerFormSet, extra=5, can_delete=False)
    if request.method == 'POST':
        questionForm = QuestionForm(request.POST)
        if questionForm.is_valid():
            new_question = questionForm.save()
            answerInlineFormSet = AnswerInlineFormSet(request.POST, request.FILES, instance=new_question)
            print "non form errors %s" %answerInlineFormSet.non_form_errors()
            print "form errors %s" %answerInlineFormSet.errors
            if answerInlineFormSet.is_valid():
                print "Valid"
                answerInlineFormSet.save()
                return redirect(new_question)
    else:
        answerInlineFormSet = AnswerInlineFormSet()
        questionForm = QuestionForm()
    return render_to_response('submit.html', {"answerInlineFormSet":answerInlineFormSet, "questionForm":questionForm,}, context_instance=RequestContext(request))


@login_required
def profile(request):
    user = request.user
    grid_data = []
    for q in user.questions_answered.all():
        #### IN REAL LIFE, this is supposed to return only 1 answer choice.
        #### Since we have repeats enabled for testing purposes, this also has to be modified.
        #### For testing I am being lazy and just grabbing the first choice returnede
        a = user.answer_selections.filter(question_id=q.id)[0]
        #### Real life version uses .get(), which bombs if there's more than 1 item
        #### a = user.answer_selections.get(question_id=q.id)
        answerlist = list(q.answers.values("id","answer").annotate(value=Count("votes")))
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


# SCRAPPED!
@login_required
def connect_facebook_account(request):
    access_token = request.GET.get("access_token")
    fb_email = GraphAPI(access_token).get('me/')["email"]
    user = request.user
    user.fb_access_token = access_token
    user.populate_graph_info()
    user.save()
    return redirect(profile)


def facebook_login_success(request):
    access_token = request.GET.get("access_token")
    graphinfo = GraphAPI(access_token).get('me/')
    fb_id = graphinfo["id"]
    fb_email = graphinfo["email"]
    fb_gender = graphinfo["gender"]
    if request.user.is_authenticated():
        user = request.user
        user.fb_access_token = access_token
    else:
        try:
            user = MyUser.objects.get(email=fb_email)
            print "yes"
        except:
            user = MyUser.objects.create_user(email=fb_email, gender=fb_gender)
        user.backend = 'django.contrib.auth.backends.ModelBackend'
    user.fb_access_token=access_token
    print "ok"
    user.populate_graph_info()
    user.save()
    login(request, user)
    current_question = Question.objects.all().order_by('?')[:1].get()
    return redirect(current_question)