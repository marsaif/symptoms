from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView , UpdateView
from django.urls import reverse, reverse_lazy
from app.forms import QuestionForm

from app.models import Question, Symptom
from django.contrib.auth.mixins import LoginRequiredMixin

class QuestionListView(LoginRequiredMixin,ListView):
    model = Question
    template_name = "question/list.html"
    paginate_by = 10  

    def get_queryset(self):
        return Question.objects.filter(symptom_id=self.kwargs['symptom_id'])

    def get_context_data(self, **kwargs):
        context = super(QuestionListView, self).get_context_data(**kwargs)
        context['symptom'] = Symptom.objects.get(pk=self.kwargs['symptom_id'])
        return context

class QuestionCreateView(LoginRequiredMixin,CreateView):
    model = Question
    form_class = QuestionForm
    template_name = "question/create.html"
    def get_success_url(self):
        return reverse('questions-list',args=(self.kwargs.get('symptom_id'),))

    def form_valid(self, form):
            form.instance.previous_answer = 0
            form.instance.symptom = Symptom.objects.get(pk=self.kwargs.get('symptom_id'))
            return super().form_valid(form)

class QuestionDeleteView(LoginRequiredMixin,DeleteView):
    model = Question
    
    def get_success_url(self):
        return reverse('questions-list',args=(self.object.symptom.id,))

class QuestionUpdateView(LoginRequiredMixin,UpdateView):
    model = Question
    form_class = QuestionForm
    template_name = "question/update.html"
    
    def get_success_url(self):
        return reverse('questions-list',args=(self.object.symptom.id,))

   

