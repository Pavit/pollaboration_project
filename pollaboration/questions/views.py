from django.conf import settings
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q, Count
from questions.models import *
from django.core.urlresolvers import reverse


def index(request):
    current_question = Question.objects.all().order_by('?')[:1].get()
    return HttpResponseRedirect(reverse('questions.views.current_question', args=(current_question.id,)))


def current_question(request, current_question_id):
    previous_question_id = request.session.get('previous_question_id', None)
    if previous_question_id is not None:
        previous_question = get_object_or_404(Question, pk=previous_question_id)
    else:
        previous_question = None
    current_question = get_object_or_404(Question, pk=current_question_id)
    context = {
        'current_question': current_question,
        'previous_question': previous_question,
    }
    return render_to_response("current_question.html", context, context_instance = RequestContext(request))


def vote(request, a_id):
    answer = Answer.objects.get(id=a_id)
    previous_question = answer.question
    if request.user.is_authenticated():
        print "hi"
    else:
        vote = Vote.objects.create(voter=None, answer=answer)
        vote.answer = answer
        vote.save()
    current_question = Question.objects.filter(~Q(id=previous_question.id)).order_by('?')[:1].get()
    request.session['previous_question_id'] = previous_question.id
    return redirect(current_question)
    # return redirect('current_question', current_question_id=current_question.id, previous_question_id=previous_question.id)
    # return HttpResponseRedirect(reverse('questions.views.current_question', args=[current_question.id, previous_question.id]))