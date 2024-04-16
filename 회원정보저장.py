
import csv
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Export user data from Django Admin to CSV'

    def handle(self, *args, **options):
        # Django Admin에 저장된 모든 사용자 정보 가져오기
        users = User.objects.all()

        # CSV 파일 경로 정의
        csv_file_path = 'users.csv'

        # 사용자 정보를 CSV 파일에 작성
        with open(csv_file_path, 'w', newline='') as csvfile:
            fieldnames = ['id', 'pw', 'birth', 'gender']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for user in users:
                writer.writerow({
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                })

        self.stdout.write(self.style.SUCCESS('Successfully exported user data to {}'.format(csv_file_path)))