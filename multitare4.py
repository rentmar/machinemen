import threading
import time

g_num = 0


def test1(num):
    global g_num
    for i in range(num):
        g_num += 1
    print("----test1:g_num=%d" % g_num)


def test2(num):
    global g_num  # Debido a que desea modificar el valor de g_num, debe establecerlo como una variable global
    for i in range(num):
        g_num += 1
    print("--test2: g_num=%d" % g_num)


def main():
    # Pasar una tupla con el parámetro args al pasar parámetros
    t1 = threading.Thread(target=test1, args=(1000000,))  # Cuando los datos entrantes son demasiado grandes, habrá competencia de recursos
    t2 = threading.Thread(target=test2, args=(1000000,))  # Recorre 1 millón de veces
    t1.start()
    t2.start()
    time.sleep(3)
    print("----main: g_num= %d" % g_num)

if __name__ == '__main__':
    main()
