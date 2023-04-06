from datetime import datetime
import re
from io import BytesIO
import requests
import pypdf
from questions.models import Exam, Question, Examination
from django.core.management.base import BaseCommand
import os
import shutil
from pathlib import Path
import os.path


class Command(BaseCommand):
    def handle(self, **options):
        self.folder = os.path.dirname(__file__) + '/../pdf_exams'
        Exam.objects.all().delete()
        self.find_and_download_all_nvon_exams()

    def clear_folder(self):
        for filename in os.listdir(self.folder):
            file_path = os.path.join(self.folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))

    def find_and_download_all_nvon_exams(self) -> list[Exam]:
        urls = [
            {
                'level': 'vmbo',
                'url': 'https://newsroom.nvon.nl/files/default/skc{name}vb.pdf'
            },
            {
                'level': 'vmbo',
                'url': 'https://newsroom.nvon.nl/files/default/nask2tl{name}vb.pdf'
            },
            {
                'level': 'havo',
                'url': 'https://newsroom.nvon.nl/files/default/skh{name}vb.pdf'
            },
            {
                'level': 'vwo',
                'url': 'https://newsroom.nvon.nl/files/default/skv{name}vb.pdf'
            }
        ]

        for url_item in urls:
            for year in range(2000, datetime.today().year):
                for version in range(1, 3):
                    name = str(year)[-2:] + str(version)
                    url = url_item['url'].replace('{name}', name)
                    path = f'{self.folder}/{name}.pdf'

                    print(f'Downloading exam to {path}')
                    response = requests.get(url, stream=True)
                    if response.status_code == 404:
                        print('PDF was not found')
                        continue
                    with open(path, 'wb+') as f:
                        f.write(response.content)

                    exam = Exam()
                    exam.name = name
                    exam.url = url
                    exam.pdf_path = path
                    exam.level = url_item['level']
                    exam.year = year
                    exam.version = version
                    exam.save()
