from sqlalchemy import create_engine
engine = create_engine('postgresql://lab4_user:DoveLove@localhost:5432/lab4')
conn = engine.connect()
conn.close()