

from django.http import JsonResponse
from django.shortcuts import render
from app.models import Question, Symptom


def front(request):
        symptoms = Symptom.objects.filter(ordered=True)
        context = {
            'symptoms' : symptoms 
        }
        return render(request,"front/front.html",context)

def first_question(request):
    if request.method == "POST":
        symptom_id = request.POST['symptom']
        question = Question.objects.filter(symptom_id=symptom_id).filter(first_question=True)
        context = {
            'question' : question[0]
        }
        return render(request,"front/questions.html",context)

def next_question(request,previous_question,previous_answer):

    questions = Question.objects.filter(previous_question=int(previous_question))
    if not questions :
        return JsonResponse( {"finished" : True  },safe=False)
    
    if len(questions) == 1 : 
        if questions[0].previous_answer != 0 :
            if questions[0].previous_answer != int(previous_answer) :
                return JsonResponse( {"finished" : True  },safe=False)
            else :
                q = questions[0]
                answers = []
                for answer in q.answer_set.all() :
                    answers.append({ 'answer' : answer.answer , 'id' : answer.id})
                    
                
                return JsonResponse( {"question" : q.serialize() , 'answers' : answers  },safe=False)
        else :
            q = questions[0]
            answers = []
            for answer in q.answer_set.all() :
                answers.append({ 'answer' : answer.answer , 'id' : answer.id})
                
            
            return JsonResponse( {"question" : q.serialize() , 'answers' : answers  },safe=False)
    else :
        for question in questions:

            if question.previous_answer == int(previous_answer):
                q = question
        if not q :
            return JsonResponse( {"finished" : True  },safe=False)


        answers = []
        for answer in q.answer_set.all() :
            answers.append({ 'answer' : answer.answer , 'id' : answer.id})
            
        
        return JsonResponse( {"question" : q.serialize() , 'answers' : answers  },safe=False)

 