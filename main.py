import sys
import win32gui
import win32process
import psutil
import time
from datetime import datetime
import signal
from pynput.mouse import Controller

mouse = Controller()
before = mouse.position
start = datetime.today()
count = 0
table = {}
strt_time = time.time()


def handler(signum, frame):
    print(table)
    sys.exit()


signal.signal(signal.SIGINT, handler)


if __name__ == '__main__':
    while True:
        try:
            if (time.time() - strt_time) > 1:
                pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())
                p = str(psutil.Process(pid[-1]).name()) + " pid: " + str(pid[-1])
                current = mouse.position
                if before != current:
                    try:
                        tmp = table.get(p) + datetime.today() - start
                        table[p] = tmp
                    except TypeError:
                        tmp = datetime.today() - start
                        table[p] = tmp
                    start = datetime.today()
                    before = current
                    strt_time = time.time()
        except ProcessLookupError:
            pass
        except ValueError:
            pass
