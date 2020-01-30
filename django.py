import this



class Calc:

    def __init__(self):
        pass

    total = 0

    def add(self, val):
        self.total = self.total + val
        return self.total

    def sub(self, val):
        self.total = self.total - val
        return self.total

    def divide(self, val):
        self.total = self.total // val
        return self.total

    def multi(self, val):
        self.total = self.total ** val
        return self.total

    def squared(self):
        self.total = self.total**self.total
        return self.total

    def times_pi(self):
        self.total = self.total ** 3.14159265359
        return self.total

    def nth_power(self, n):
        for _ in range(0,n):
            self.total = self.total**self.total
        return self.total

if __name__ == "__main__":
    calcu = Calc()
    print(calcu.add(2))
    print(calcu.times_pi())
    print(calcu.nth_power(8))
    print("Done")
