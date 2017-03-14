from django.http import HttpResponse
from django.shortcuts import render
from .models import Question, Comment
from .forms import QuestionForm, CommentForm

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'socrates/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
	comments = question.comments
	if request.method == 'POST':
	  # A comment was posted
	  comment_form = CommentForm(data=request.POST)
	  if comment_form.is_valid():
	    # Create Comment object but don't save to database yet
	    new_comment = comment_form.save(commit=False)
	    # Assign the current post to the comment
	    new_comment.question = question
	    new_comment.ownerComment = request.user
	    # Save the comment to the database
	    new_comment.save()
	else:
	    comment_form = CommentForm()
	return render(request,'socrates/detail.html',
		     {'question': question, 'comments': comments, 'comment_form': comment_form})
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
#    return render(request, 'socrates/detail.html', {'question': question, 'comments': comments}, )

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def pose(request):
    if request.method == 'POST':
      question_form = QuestionForm(data=request.POST)
      if question_form.is_valid():
        new_question = question_form.save(commit=False)
	new_question.owner = request.user
	new_question.save()
    else:
      question_form = QuestionForm()

    return render(request, 'socrates/pose.html', {'question_form': question_form})
