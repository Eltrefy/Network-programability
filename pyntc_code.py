#code for saving running configuration using pyntc
import json
from pyntc import ntc_device as ntc
ios_device = ntc(host='192.168.1.100', username='cisco123',
                 password='cisco123', device_type='cisco_ios_ssh', secret="cisco")#secret is for enable password ||secret
mytxt = open(
    r"E:\New folder\New folder\Automation\cisco _programming\my_pyntc2.txt", "w") #
writerr = ios_device.running_config
mytxt.write(writerr)       
