from django import forms
from django.forms.models import BaseInlineFormSet
from questions.models import *


class QuestionForm(forms.ModelForm):
    question=forms.CharField(label="Question", min_length=5,max_length=60,
                             error_messages={
                                    "required":"Seriously? You need a QUESTION to ASK something."})
    class Meta:
        model = Question
        exclude = ("submitter","created","answered_by","slug","modified",)


class AnswerForm(forms.ModelForm):
    answer = forms.CharField(label="Answer", max_length=50)
    class Meta:
        model = Answer
        exclude = ("question","selected_by","modified",)


class AnswerFormSet(BaseInlineFormSet):
    def clean(self):
        super(AnswerFormSet, self).clean()
        blanks = []
        for form in self.forms:
            try:
                print form
                x=form.cleaned_data['answer']
            except:
                blanks.append(form)
        if len(blanks)>=4:
            raise forms.ValidationError("There are no stupid questions. Except this one. Please enter at least 2 answer choices.")