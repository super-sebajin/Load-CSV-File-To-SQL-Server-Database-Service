import pandas as pd
import numpy as np
import sys
from typing import Dict

base_directory = "./app/workers/app_data/"

file_path = f"{base_directory}{sys.argv[2]}"

data_file = pd.read_csv(file_path)

data_file.ffill(inplace=True)


def make_column_string() -> str:
    return ','.join(list(data_file.columns))


def make_statements() -> Dict:
    
    file_values = list(data_file.values)
    
    final_insert_string = ""
    
    insert_values = list()
    
    for val in file_values:
        
        interim = [f"'{str(x)}'" for x in val.tolist()]
        insert_values.append(f"('{sys.argv[1]}',{','.join(tuple(interim))})\n")

    for n_values_string in np.array_split(insert_values, 10):
        
        values_string = ','.join(n_values_string)
        insert_string = (f"INSERT INTO FILE_DATA (FILE_DATE,"
                         f"{make_column_string()})\nVALUES {values_string};\n")
        final_insert_string = insert_string + final_insert_string

    metadata_insert_string = f"INSERT INTO FILE_NAME (DATA_FILE_NAME) VALUES ('{sys.argv[2]}');"
    
    return {'file-data': final_insert_string, 'file-metadata':f"{metadata_insert_string}"}

def do_db_job():
    import db
    inserts = make_statements()
    
    try:
        with db.cursor:
            # 1. Inserta file name and throw error if the file had been sent already
            db.cursor.execute(f"{inserts['file-metadata']}")
            db.cursor.commit()
            
            # 2. Insert the data set
            db.cursor.execute(f"{inserts['file-data']}")
            db.cursor.commit()
        print("DB loading job Done!")
    
    except db.pyodbc.Error as err:
        print(f"Commit unsuccessful, please see the error message: {err}")
        print("DB loading job unsuccessful!") 

def clean_up():
    import os
    
    os.remove(file_path)
    print("File deleted and folder emptied!")

if __name__ == "__main__":
    
    print("Doing work!")
    
    do_db_job()
    clean_up()
    
    print("Work done!")
    
   
