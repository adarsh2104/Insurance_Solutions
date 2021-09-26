from django.core.management.base import BaseCommand, CommandError
from agent_dashboard.utils.policy_data_import import PolicyDataImport 
import os


class Command(BaseCommand):
    '''
    Management command for performing data import through CSV file
    Supported Models : Policy , Customer
    '''
    
    help = 'Usage: python manage.py policy_data_import_from_csv --file=csv_file_path'

    def add_arguments(self, parser):
        parser.add_argument('--file', type=str)

    def handle(self, *args, **options):
        import_csv_file_path =  options.get('file','')
        if os.path.isfile(import_csv_file_path):
            PolicyDataImport()._from_csv(import_csv_file_path)
        else:
            print('Invalid CSV file path')