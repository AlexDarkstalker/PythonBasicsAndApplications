import itertools


def primes():
    k = 1
    while True:
        k += 1
        print(*range(1, int(k**0.5) + 1))
        count_delimeters = 0
        for i in range(1, int(k**0.5) + 1):
            if k % i == 0:
                count_delimeters += 1
                if count_delimeters > 2:
                    break
        if count_delimeters == 1:
            yield k


print(list(itertools.takewhile(lambda x: x <= 31, primes())))
