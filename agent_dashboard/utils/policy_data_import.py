import pandas as pd
import pymysql.cursors
from django.conf import settings
from agent_dashboard.models import Policy,Customer


class PolicyDataImport:
    db_config = settings.DATABASES.get('default')
    db_name = db_config.get('NAME')
    db_user = db_config.get('USER')
    db_pass = db_config.get('PASSWORD')
    db_host = db_config.get('HOST')


    def _from_csv(self,csv_file_path:str):
        data_frame = pd.read_csv(csv_file_path)
        new_customers_dataset = set(data_frame['Customer_id'].unique())
        new_policy_dataset = set(data_frame['Policy_id'].unique())

        data_frame.rename(columns = {"Date of Purchase": "purchase_date"},inplace=True)
        data_frame['purchase_date'] = pd.to_datetime(data_frame['purchase_date'])
        
        filtered_new_customers_dataset = self.check_and_remove_existing_objects(Customer,new_customers_dataset)
        filtered_new_policy_dataset = self.check_and_remove_existing_objects(Policy,new_policy_dataset)

        insert_data = []
        for row in data_frame.itertuples():
            if row.Policy_id in filtered_new_policy_dataset: 
                insert_data.append(tuple([row.Policy_id,row.purchase_date,row.Customer_id,row.Premium,row.Customer_Region]))

        insert_customer_query = "INSERT INTO customer (customer_id) Values (%s)"
        insert_policy_query = 'INSERT INTO policy (policy_id,purchase_date,fk_customer_id,premium,region) VALUES(%s, %s, %s, %s, %s)' 
        self.execute_insert_query(insert_customer_query,filtered_new_customers_dataset,many=True)
        self.execute_insert_query(insert_policy_query,insert_data,many=True)


    def check_and_remove_existing_objects(self,model,new_data_set):
        existing_objects_dataset = model.objects.only('pk').values_list('pk',flat=True)
        return list(set(new_data_set) - set(existing_objects_dataset))


    def execute_insert_query(self, query, params, many=False):
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
