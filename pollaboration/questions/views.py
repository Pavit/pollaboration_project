from django.conf import settings
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q, Count
from questions.models import *
from django.core.urlresolvers import reverse
from django.utils import simplejson
from django.forms.models import inlineformset_factory
import moment


def index(request):
    current_question = Question.objects.all().order_by('?')[:1].get()
    request.session["previous_question_id"]=None
    return HttpResponseRedirect(reverse('questions.views.current_question', args=(current_question.id,)))


def current_question(request, current_question_id):
    current_question = get_object_or_404(Question, pk=current_question_id)
    print request.META.get('HTTP_X_PJAX')   
    print request.user.is_authenticated()
    previous_question_id = request.session.get('previous_question_id', None)
    previous_question = None
    request.session["previous_question_id"]=None
    if previous_question_id is not None:
        previous_question = get_object_or_404(Question, pk=previous_question_id)
    else:
        previous_question = None
    context = {
        'current_question': current_question,
        'previous_question': previous_question,
    }
    return render_to_response("current_question.html", context, context_instance = RequestContext(request))


def vote(request, a_id):
    answer_selected = Answer.objects.get(id=a_id)
    previous_question = answer_selected.question
    previous_question.processvote(answer_selected, request)
    current_question = Question.objects.filter(~Q(id=previous_question.id)).order_by('?')[:1].get()
    request.session['previous_question_id'] = previous_question.id
    return redirect(current_question)
    # return redirect('current_question', current_question_id=current_question.id, previous_question_id=previous_question.id)
    # return HttpResponseRedirect(reverse('questions.views.current_question', args=[current_question.id, previous_question.id]))


def question_details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    resp_dict={
        "question":question.question,
        "value":question.total_vote_count,
        "answers":[],
        "start": question.votes.order_by('created')[0].date,
        "end": question.votes.latest('created').date,
    }
    for answer in question.answers.all().annotate(vote_count=Count('votes')).order_by('-vote_count'): # this will run thru the answers in order of # votes
        vote_list=[]
        for vote in answer.votes.all():
            vote_dict=dict()
            if vote.voter:
                if vote.voter.gender: vote_dict["gender"]=vote.voter.gender
                if vote.voter.agegroup: vote_dict["agegroup"]=vote.voter.agegroup
                if vote.voter.political: vote_dict["political"]=vote.voter.political
            else:
                 vote_dict["gender"]="Unknown"
                 vote_dict["agegroup"]="Unknown"
                 vote_dict["political"]="Unknown"
            vote_dict["date"]=vote.date
            vote_dict["count"]=1
            vote_list.append(vote_dict)
        resp_dict["answers"].append({
            "answer":answer.answer,
            "count":answer.votes.count(),
            # "data":list(answer.selected_by.values('gender','agegroup','political','votes__date').annotate(count=Count('id'))),
            "data": vote_list,
        })
    json = simplejson.dumps(resp_dict).replace("'",r"\'")
    context = {
        "question":question,
        "json":json,
    }
    return render_to_response("question_details.html", context, context_instance=RequestContext(request))


def getjson(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    resp_dict={
        "question":question.question,
        "value":question.total_vote_count,
        "answers":[],
        "start": question.votes.order_by('created')[0].date,
        "end": question.votes.latest('created').date,
    }
    for answer in question.answers.all():
        vote_list=[]
        for vote in answer.votes.all():
            vote_dict=dict()
            if vote.voter:
                if vote.voter.gender: vote_dict["gender"]=vote.voter.gender
                if vote.voter.agegroup: vote_dict["agegroup"]=vote.voter.agegroup
                if vote.voter.political: vote_dict["political"]=vote.voter.political
            else:
                 vote_dict["gender"]="Unknown"
                 vote_dict["agegroup"]="Unknown"
                 vote_dict["political"]="Unknown"
            vote_dict["date"]=vote.date
            vote_dict["count"]=1
            vote_list.append(vote_dict)
        resp_dict["answers"].append({
            "answer":answer.answer,
            "count":answer.votes.count(),
            # "data":list(answer.selected_by.values('gender','agegroup','political','votes__date').annotate(count=Count('id'))),
            "data": vote_list,
        })
    json = simplejson.dumps(resp_dict).replace("'",r"\'")
    context = {
        "question":question,
        "json":json,
    }
    return HttpResponse(json, mimetype='application/json')

def search(request):
    resp=[]
    if 'q' in request.GET:
        q=request.GET.get('q')
        queryset=Question.objects.filter(Q(question__icontains=q))
    else:
        queryset=Question.objects.all()
    for question in queryset:
        newdict=dict()
        wordlist=[]
        for word in question.question.split():
            wordlist.append(word)
        newdict["value"]=question.question
        newdict["id"]=question.id
        newdict["tokens"]=wordlist
        resp.append(newdict)
    json = simplejson.dumps(resp)
    print json
    return HttpResponse(json, mimetype='application/json')

def search_results(request):
    q=request.GET.get('q')
    response_dict = {
        'results':Question.objects.filter(Q(question__icontains=q)).order_by('question'),
        }
    return render_to_response("search_results.html", response_dict, context_instance=RequestContext(request))