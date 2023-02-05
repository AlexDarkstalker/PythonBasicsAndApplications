import datetime


inp_date = datetime.date(*map(int, input().split()))
days = int(input())
delta = datetime.timedelta(days)
result_date = inp_date + delta
print(result_date.year, result_date.month, result_date.day)
