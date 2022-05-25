
from django.conf import settings
from django.urls import include, path
from app.Views.answers import AnswerCreateView, AnswerDeleteView, AnswerListView, AnswerUpdateView
from app.Views.dashboard import dashboard
from app.Views.front import first_question, front, next_question
from app.Views.order import list_questions, order, order_question
from app.Views.questions import QuestionCreateView, QuestionDeleteView, QuestionListView, QuestionUpdateView 

from app.Views.symptoms import SymptomListView , SymptomCreateView , SymptomDeleteView , SymptomUpdateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
   
    path('', include('django.contrib.auth.urls')),
   
    path('order-questions', list_questions,name="questions-order"),

    path('user/', front,name="front"),

    path('questions/', first_question,name="first_question"),

    path('next_question/<int:previous_question>/<int:previous_answer>', next_question,name="next_question"),


    path('order-qs/', order_question,name="order-qs"),

    path('', dashboard , name="dashboard") ,
    
    path('order/', order , name="order") ,

    path('symptoms', SymptomListView.as_view() , name="symptoms-list") ,
    path('add-symptom/', SymptomCreateView.as_view() , name="symptoms-create") ,
    path('delete-symptom/<int:pk>/', SymptomDeleteView.as_view() , name="symptoms-delete") , 
    path('update-symptom/<int:pk>/', SymptomUpdateView.as_view() , name="symptoms-update") , 

    path('questions/<int:symptom_id>', QuestionListView.as_view() , name="questions-list") ,
    path('add-question/<int:symptom_id>', QuestionCreateView.as_view() , name="questions-create") ,
    path('delete-question/<int:pk>/', QuestionDeleteView.as_view() , name="questions-delete") , 
    path('update-question/<int:pk>/', QuestionUpdateView.as_view() , name="questions-update") , 

    path('answers/<int:question_id>', AnswerListView.as_view() , name="answers-list") ,
    path('add-answer/<int:question_id>', AnswerCreateView.as_view() , name="answers-create") ,
    path('delete-answer/<int:pk>/', AnswerDeleteView.as_view() , name="answers-delete") , 
    path('update-answer/<int:pk>/', AnswerUpdateView.as_view() , name="answers-update") ,


]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)