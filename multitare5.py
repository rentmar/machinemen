import threading
import time

g_num = 0
lock = threading.Lock()  # Crea un mutex


def test1(num):
    global g_num
    lock.acquire()  # Bloqueado
    for i in range(num):
        g_num += 1
    lock.release()  # Cuando se ejecuta el programa, suelte
    print("----test1:g_num=%d" % g_num)


def test2(num):
    global g_num  # Debido a que desea modificar el valor de g_num, debe establecerlo como una variable global
    with lock:  # Operación de bloqueo de exclusión mutua, cuando se ejecuta el bloque de código interno de con, se liberará automáticamente
        for i in range(num):
            g_num += 1

    print("--test2: g_num=%d" % g_num)


def main():
    """Al pasar parámetros, utilice el parámetro args para pasar una tupla"""
    thread_list = []  # Crear grupo de subprocesos
    t1 = threading.Thread(target=test1, args=(1000000,))
    thread_list.append(t1)
    t2 = threading.Thread(target=test2, args=(1000000,))

    thread_list.append(t2)
    for t in thread_list:
        t.start()
        t.join()  # Deje que el hilo secundario termine primero y el hilo principal se ejecute al final

    print("----main: g_num= %d" % g_num)


if __name__ == '__main__':
    main()
