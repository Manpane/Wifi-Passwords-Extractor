'''
Extracts all saved wifi network's SSID and password from windows machine.
'''
import subprocess
def getSSIDs():
    process = subprocess.Popen("netsh wlan show profiles",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    output,_ = process.communicate()
    return [ line.split(":")[-1].strip() for line in output.decode().split("\n") if "All User Profile"  in line]

def getPassword(SSID):
    process = subprocess.Popen(f'netsh wlan show profile "{SSID}" key=clear',shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    output,_ = process.communicate()
    password = [ line.split(":")[-1].strip() for line in output.decode().split("\n") if "Key Content"  in line]
    if len(password): return password[0]
    else: return ""

PASSWORDS = {ssid:getPassword(ssid) for ssid in getSSIDs()}

#Do whatever you want to with the ssid and passwords
for key in PASSWORDS.keys():
    print(key,":",PASSWORDS[key])

