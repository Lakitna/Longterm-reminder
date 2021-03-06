import digitalRead
import analogRead
from httpUpdate import activeReminders
from reminder import setComplete


but_A = digitalRead.Button(13, 3) # (pin, readings per poll)
but_B = digitalRead.Button(2, 3) # (pin, readings per poll)
ldr_A = analogRead.Analog(0, 3) # (pin, readings per poll)

def poll():
    ldr_A.poll_period(60) # in seconds

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


def but_A_down():
    print("Av %d" % ldr_A.val)
    if len(activeReminders) > 0:
        setComplete( activeReminders[ next(iter(activeReminders)) ] )

def but_A_up():
    print("A^")


def but_B_down():
    print("Bv")

def but_B_up():
    print("B^")
