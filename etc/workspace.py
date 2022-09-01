import threading
import _thread


stack = 0

while 1:
    # Called impatient calculator
    timer = threading.Timer(10.0, _thread.interrupt_main)
    try:
        timer.start()
        operand_1 = int(input("Choose a number:\n"))
        operand_2 = int(input("Choose another one:\n"))
        operation = input("Choose an operation:\n\tOptions are: + , - , * or /.\n\tWrite 'exit' to finish.\n")
    except KeyboardInterrupt as K:
        print("Time out!!!🤯")
        break
    
    timer.cancel()
    
    if operation.lower() == "exit":
        break
    elif operation in ["+","-","*","/"]:
        print("Result:", eval(f"{operand_1}{operation}{operand_2}"))
    else:
        stack += 1
        if stack == 3:
            print("The calculator be stopped!!🤯")
            break
        print(f"Not in options! Try again from the first!🤨 ({stack}/3)")