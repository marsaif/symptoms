from django import forms

from app.models import Answer, Question, Symptom

class SymptomForm(forms.ModelForm):

    description = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Symptom
        exclude = ('ordered',)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['symptom'].widget.attrs['class'] = 'form-control'
        self.fields['upload'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'  
        exclude = ('symptom','previous_answer','previous_question','first_question')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['question'].widget.attrs['class'] = 'form-control'
        self.fields['image'].widget.attrs['class'] = 'form-control'

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = '__all__'  
        exclude = ('question',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['answer'].widget.attrs['class'] = 'form-control'