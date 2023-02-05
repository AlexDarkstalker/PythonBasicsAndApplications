class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, val):
        if val < 0:
            raise NonPositiveError("nonpositive value")
        else:
            super().append(val)
