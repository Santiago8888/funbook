from .models import Question, Comment
from django import forms
class QuestionForm(forms.ModelForm):
  class Meta:
    model = Question
    fields = ('question_text', 'question_body')

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ('comment_text',)
