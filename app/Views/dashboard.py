

from django.shortcuts import redirect, render
from app.models import Answer , Question , Symptom
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
        nbr_symptoms = len(Symptom.objects.all())
        nbr_questions = len(Question.objects.all())
        nbr_answers = len(Answer.objects.all())
        context = {
            'nbr_symptoms' : nbr_symptoms ,
            'nbr_questions' : nbr_questions , 
            'nbr_answers' : nbr_answers
        }

        return render(request,"dashboard/dashboard.html",context)
