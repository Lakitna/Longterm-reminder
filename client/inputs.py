import digitalRead
import analogRead


but_A = digitalRead.Button(13, 3) # (pin, readings per poll)
but_B = digitalRead.Button(2, 3) # (pin, readings per poll)
ldr_A = analogRead.Analog(0, 5) # (pin, readings per poll)

def poll():
    but_A.poll()
    if but_A.up():
        but_A_up()
    if but_A.down():
        but_A_down()

    but_B.poll()
    if but_B.up():
        but_B_up()
    if but_B.down():
        but_B_down()

    if ldr_A.poll_period(300): # in seconds
        if ldr_A.val_period < 100:
            print("LDR: %d - Night mode" % ldr_A.val_period)
        else:
            print("LDR: %d - Day mode" % ldr_A.val_period)



def but_A_down():
    print("Av")
    print(ldr_A.val)

def but_A_up():
    print("A^")


def but_B_down():
    print("Bv")

def but_B_up():
    print("B^")
