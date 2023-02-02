import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def append(self, val):
        super().append(val)
        super().log(val)


x = LoggableList()
x.append(7)
