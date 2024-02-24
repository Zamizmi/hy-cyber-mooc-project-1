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
        return Question.objects.order_by("-pub_date")


class DetailsView(generic.DetailView):
    model = Question
    template_name = "details.html"


@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
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
        return HttpResponseRedirect(reverse("polls:details", args=(question.id,)))


class QuestionCreateView(generic.CreateView):
    model = Question
    fields = ["question_text"]

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


def getCreateVote(request):
    if request.method == "POST":
        form = PollForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/polls/")

    else:
        form = PollForm()
    return render(request, "createPoll.html", {"form": form})


@login_required
def postCreateCote(request):
    questionBody = request.body
    try:
        createdQuestion = Question.objects.create(questionBody)
    except KeyError:
        return HttpResponseRedirect(reverse("polls:create"))
    else:
        createdQuestion.save()
        return HttpResponseRedirect(
            reverse("polls:details", args=(createdQuestion.id,))
        )
