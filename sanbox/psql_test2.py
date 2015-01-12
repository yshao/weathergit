import psycopg2
import sys

login={"host":"192.168.1.120","dbname":"postgres","user":"archiver","password":"password"}
con = None

try:
     
    con = psycopg2.connect(host='192.168.1.120',database='archiver', user='archiver', password='password')
    cur = con.cursor()
    cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
    ver = cur.fetchone()
    print ver    
    

except psycopg2.DatabaseError, e:
    print 'Error %s' % e    
    sys.exit(1)
    
    
finally:
    
    if con:
        con.close()