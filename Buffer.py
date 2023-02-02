class Buffer:
    buf_list = []

    def __init__(self):
        self.buf_list = []

    def add(self, *a):
        list_args = list(a)
        list_buffer_length = len(self.buf_list)
        if list_buffer_length + len(list_args) >= 5:
            self.buf_list += list_args[:5 - list_buffer_length]
            print(sum(self.buf_list))
            self.buf_list.clear()
            self.add(*tuple(list_args[5 - list_buffer_length:]))
        else:
            self.buf_list += list_args

    def get_current_part(self):
        return self.buf_list


buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part() # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part() # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part() # вернуть [1]
