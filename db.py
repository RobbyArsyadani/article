import psycopg2


def db_connection():
    conn = psycopg2.connect(
        host='localhost',
        port=5432,
        database='db_blog', #sesuaikan sama nama database lu
        user='postgres',    #sesuaikan sama nama owner database bd_blog lu
        password='02062002' #kalo lu make postgres, sesuaikan ama password yang lu masukin pas masuk pgAdmin
    )
    return conn