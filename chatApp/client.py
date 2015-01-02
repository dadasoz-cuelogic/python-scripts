#!/usr/bin/python           

import socket    
import thread  
import threading
from threading import Thread
import time   
import json  
s = socket.socket()         
host = "192.168.10.27"      
port = 1234                 
s.connect((host, port))
currentUser=""
current=None
me=None


def writeFile(str):
    text_file = open("Output.txt", "w")
    text_file.write(str)
    text_file.close()

def readFile():
    text_file = open("Output.txt", "r")
    lines = text_file.read().split(',')
    if(len(lines)>0):
        return lines[0]
    else:
        return ""
    text_file.close() 
    
writeFile("")
    
def viewUsers(data):
    data=data["userlist"]
    print '-'*20," Online Users ",'-'*20
    i=1
    for user in data.keys():
        user=data[user]
        if(user["username"]!=me):
            print i,". ",user["username"]
            i=i+1
        
def startReply(msg,usr):
    if msg!=None:
        msgdata={"usermsg":msg,"usr":usr,"sender":me}
        sendMsg(s, str(msgdata))
    while True:
        inp=raw_input("Me : ")
        if(inp=="end"):
            break
        else:
            msgdata={"usermsg":inp,"usr":usr,"sender":me}
            sendMsg(s, str(msgdata))
        
def printMsg(data):
    print data["sender"]," : ",data["receive"]     
    currentUser =  data["sender"]
    writeFile(currentUser)


def processData(data):
    data=data.replace("u'", "\"")
    data=data.replace("'", "\"")
    data=json.loads(data)
    if("userlist" in data.keys()):
        viewUsers(data)
    elif("receive" in data.keys()):
        printMsg(data) 
        #thread.start_new_thread(writehread ,(s,))      

def clientthread(conn):
    
    while True:        
        data = conn.recv(1024)
        processData(data)
    conn.close()

def writehread(s):    
    startReply("Test")

msg=s.recv(1024)

def sendMsg(conn,msg):
    conn.send(msg)

    

if(msg=="connected"):
    print("Plese select option:")
    print("1.Login:")
    print("2.Register")
    print("3.Exit")
    print("-"*50)    
    inp=raw_input("Please enter your choice: ")
    if(inp=="1"):
        username=raw_input("Please enter username: ")
        password=raw_input("Please enter password: ")
        logindata={"login":{"username":username,"password":password}}
        sendMsg(s, str(logindata))
        msg=s.recv(1024)
        if(msg=="loginSuccess"):
            me=username
            thread.start_new_thread(clientthread ,(s,))
            print '-'*50
            print("You have been logged in successfully!")
            print '-'*50
            print("Please select option: ")
            print("1.View All")
            print("2.Exit")
            inp=raw_input("Please enter your choice: ")
            if(readFile()==""):
                if(inp=="1"):
                    current="viewall"
                    msgdata={"view":"viewAll"}
                    sendMsg(s, str(msgdata))
                    inp=raw_input("Plese select User to chat with: ")
                    if(readFile()==""):
                        currentUser=inp
                        msgdata={"user":inp}
                        sendMsg(s, str(msgdata))
                        print ("-"*18)+currentUser+("-"*18)
                        while(True):
                            inp=raw_input("Me : ")
                            if(inp=="end"):
                                break
                            else:
                                msgdata={"usermsg":inp,"usr":currentUser,"sender":me}
                                sendMsg(s, str(msgdata))
                    else:
                        startReply(inp,readFile())  
            else:
                startReply(inp,readFile())  
                        
                
                
                
                
                
            
                        