from django import forms
from django.forms.models import BaseInlineFormSet
from questions.models import *


class QuestionForm(forms.ModelForm):
    question = forms.CharField(label="Question", widget=forms.TextInput(attrs={'placeholder': 'What do you want to ask?'}))
    class Meta:
        model = Question
        fields = ("question",)


class AnswerForm(forms.ModelForm):
    answer = forms.CharField(label="Answer", widget=forms.TextInput(attrs={'placeholder': "What kind of answer do you want?"}))
    class Meta:
        model = Answer
        exclude = ("question","selected_by","modified",)


class AnswerFormSet(BaseInlineFormSet):
    def clean(self):
        super(AnswerFormSet, self).clean()
        # example custom validation across forms in the formset:
        blanks = []
        for form in self.forms:
            print form.cleaned_data
            print form
            try:
                print form.cleaned_data['answer']
                x=form.cleaned_data['answer']
                print form
                print x
            except:
                blanks.append(form)
                print "blank appended"
        if len(blanks)>=4:
            raise forms.ValidationError("Must have at least two answer choices!")