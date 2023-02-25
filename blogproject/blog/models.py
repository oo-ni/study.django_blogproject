from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):   # 글 제목 표시 함수
        return self.title

    def summary(self):   # 글 내용 요약 함수
        return self.body[:150]