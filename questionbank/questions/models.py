from django.db import models
from django.urls import reverse


class Exam(models.Model):
    name = models.CharField(max_length=200)
    pdf_url = models.URLField(max_length=200)
    pdf_path = models.FilePathField()
    level = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    version = models.CharField(max_length=200)

    def examinations(self):
        return self.examination_set.all()

    def get_absolute_url(self):
        return reverse('exam-detail', kwargs={"pk": self.pk})

    def __str__(self):
        return f'{self.name}'


class Question(models.Model):
    text = models.TextField()
    context = models.TextField()

    def get_absolute_url(self):
        return reverse('question-detail', kwargs={"pk": self.pk})

    def examination(self):
        return self.examination_set.all()[0]

    def __str__(self):
        return f'{self.text}'


class Examination(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    page_number = models.IntegerField()
    question_number = models.IntegerField()

    def get_absolute_url_to_pdf(self):
        return f'{self.exam.pdf_url}#page={self.page_number}'

    def get_absolute_url(self):
        return reverse('examination-detail', kwargs={"pk": self.pk})

    def __str__(self):
        return f'{self.question} in {self.exam}'
