import pandas as pd
import sqlite3
from file_path import path # file with file path to .db file 

conn = sqlite3.connect(path)

df = pd.read_sql_query('SELECT * FROM invoice_line;', conn)
