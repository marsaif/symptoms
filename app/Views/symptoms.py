from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView , UpdateView
from django.urls import reverse_lazy
from app.forms import SymptomForm
from app.models import Symptom
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

   

