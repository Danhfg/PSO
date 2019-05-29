from threading import Thread
from multiprocessing import Process

def one(): import main
def two(): import teste3
def three(): import tk3


Thread(target=one).start()
Thread(target=two).start()
Thread(target=three).start()