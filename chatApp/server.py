#!/usr/bin/python
import socket    
import thread  
import threading
from threading import Thread
import time   
import json        
s = socket.socket()         
host = '' 
port = 1234                 
s.bind((host, port))       
s.listen(5)
users={"1":{"conn":"conn","username":"nishant","password":"nishant"},"2":{"conn":"conn","username":"vishal","password":"vishal"}}
logins={}
userobj={}


def findDict(dictn,dict1,key):
    try:
        keys= dict1.keys()
        dict1= dict1.get(keys[0])
        if(len(users)!=0):
            for data in dictn.values():
                if(dict1[key]==data[key]):
                    return keys
        return "n"
    except:
        pass
   
def addUsers(conn,username):
    try:
        usersCount=len(logins)+1
        newUsr={str(usersCount):{"username":username}}
        newuserobj={username:conn}
        if(findDict(logins, newUsr,"username") =="n"):
            logins.update(newUsr)
            userobj.update(newuserobj)
            print "User added: ",logins        
    except:
        pass
def sendMsg(conn,msg):
    try:
        conn.send(msg)
    except:
        pass
        
def validateLogin(data):
    try:
        data=data["login"]
        for ud in users:
            ud=users[ud]
            if(data["username"]==ud["username"] and data["password"]==ud["password"]):
                print "Login Success"
                return True
    except Exception as ex:
        print ex
            
def register(data):
    try:
        for d in users.keys():
            print data[d]
        print data
    except:
        pass 

def processData(conn,data):
    try:
        if(data!=""):
            data=data.replace("'", "\"")
            data=json.loads(data)
            if("login" in data.keys()):
                if(validateLogin(data)):
                    sendMsg(conn, "loginSuccess")
                    dt=data["login"]
                    addUsers(conn,dt["username"])
                    
            elif("register" in data.keys()):
                register(data)   
            elif("view" in data.keys()):
                lg={"userlist":logins}
                sendMsg(conn, str(lg))  
            elif("user" in data.keys()):
                lg={"useravail":"yes"}
                sendMsg(conn, str(lg))  
            elif("usermsg" in data.keys()):
                print data
                msgdata={"receive":data["usermsg"],"sender":data["sender"],"receiver":data["usr"]}
                getConn=userobj[data["usr"]]
                sendMsg(getConn, str(msgdata))
    except:
        pass

def clientthread(conn):
    conn.send('connected') 
    try:
        while True:        
            data = conn.recv(1024)
            processData(conn,data)
            if not data:
                break
    except Exception as ex:
        print ex
    conn.close()

                 
                 
while True:
   conn, addr = s.accept()    
   print 'Got connection from', addr
   thread.start_new_thread(clientthread ,(conn,))
    

print users
    

s.close()


