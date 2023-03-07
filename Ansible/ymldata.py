import yaml
import mysql.connector
#load database configuration from YAML file
with open('config.yml','r') as f:
    config = yaml.safe_load(f)['database']
#connect to database
conn=mysql.connector.connect(
    host=config['host'],
    port=config['port'],
    database=config['dbname'],
    user=config['user'],
    password=config['password']
)
cur=conn.cursor()
cur.execute("SELECT * FROM hcl_vijayawada.customer")
rows=cur.fetchall()
for row in rows:
    print(row)
#close the database connection when finished
cur.close()
conn.close()