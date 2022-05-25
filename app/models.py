from django.db import models
import uuid
import os

# Create your models here.
def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return filename

class Symptom(models.Model) : 
    ordered = models.BooleanField(default=False)
    symptom = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return self.symptom

class Question(models.Model) : 
    first_question = models.BooleanField(default=False)
    previous_question = models.IntegerField(default=0)
    previous_answer = models.IntegerField(default=0)
    question = models.CharField(max_length=1000)
    image = models.ImageField(upload_to=get_file_path,null=True, blank=True )
    symptom = models.ForeignKey(Symptom,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.question
    
    def serialize(self):
        return {
            "id" : self.id,
            "question": self.question,
            "image": self.image.url if self.image else None , 
        }



class Answer(models.Model) : 
    answer = models.CharField(max_length=1000)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.answer


    

