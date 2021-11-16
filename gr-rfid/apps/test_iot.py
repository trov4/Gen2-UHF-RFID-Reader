import aws_interface as iot 
import time


while(True):
    iot.push('1876', "Q245")
    time.sleep(5)
