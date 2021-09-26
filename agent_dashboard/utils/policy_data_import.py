import pandas as pd
import pymysql.cursors
from django.conf import settings
from agent_dashboard.models import Policy,Customer


class PolicyDataImport:
    '''
    Grouped data importing functions through various data pipelines.
    Currently Supported formats : CSV
    Models : Policy , Customer
    Management Command : python manage.py policy_data_import --file=<csv_file_path>
    '''

    db_config = settings.DATABASES.get('default')
    db_name = db_config.get('NAME')
    db_user = db_config.get('USER')
    db_pass = db_config.get('PASSWORD')
    db_host = db_config.get('HOST')
    # Using pymysql over ORM to optimize resource usage for importing large data set
    # To maintain high-performance while performing bulk inserts


    def _from_csv(self,csv_file_path:str):
        '''
        CSV data parser to insert selected fields from CSV to Mysql DB.
        '''
        try:
            data_frame = pd.read_csv(csv_file_path)
            # Get distinct customer ids from data set
            new_customers_dataset = set(data_frame['Customer_id'].unique())
            
            # Get distict policy ids from data set. 
            new_policy_dataset = set(data_frame['Policy_id'].unique())

            # Perform data cleaning operations on dataset 
            # Rename "Date of Purchase" column and setting same date format on  purchase_date
            data_frame.rename(columns = {"Date of Purchase": "purchase_date"},inplace=True)
            data_frame['purchase_date'] = pd.to_datetime(data_frame['purchase_date'])


            # Filter out the previouly inserted Customer and Policy Objects from the New dataset.
            filtered_new_customers_dataset = self.check_and_remove_existing_objects(Customer,new_customers_dataset)
            filtered_new_policy_dataset = self.check_and_remove_existing_objects(Policy,new_policy_dataset)

            # Create tuples for peforming bulk insert on Policy Model using pymysql cursor
            insert_data = []
            for row in data_frame.itertuples():
                if row.Policy_id in filtered_new_policy_dataset: 
                    insert_data.append(tuple([row.Policy_id,row.purchase_date,row.Customer_id,row.Premium,row.Customer_Region]))

            # Query string for inserting into data into Policy and Customer Models.
            insert_customer_query = "INSERT INTO customer (customer_id) Values (%s)"
            insert_policy_query = 'INSERT INTO policy (policy_id,purchase_date,fk_customer_id,premium,region) VALUES(%s, %s, %s, %s, %s)' 
            
            # Execute the query on the database to insert the new data.
            self.execute_insert_query(insert_customer_query,filtered_new_customers_dataset,many=True)
            self.execute_insert_query(insert_policy_query,insert_data,many=True)
            print('Data import completed succuessfully !')
        
        except Exception as e:
            print('Error in data import : ',e)


    def check_and_remove_existing_objects(self,model,new_data_set:list):
        '''
        Utility for filtering the available objects from new dataset.
        Arguments: model : Model class for which filter operation is to be perfomed.
        new_data_set : new data set object id list from previouly available data is to be filtered.
        '''
        existing_objects_dataset = model.objects.only('pk').values_list('pk',flat=True)
        return list(set(new_data_set) - set(existing_objects_dataset))


    def execute_insert_query(self, query, params, many:bool=False):
        '''
        PyMysql utility for perforing insert/update operations.
        Many - True : Use executemany for bulk insertion/updation
               False : Use execute for single insertion/updation
        '''
        try:
            connection = pymysql.connect(host=self.db_host, user=self.db_user, password=self.db_pass,
                                         db=self.db_name, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor, autocommit=True)
            with connection.cursor() as cursor:
                if many is True:
                    cursor.executemany(query, (params))
                else:
                    cursor.execute(sql, (params))
        except Exception as e:
            print('There was an exception in DBservice 10:', e)
            connection.close()
