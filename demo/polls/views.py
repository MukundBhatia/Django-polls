from django.utils import timezone
from django.views import generic
from urllib import response
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
# Create your views here.
from django.urls import reverse
from .models import Question, Choice
from django.template import loader


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    {  # in order by - sign gives desc order and no sign give asc

        # output = ', '.join([q.question_text for q in latest_question_list])
        # return HttpResponse(output)
        # There’s a problem here, though: the page’s design is hard-coded
        # in the view. If you want to change the way the page looks,
        # you’ll have to edit this Python code. So let’s use Django’s
        # template system
    }
    context = {'latest_question_list': latest_question_list, }
    {
        # template = loader.get_template('polls/index.html')
        # return HttpResponse(template.render(context, request))

        # render is an easy way
        # both can be used template as well as render
    }
    return render(request, 'polls/index.html', context)
    {
        # It’s a very common idiom to load a template, fill a
        # context and return an HttpResponse object with the
        # result of the rendered template
    }


def detail(request, question_id):

    # raising a 404 error
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    # return HttpResponse("You're looking at question %s." % question_id)

    # shortcut
    question1 = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/detail.html', {'question': question1})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        # As the Python comment above points out, you should always return an
        #  HttpResponseRedirect after successfully dealing with
        # POST data.


{  # In our poll application, we’ll have the following four views:

    # Question “detail” page – displays a question text, with no results but with a form to vote.
    # Question “results” page – displays results for a particular question.
    # Question “index” page – displays the latest few questions.
    # Vote action – handles voting for a particular choice in a particular question.
}


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        # return Question.objects.order_by('-pub_date')[:5]
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
        # lte less than or equal to


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
