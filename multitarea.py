import threading
import time

def sing():
    for i in range(5):
        print("Canto....")
        time.sleep(2)


def dancing():
    for i in range(5):
        print("Bailo....")
        time.sleep(2)


def main():
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dancing)
    t1.start()
    t2.start()


if __name__ == '__main__':

    main()