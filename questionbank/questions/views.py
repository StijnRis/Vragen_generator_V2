from django.shortcuts import render
from django.views import generic
from django.db.models import Q
from questions.models import Exam, Question, Examination


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_exams = Exam.objects.all().count()
    num_questions = Question.objects.all().count()
    num_examinations = Examination.objects.count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits

    context = {
        'num_exams': num_exams,
        'num_questions': num_questions,
        'num_examinations': num_examinations,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'questions/index.html', context=context)


class ExamListView(generic.ListView):
    model = Exam
    paginate_by = 10
    template_name = 'questions/exam_list.html'
    context_object_name = 'exams'

    def get_queryset(self):
        return Exam.objects.all()


class ExamDetailView(generic.DetailView):
    model = Exam
    template_name = 'questions/exam_detail.html'
    context_object_name = 'exam'


class QuestionListView(generic.ListView):
    model = Question
    paginate_by = 10
    template_name = 'questions/question_list.html'
    context_object_name = 'questions'

    def get_queryset(self):
        return Question.objects.all()


class SearchQuestionListView(generic.ListView):
    model = Question
    paginate_by = 10
    template_name = 'questions/question_list.html'
    context_object_name = 'questions'

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Question.objects.filter(
            Q(text__icontains=query) | Q(context__icontains=query)
        )
        return object_list


class QuestionDetailView(generic.DetailView):
    model = Question
    template_name = 'questions/question_detail.html'
    context_object_name = 'question'


class ExaminationListView(generic.ListView):
    model = Examination
    paginate_by = 10
    template_name = 'questions/examination_list.html'
    context_object_name = 'examinations'

    def get_queryset(self):
        return Examination.objects.all()


class ExaminationDetailView(generic.DetailView):
    model = Examination
    template_name = 'questions/examination_detail.html'
    context_object_name = 'examination'
