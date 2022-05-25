from django.shortcuts import render

from app.models import Question, Symptom
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json  
from django.http import JsonResponse

@login_required
def order(request):
        symptoms = Symptom.objects.all()
        context = {
            'symptoms' : symptoms 
        }
        return render(request,"order/order.html",context)

def list_questions(request):
    if request.method == "POST":
        symptom_id = request.POST['symptom']
        questions = Question.objects.filter(symptom_id=symptom_id)
        context = {
            'questions' : questions 
        }
        return render(request,"order/questions.html",context)

@csrf_exempt
def order_question(request):
    body_unicode = request.body.decode('utf-8') 	
    body = json.loads(body_unicode) 	
    question = Question.objects.get(pk=body['option'])
    question.previous_question = body['previousQuestion']

    if body['previousAnswer'] : 
        question.previous_answer = body['previousAnswer']
    question.save()
    return JsonResponse({'status':'good'})
