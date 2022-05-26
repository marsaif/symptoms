from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView , UpdateView
from django.urls import reverse_lazy
from app.forms import SymptomForm
from app.models import Question, Symptom
from django.contrib.auth.mixins import LoginRequiredMixin

class SymptomListView(LoginRequiredMixin,ListView):
    model = Symptom
    template_name = "symptom/list.html"
    paginate_by = 10  

class SymptomCreateView(LoginRequiredMixin,CreateView):
    model = Symptom
    form_class = SymptomForm
    template_name = "symptom/create.html"
    success_url = reverse_lazy('symptoms-list') 

class SymptomDeleteView(LoginRequiredMixin,DeleteView):
    model = Symptom
    success_url = reverse_lazy('symptoms-list') 

class SymptomUpdateView(LoginRequiredMixin,UpdateView):
    model = Symptom
    form_class = SymptomForm
    success_url = reverse_lazy('symptoms-list') 
    template_name = "symptom/update.html"

class OrderedSymptomListView(LoginRequiredMixin,ListView):
    model = Symptom
    template_name = "order/list_symptoms.html"
    paginate_by = 10   
    
    def get_queryset(self):
        return Symptom.objects.filter(ordered=True)

def clear_order_symptom(request,symptom_id) : 
    symptom = Symptom.objects.get(pk=symptom_id)
    symptom.ordered = False
    symptom.save()

    Question.objects.filter(symptom_id=symptom_id).update(first_question=False,previous_question=0,previous_answer=0)

    return redirect('/../ordered-symtoms/')


