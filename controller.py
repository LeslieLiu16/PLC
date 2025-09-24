from pycomm3 import LogixDriver

def left_run():
    with LogixDriver('192.168.0.40') as plc:
        print(plc.read('Program:MainProgram.left_manual_button'))
        time=0
        while time<=300:
            plc.write('Program:MainProgram.left_manual_button',1)
            time+=1
        print(plc.read('Program:MainProgram.left_manual_button'))

def right_run():
    with LogixDriver('192.168.0.40') as plc:
        print(plc.read('Program:MainProgram.right_manual_button'))
        time=0
        while time<=300:
            plc.write('Program:MainProgram.right_manual_button',1)
            time+=1
        print(plc.read('Program:MainProgram.right_manual_button'))

