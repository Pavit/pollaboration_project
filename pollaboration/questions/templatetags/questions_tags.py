from django import template
from django.conf import settings

register = template.Library()

# settings value
@register.simple_tag
def settings_value(name):
    return getattr(settings, name, "")


@register.simple_tag
def total_submission_votes(user):
    total=0
    for sub in user.submissions.all():
        total+=sub.total_vote_count
    return total


@register.simple_tag
def percentage(previous_question, answer):
      if previous_question.total_vote_count > 0:
            return int(float(answer.votes.count()) / float(previous_question.total_vote_count) * 100)
      else:
            return 0