from django.db import models

# Create your models here.
class Polls(models.Model):
    text=models.CharField(max_length=255)
    pub_date=models.DateField()

    def __str__(self):
        return self.text


class Choice(models.Model):
    question=models.ForeignKey(Polls,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=255)
    votes=models.IntegerField(default=0)

    def __str__(self):
        return '{} - {}'.format(self.question.text[:20],self.choice_text[:20])
