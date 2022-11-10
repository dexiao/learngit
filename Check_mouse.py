from pymouse import PyMouse
import time
if __name__ == '__main__':
    m = PyMouse()
    time.sleep(10)
    print(m.position())
    lis = m.position()
    m.click(lis[0], lis[1])
    times = 0
    print ("start")
    while times < 60:
        m.click(lis[0], lis[1])
        time.sleep(180)
        print("clicked :", times)
        times += 1
        