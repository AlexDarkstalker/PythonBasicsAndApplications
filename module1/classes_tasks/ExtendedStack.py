class ExtendedStack(list):
    def sum(self):
        sum1 = self.pop()
        sum2 = self.pop()
        self.append(sum1 + sum2)

    def sub(self):
        sum1 = self.pop()
        sum2 = self.pop()
        self.append(sum1 - sum2)

    def mul(self):
        sum1 = self.pop()
        sum2 = self.pop()
        self.append(sum1 * sum2)

    def div(self):
        sum1 = self.pop()
        sum2 = self.pop()
        self.append(sum1 // sum2)
