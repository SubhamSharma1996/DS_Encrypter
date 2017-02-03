#developed by Subham Sharma
from random import randint
from easygui import *
import smtplib

MAX_KEY_SIZE = 26
sm=[' ','!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[',']','/','^','_','`','{','|','}','~']
hd=['p','I','o','Y','U','r','T','w','E','q','L','k','J','G','h','D','f','A','s','M','b','N','C','v','Z','x','#','$','^','%','*',')','&','!','@','|',':',';','?','>']   
'''def getMessage():
    print('Enter your message:')
    msg=raw_input()
    return msg'''
def getKey():
    key = 0
    key= randint(1,26)
    return key
def getKey1():
    key1=0
    key1 = randint(0,38)
    return key1

def getTranslatedMessage(message):
    l=len(message)
    message1=''
    if l%2==0:
        mid=l/2
    else:
        mid=int(l/2)
    
    for i in range(0,40):
        if message[mid]==hd[i]:
            rkey1=i
    
    for j in range(0,40):
        if message[mid-1]==hd[j]:
            rkey=j

    
    key = -rkey
    key1 = -rkey1
    trans= ''
    for g in range(0,mid-1):
        message1 +=message[g]
    for z in range(mid+1,l-1):
        message1 +=message[z]
        
    for symbol in message1:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                        num -= 26
                elif num < ord('a'):
                        num += 26
                
            trans+= chr(num)
        elif symbol.isdigit():
            num1 =int(symbol)
            num1 +=key
            while num1>9:
                num1 = num1 - 9
            while num1<0:
                num1 = num1 + 9
            trans+= str(num1)
        elif symbol=="'":
            trans+= "\n"   
        else:
            for i in range(0,33):
                if symbol==sm[i]:
                    num2=i
            num2 +=key1
            while num2 > 33:
                num2=num2-33
            while num2 < 0:
                num2=num2+33
            trans += sm[num2]
    return trans

def TranslateMessage(message, key,key1):
    z=0
    rkey = key
    rkey1 = key1
    key = +key
    key1 = +key1
    translated = ''
    translatedf = ''
    l=len(message)
    if l%2==0:
        mid=l/2
    else:
        mid=int(l/2)
    
    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)
        elif symbol.isdigit():
            num1 =int(symbol)
            num1 +=key
            while num1>9:
                num1 = num1 - 9
            while num1<0:
                num1 = num1 + 9
            translated += str(num1)
        elif symbol=='\n':
            translated += "'"
        else:
            for i in range(0,33):
                if symbol==sm[i]:
                    num2=i

            num2 +=key1
            while num2 > 33:
                num2=num2-33
            while num2 < 0:
                num2=num2+33
            translated += sm[num2]
    if l%2==0:
        mid=l/2
    else:
        mid=int(l/2)
    
    for i in range(0,mid):
        translatedf += translated[i]
    
    translatedf += hd[rkey]
    translatedf += hd[rkey1]
    for j in range(mid,l):
        translatedf += translated[j]
    
    return translatedf
def yahoom(sid,rid,msg,pswd):
    # Specifying the from and to addresses

    u=0
    fromaddr = sid
    toaddrs  = rid

    # Writing the message (this message will appear in the email)

    msg = msg

    # Yahoo Login

    username = sid
    password = pswd

    # Sending the mail  

    server = smtplib.SMTP('smtp.mail.yahoo.com:587')
    server.starttls()
    try:
        server.login(username,password)
    except:
        msgbox(msg='PLEASE ENTER A CORRECT USERNAME AND PASSWORD', title='D-S ENCRYPTER-DECRYPTER', ok_button='OK', image='error.gif')
        u=1
    if u!=1 :
        msgbox(msg='YOUR MAIL HAS BEEN SENT', title='D-S ENCRYPTER-DECRYPTER', ok_button='OK', image='sent.png')
        server.sendmail(fromaddr, toaddrs, msg)
    server.quit()
def gmailm(sid,rid,msg,pswd):
    # Specifying the from and to addresses
    u=0


    fromaddr = sid
    toaddrs  = rid

    # Writing the message (this message will appear in the email)

    msg = msg

    # Yahoo Login

    username = sid
    password = pswd

    # Sending the mail  

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    try:
        server.login(username,password)
    except:
        msgbox(msg='PLEASE ENTER A CORRECT USERNAME AND PASSWORD', title='D-S ENCRYPTER-DECRYPTER', ok_button='OK', image='error.gif')
        u=1
    if u!=1 :
        msgbox(msg='YOUR MAIL HAS BEEN SENT', title='D-S ENCRYPTER-DECRYPTER', ok_button='OK', image='sent.png')
        server.sendmail(fromaddr, toaddrs, msg)
    server.quit()

    


'''print('Do you wish to encrypt or decrypt a message?')
mode=raw_input()
if mode== 'e':
    message= getMessage()
    key= getKey()
    key1= getKey1()
elif mode=='d':
    message= getMessage()
else:
    print('Enter either "e" or "d".')
if mode== 'e':
    print('Your Encrypted text is:')
    print(TranslateMessage(message, key, key1))
elif mode== 'd':
    print('Your Decrypted text is:')
    print(getTranslatedMessage(message))'''
while 1:
    check=boolbox(msg=' WELCOME TO D-S ENCRYPTER-DECRYPTER ', title='D-S ENCRYPTER-DECRYPTER', choices=('ENTER', 'EXIT'), image="LAST.png")
    if check==1:
        check1=boolbox(msg=' SELECT YOUR CHOICE ', title='D-S ENCRYPTER-DECRYPTER', choices=('ENCRYPTER', 'DECRYPTER'), image="CHOICE.png")
        if check1==1:
            
            message=textbox(msg=' ENTER YOUR MAIL FOR ENCRYPTION ', title='D-S ENCRYPTER-DECRYPTER ', text='', codebox=0)
            if not message:
                msgbox(msg='PLEASE  ENTER YOUR MAIL FOR ENCRYPTION ' , title='D-S ENCRYPTER-DECRYPTER', ok_button='OK', image='error.gif')
            else:
                key= getKey()
                key1= getKey1()
                texte=TranslateMessage(message , key, key1)
                try:
                    #msgbox(msg='Encrypted Mail :-  '+  text  , title='D-S ENCRYPTER-DECRYPTER', ok_button='OK', image=None)
                    #textbox(msg='Encrypted Mail :-  ', title='D-S ENCRYPTER-DECRYPTER ', text=texte, codebox=0)
                    codebox(msg='Encrypted Mail :-  ', title='D-S ENCRYPTER-DECRYPTER ', text=texte)
                except:
                    msgbox(msg='PLEASE ENTER A CORRECT TEXT OR TRY AGAIN', title='D-S ENCRYPTER-DECRYPTER', ok_button='OK', image='error.gif')
            check2=boolbox(msg=' SELECT YOUR CHOICE ', title='D-S ENCRYPTER-DECRYPTER', choices=('DECRYPT', 'SEND MAIL'), image="CHOICE.png")
            if check2==1:
                text1=getTranslatedMessage(texte)
                try:
                    codebox(msg='Decrypted Text :-  ', title='D-S ENCRYPTER-DECRYPTER ', text=text1)
                except:
                    msgbox(msg='PLEASE ENTER A CORRECT TEXT OR TRY AGAIN', title='D-S ENCRYPTER-DECRYPTER', ok_button='OK', image='error.gif')
            else:
                check3=boolbox(msg=' SELECT YOUR CHOICE ', title='D-S ENCRYPTER-DECRYPTER', choices=('GMAIL', 'YAHOO'), image="MAIL.png")
                if check3==0:
                    msg = "Enter Your Login Information"
                    title = "Yahoo-Mail"
                    fieldNames = ["User ID", "To", "Message", "Password"]
                    fieldValues = []  # we start with blanks for the values
                    fieldValues = multpasswordbox(msg,title, fieldNames)
                    while 1:
                        if fieldValues == None: break
                        errmsg = ""
                        for i in range(len(fieldNames)):
                            if fieldValues[i].strip() == "":
                                errmsg = errmsg + ('"%s" is a required field.' % fieldNames[i])
                        if errmsg == "": break
                        fieldValues = multpasswordbox(errmsg, title, fieldNames, fieldValues)
                    yahoom(fieldValues[0],fieldValues[1],fieldValues[2],fieldValues[3])
                else:
                    msg = "Enter Your Login Information"
                    title = "G-Mail"
                    fieldNames = ["User ID", "To", "Message", "Password"]
                    fieldValues = []  # we start with blanks for the values
                    fieldValues = multpasswordbox(msg,title, fieldNames)
                    while 1:
                        if fieldValues == None: break
                        errmsg = ""
                        for i in range(len(fieldNames)):
                            if fieldValues[i].strip() == "":
                                errmsg = errmsg + ('"%s" is a required field.' % fieldNames[i])
                        if errmsg == "": break
                        fieldValues = multpasswordbox(errmsg, title, fieldNames, fieldValues)
                    gmailm(fieldValues[0],fieldValues[1],fieldValues[2],fieldValues[3])
        else:
            messagee=enterbox(msg=' ENTER YOUR TEXT FOR DECRYPTION .', title='D-S ENCRYPTER-DECRYPTER ', default='', strip=False,image="DECRYPT.png")
            #textbox(msg=' ENTER YOUR TEXT FOR DECRYPTION ', title='D-S ENCRYPTER-DECRYPTER ', text='', codebox=0)
            if not messagee:
                msgbox(msg='PLEASE ENTER A TEXT FOR DECRYPTION' , title='D-S ENCRYPTER-DECRYPTER', ok_button='OK', image='error.gif')
            else:
                text2=getTranslatedMessage(messagee)
                try:
                    codebox(msg='Decrypted Text :-  ', title='D-S ENCRYPTER-DECRYPTER ', text=text2)
                except:
                    msgbox(msg='PLEASE ENTER A CORRECT TEXT OR TRY AGAIN', title='D-S ENCRYPTER-DECRYPTER', ok_button='OK', image='error.gif')

    
    else:
        sys.exit(0)
