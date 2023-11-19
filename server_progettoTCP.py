import threading 
import socket
import mysql.connector
import sys

comunicazioni = ["",""]
PASSWORD = "CIAO"

def trasforma_lista(lista):
    stringa=""
    for elem in lista:
        stringa+='\n'
        for subelem in elem:
            stringa+=str(subelem)+' '

    return stringa
def gestisci_comunicazione(conn):
    conn.send("Benvenuto, inserisci password: ".encode())
    data = conn.recv(1024).decode()
    i=0
    d="Benvenuto, cosa vuoi fare: C=Create, U=update,R=read,D=delete,E=EXIT"
    while data != PASSWORD and i<2:
        i+=1
        conn.send(f"Password ERRATA, reinserisci password: tentativi rimasti {2-i} ".encode())
        data = conn.recv(1024).decode()      

    if(data != PASSWORD):
        conn.send(f"Password ERRATA troppe volte, arrivederci".encode())
        conn.close()
        return
    mess=d
    while True:
        conn.send(mess.encode())
        data = conn.recv(1024).decode()
        data=data.upper()
        #fatto
        if(data=="R"):
            conn.send("in che tabella vuoi leggere: D=dipendenti, Z=zone di lavoro".encode())
            data = conn.recv(1024).decode()    
            data=data.upper()
            dati_query = db_get(data)
            mess+='\n'+str(dati_query)
        #fatto
        elif(data=="D"):
            conn.send("che tabella vuoi selezionare? D=dipendenti, Z=zone di lavoro".encode())
            data=conn.recv(1024).decode()
            data=data.upper()
            mess=(trasforma_lista(db_get(data))+'\n\n').encode()
            conn.send(mess+"inserisci l'ID del record da eliminare".encode())
            id = conn.recv(1024).decode() 
            dati_query = db_delete(id,data)
            mess=(trasforma_lista(db_get(data))+'\n\n')
            mess='\n'+mess+d
        #fatto
        elif(data=="U"):
            conn.send("che tabella vuoi aggiornare: D=dipendenti, Z=zone di lavoro".encode())
            data = conn.recv(1024).decode() 
            data=data.upper()
            dati_query = db_update(data,conn)
            mess='\n'+str(dati_query)+d

        elif(data=="C"):
            conn.send("in che tabella vuoi inserire un record?  D=dipendenti, Z=zone di lavoro".encode())
            data = conn.recv(1024).decode() 
            data=data.upper()
            dati_query = db_create(data,conn)
            mess='\n'+trasforma_lista(db_get(data))+'\n'+d       
        elif(data=="E"):
            conn.send('E'.encode())
            sys.exit()
        
    return

def db_get(data):
    conn = mysql.connector.connect(
        #host="10.10.0.10", #a scuola
        host="127.0.0.1", #a casa
        user="federico_oliva",
        password="oliva1234",
        database="5ATepsit",
        port=3306, 
        )

    cur = conn.cursor()

    query = "SELECT * FROM "
    if(data=='D'):
        query+='dipendenti_federico_oliva'
    elif(data=='Z'):
        query+='zone_di_lavoro_federico_oliva'
    
    cur.execute(query)
    dati = cur.fetchall()
    return dati

def db_update(data,con):
    conn = mysql.connector.connect(
        #host="10.10.0.10", #a scuola
        host="127.0.0.1", #a casa
        user="federico_oliva",
        password="oliva1234",
        database="5ATepsit",
        port=3306, 
        )
    cur = conn.cursor()
    mess=(trasforma_lista(db_get(data))+'\n\n').encode()
    if(data=='D'):
        con.send(mess+"inserisci l'id del dipendente da modificare".encode())
        id=con.recv(1024).decode()

        con.send("inserisci il nome".encode())
        nome=con.recv(1024).decode()
        con.send("inserisci il cognome".encode())
        cognome=con.recv(1024).decode()
        con.send("inserisci la posizione lavorativa".encode())
        pos=con.recv(1024).decode()
        con.send("inserisci la data di assunzione".encode())
        dataA=con.recv(1024).decode()
        con.send("inserisci il codice fiscale".encode())
        cf=con.recv(1024).decode()
        con.send("inserisci la data di nascita".encode())
        dataN=con.recv(1024).decode()
        query = f'Update dipendenti_federico_oliva SET nome = \'{nome}\', cognome = \'{cognome}\', posizione_lavorativa = \'{pos}\', data_di_assunzione = \'{dataA}\', codice_fiscale = \'{cf}\', data_nascita = \'{dataN}\' WHERE id = \'{id}\''
    elif(data=='Z'):
        con.send(mess+"inserisci l'id del reparto da modificare".encode())
        id=con.recv(1024).decode()
        con.send("inserisci il nome della zona".encode())
        nome=con.recv(1024).decode()
        con.send("inserisci il numero dei clienti".encode())
        numC=con.recv(1024).decode()
        con.send("inserisci il numero dei posti".encode())
        numP=con.recv(1024).decode()
        con.send("inserisci l'id del dipendente".encode())
        idD=con.recv(1024).decode()
        query = f'Update zone_di_lavoro_federico_oliva SET nome_zona = \'{nome}\', numero_clienti = {numC}, numero_posti = {numP}, id_dipendenti = {idD} WHERE id_zona = \'{id}\''

    cur.execute(query)
    conn.commit()

    #print(query)
    return 

def db_create(data,con):
    conn = mysql.connector.connect(
        #host="10.10.0.10", #a scuola
        host="127.0.0.1", #a casa
        user="federico_oliva",
        password="oliva1234",
        database="5ATepsit",
        port=3306, 
        )
    
    cur = conn.cursor()

    if(data=='D'):
        con.send("inserisci il nome".encode())
        nome=con.recv(1024).decode()
        con.send("inserisci il cognome".encode())
        cognome=con.recv(1024).decode()
        con.send("inserisci la posizione lavorativa".encode())
        pos=con.recv(1024).decode()
        con.send("inserisci la data di assunzione".encode())
        dataA=con.recv(1024).decode()
        con.send("inserisci il codice fiscale".encode())
        cf=con.recv(1024).decode()
        con.send("inserisci la data di nascita".encode())
        dataN=con.recv(1024).decode()
        query = f'INSERT INTO dipendenti_federico_oliva (nome,cognome,posizione_lavorativa,data_di_assunzione,codice_fiscale,data_nascita) VALUES (\'{nome}\',\'{cognome}\',\'{pos}\',\'{dataA}\',\'{cf}\',\'{dataN}\')'

    elif(data=='Z'):
        mess=(trasforma_lista(db_get('D'))+'\n\n').encode()
        con.send(mess+"inserisci il nome della zona".encode())
        nome=con.recv(1024).decode()
        con.send("inserisci il numero dei clienti".encode())
        numC=con.recv(1024).decode()
        con.send("inserisci il numero dei posti".encode())
        numP=con.recv(1024).decode()
        con.send("inserisci l'id del dipendente".encode())
        idD=con.recv(1024).decode()
        query = f'INSERT INTO zone_di_lavoro_federico_oliva (nome_zona,numero_clienti,numero_posti,id_dipendenti) VALUES (\'{nome}\',{numC},{numP},{idD})'
    cur.execute(query)
    conn.commit()
    #print(query)
    return

def db_delete(id,data):
    conn = mysql.connector.connect(
        #host="10.10.0.10", #a scuola
        host="127.0.0.1", #a casa
        user="federico_oliva",
        password="oliva1234",
        database="5ATepsit",
        port=3306, 
        )

    cur = conn.cursor()
    query=''
    if(data=='D'):
        query = f"DELETE FROM dipendenti_federico_oliva where id = '{id}' "
    elif(data=='Z'):
        query = f"DELETE FROM zone_di_lavoro_federico_oliva where id = '{id}' "
    cur.execute(query)
    conn.commit()
    return


print("server in ascolto: ")
lock = threading.Lock()
HOST = ''                 # Nome simbolico che rappresenta il nodo locale, ci va l'indirizzo IP
PORT = 50010            # Porta non privilegiata arbitraria
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(10)
thread = []
lista_connessioni = []
i=0

while True:
    lista_connessioni.append( s.accept() ) #connessione = s.accept() 
    print('Connected by', lista_connessioni[i][1]) # print(connessione[0])
    thread.append(threading.Thread(target=gestisci_comunicazione, args = (lista_connessioni[i][0],) )) 
    thread[i].start()
    i+=1
