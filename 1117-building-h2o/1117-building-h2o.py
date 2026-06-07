from threading import Semaphore
class H2O:
    def __init__(self):
        self.h = Semaphore(2)
        self.o = Semaphore(0)
    def hydrogen(self, releaseHydrogen):
        self.h.acquire()
        releaseHydrogen()
        if self.h._value == 0:
            self.o.release()
    def oxygen(self, releaseOxygen):
        self.o.acquire()
        releaseOxygen()
        self.h.release()
        self.h.release()