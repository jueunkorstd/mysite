from secrets import choice
from django.db import models

# Create your models here.

class Question(models.Model):
    Question_text = models.CharField(max_length=200)
    #질문내용
    pub_date = models.DateTimeField('date published')
    # 생성 날짜

    def __str__(self) -> str:
        return self.Question_text

class Choice(models.Model):
    Question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # 선택지에 해당하는 질문
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text
