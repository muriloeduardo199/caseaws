# 02_create_schema.py

import sqlite3

# conectando...
conn = sqlite3.connect('dados.db')
# definindo um cursor
sqlite_insert_blob_query = """ INSERT INTO dados
                                 (cpf, datas) VALUES (?, ?)"""

empPhoto = sqlite3.converters