from django.core.management.base import BaseCommand, CommandError
from agent_dashboard.utils.policy_data_import import PolicyDataImport 
import os


class Command(BaseCommand):
    help = 'Usage: python manage.py import_policy_data_from_csv --file=csv_file_path'

    def add_arguments(self, parser):
        parser.add_argument('--file', type=str)

    def handle(self, *args, **options):
        import_csv_file_path =  options.get('file','')
        print(import_csv_file_path)
        if os.path.isfile(import_csv_file_path):
            PolicyDataImport()._from_csv(import_csv_file_path)
        else:
            print('Invalid CSV file path')
        ...
        # SubsciptionPptEmail.main('test')