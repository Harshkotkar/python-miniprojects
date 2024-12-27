import pandas as pd
import csv
from datetime import datetime
class CSV:
    csv_file='finance_data.csv'
    @classmethod
    def initalization_csv(cls):
        try:
            pd.read_csv(cls.csv_file)
        except:
            df=pd.DataFrame(columns=["date","amt","category","desc"])
            df.to_csv(cls.csv_file,index=False)

    @classmethod
    def add_entry(cls,date,amt,category,desc):
        new_entery={
            'date':date,
            'amt':amt,
            'category':category,
            'desc':desc
        }
        with open(cls.csv_file,'a',)
CSV.initalization_csv()

