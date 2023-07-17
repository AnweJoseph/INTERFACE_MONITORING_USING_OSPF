from netmiko.exceptions import NetmikoTimeoutException
from netmiko.exceptions import NetmikoAuthenticationException
from netmiko.exceptions import SSHException
from netmiko.exceptions import AuthenticationException
from netmiko.exceptions import ReadTimeout
import schedule
import time
from netmiko import ConnectHandler
import json
import sys

with open('device_ip') as DEVICE_IP:
    for ip in DEVICE_IP:
            
        RTR = {
                'device_type': 'cisco_ios',
                'host': ip,
                'username': 'anwea',
                'password': '02anwe05',
                'secret': '02anwe05'}
                
        net_connect = ConnectHandler(**RTR)
        
def status():
    
    print("Checking ospf status on ", ip)
            
    try:    
        net_connect.enable()
                
    except NetmikoTimeoutException:
        print('Device unreachable')
        #continue
                
    except NetmikoAuthenticationException:
        print('Authentication Failed')
        #continue
                
    except SSHException:
        print('Error reading SSH protocol banner')
        #continue
                
    except AuthenticationException:
        print('Failed Authentication Exception')
        #continue
    except ReadTimeout:
        print('Netmiko ReadTimeout')
        #continue
                
                
    output = net_connect.send_command('sh ip ospf nei', use_textfsm=True)
    #print(json.dumps(output, indent = 2))        
                                        
    for ospf in output:
        if ospf['address'] == '1.1.1.1' and ospf['state'] == 'FULL/  -':
            print('OSPF IS UP')
            time.sleep(2)
                    
                   
schedule.every(5).seconds.do(status)

while True:
    
    schedule.run_pending()
    time.sleep(1)

