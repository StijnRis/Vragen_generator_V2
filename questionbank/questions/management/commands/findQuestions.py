from datetime import datetime
import re
from io import BytesIO
import requests
import pypdf
from questions.models import Exam, Question, Examination
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, **options):
        Question.objects.all().delete()
        Examination.objects.all().delete()
        for exam in Exam.objects.all():
            self.find_questions_in_exam(exam)

    def find_questions_in_exam(self, exam: Exam):
        print(f'Finding questions for {exam}')
        fileReader = pypdf.PdfReader(exam.pdf_path)

        content = '{webpage 1}'
        for page in fileReader.pages:
            content += page.extract_text() + \
                f'\n {{webpage {fileReader.get_page_number(page)+2}}}'
        with open('test.txt', 'w', encoding="utf-8") as file:
            file.write(content)
        content = re.sub(
            r'([A-Z]*-){0,1}([a-z0-9-]+) ([0-9 \/]+?) [lL]ees verder( ►►►){0,1}', '\n', content)

        matches = re.finditer(
            r'\n[0-9]p ([0-9]+)([\s\S]+?) *?(?=(\n *\n|\n[0-9]p|\Z))', content)
        parsed_content = content
        page_number = 1
        for match in matches:
            index = parsed_content.find(match.group())
            context = parsed_content[:index]
            page_number_match = re.findall(r"{webpage (\d+)}", context)
            if page_number_match:
                page_number = int(page_number_match[-1])
            parsed_content = parsed_content[index+len(match.group()):]
            question_number = int(match[1])
            text = match[2].strip()

            question = Question()
            question.text = text
            question.context = context.strip()
            question.save()

            examination = Examination()
            examination.exam = exam
            examination.question = question
            examination.question_number = question_number
            examination.page_number = page_number
            examination.save()
