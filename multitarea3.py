import threading
import time

class Test(threading.Thread):

    def run(self):
        for i in range(5):
            time.sleep(1)
            print("---- im %d= ----" %i)
        self.login()
        self.register()    



    def login(self):
        print("Inicio de sesion")


    def register(self):
        print("Registro")



if __name__ == '__main__':
    t = Test()
    t.start()