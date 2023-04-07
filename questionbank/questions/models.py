from django.db import models
from django.urls import reverse


class Exam(models.Model):
    pdf_url = models.URLField(max_length=200)
    pdf_path = models.FilePathField()
    level = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    version = models.CharField(max_length=200)

    def questions(self):
        questions = [source.question for source in self.source_set.all()]
        return questions

    def get_absolute_url(self):
        return reverse('exam-detail', kwargs={"pk": self.pk})

    def name(self):
        return f'{self}'

    def __str__(self):
        return f'{self.level} {self.year} versie {self.version}'


class Question(models.Model):
    text = models.TextField()
    context = models.TextField()

    def get_absolute_url(self):
        return reverse('question-detail', kwargs={"pk": self.pk})

    def source(self):
        return self.source_set.all()[0]

    def __str__(self):
        return f'{self.text}'


class Source(models.Model):
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
