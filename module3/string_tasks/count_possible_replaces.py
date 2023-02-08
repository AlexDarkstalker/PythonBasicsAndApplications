class ImpossibleError(ValueError):
    pass


def count_replacements(string, to_replace, replacement):
    if len(to_replace) == 1:
        if not string.__contains__(to_replace):
            return 0
        else:
            if to_replace == replacement:
                raise ImpossibleError()
            else:
                return 1
    else:
        count_rep = 0
        while string.count(to_replace) > 0:
            count_rep += 1
            if count_rep > 1000:
                raise ImpossibleError
            string = string.replace(to_replace, replacement)
        return count_rep


input_string = input()
input_to_replace = input()
input_replacement = input()
try:
    print(count_replacements(input_string, input_to_replace, input_replacement))
except ValueError:
    print("Impossible")


