import pandas as pd
import pymysql.cursors
from django.conf import settings


class PolicyDataImport:
    db_config = settings.DATABASES.get('default')
    db_name = db_config.get('NAME')
    db_user = db_config.get('USER')
    db_pass = db_config.get('PASSWORD')
    db_host = db_config.get('HOST')
    
    def execute_insert_query(self,query,params,many=False):
        try:
            connection = pymysql.connect(host=self.db_host, user=self.db_user, password=self.db_pass,db=self.db_name, charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor,autocommit=True)
            with connection.cursor() as cursor:
                if many is True:
                    cursor.executemany(query,(params))
                else:
                    cursor.execute(sql,(params))
        except Exception as e:
            print('There was an exception in DBservice 10:',e)
            connection.close()


    def _from_csv(self,csv_file_path:str):
        data_frame = pd.read_csv(csv_file_path)
        all_customers = set(data_frame['Customer_id'].unique())
        data_frame.rename(columns = {"Date of Purchase": "purchase_date"},inplace=True)
        data_frame['purchase_date'] = pd.to_datetime(data_frame['purchase_date'])

        insert_customer_query = "INSERT INTO customer (customer_id) Values (%s)"
        insert_policy_query = 'INSERT INTO policy (policy_id,purchase_date,fk_customer_id,premium,region) VALUES(%s, %s, %s, %s, %s)' 
        

        insert_data = []
        for row in data_frame.itertuples():
            insert_data.append(tuple([row.Policy_id,row.purchase_date,row.Customer_id,row.Premium,row.Customer_Region]))
        self.execute_insert_query(insert_customer_query,all_customers,many=True)
        self.execute_insert_query(insert_policy_query,insert_data,many=True)