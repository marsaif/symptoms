from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView , UpdateView
from django.urls import reverse
from app.forms import AnswerForm
from app.models import Answer, Question
from django.contrib.auth.mixins import LoginRequiredMixin


class AnswerListView(LoginRequiredMixin,ListView):
    model = Answer
    template_name = "answer/list.html"
    paginate_by = 10  

    def get_queryset(self):
        return Answer.objects.filter(question_id=self.kwargs['question_id'])

    def get_context_data(self, **kwargs):
        context = super(AnswerListView, self).get_context_data(**kwargs)
        context['question_id'] = self.kwargs['question_id']
        return context

class AnswerCreateView(LoginRequiredMixin,CreateView):
    model = Answer
    form_class = AnswerForm
    template_name = "answer/create.html"
    
    def get_success_url(self):
        return reverse('answers-list',args=(self.kwargs.get('question_id'),))

    def form_valid(self, form):
            form.instance.question =Question.objects.get(pk=self.kwargs.get('question_id')) 
            return super().form_valid(form)



class AnswerDeleteView(LoginRequiredMixin,DeleteView):
    model = Answer

    def get_success_url(self):
        return reverse('answers-list',args=(self.object.question.id,))

class AnswerUpdateView(LoginRequiredMixin,UpdateView):
    model = Answer
    form_class = AnswerForm
    template_name = "answer/update.html"

    def get_success_url(self):
        return reverse('answers-list',args=(self.object.question.id,))

   

