from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.db.models import F
from django.contrib.auth.decorators import login_required
from .forms import PollForm

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = "index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailsView(generic.DetailView):
    model = Question
    template_name = "details.html"


@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "details.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:details", args=(question.id,)))


class QuestionCreateView(generic.CreateView):
    model = Question
    fields = ["question_text"]

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


def getCreateVote(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = PollForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print(2222, form.data)
            question = form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/polls/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PollForm()
    return render(request, "createPoll.html", {"form": form})


@login_required
def postCreateCote(request):
    questionBody = request.body
    try:
        createdQuestion = Question.objects.create(questionBody)
    except KeyError:
        # Redisplay the creation form.
        return HttpResponseRedirect(reverse("polls:create"))
    else:
        createdQuestion.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(
            reverse("polls:details", args=(createdQuestion.id,))
        )
