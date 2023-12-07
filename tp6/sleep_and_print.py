import time

def sleep_and_print():
    count = 0
    while count != 11:
        print(count)
        time.sleep(0.5)
        count += 1
sleep_and_print()
sleep_and_print()