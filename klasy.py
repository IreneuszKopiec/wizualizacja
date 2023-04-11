class Fruit:
    def init(self, color, weight):
        self.color = color
        self.weight = weight


class Apple(Fruit):
    def init(self, color, weight):
        super().init(color, weight)

    def isfresh(self):
        if self.color == "red" or self.color == "green":
            return True
        else:
            return False


class Banana(Fruit):
    def init(self, color, weight):
        super().init(color, weight)

    def isfresh(self):
        if self.color == "yellow":
            return True
        else:
            return False


class Orange(Fruit):
    def init(self, color, weight):
        super().init(color, weight)

    def isfresh(self):
        if self.color == "orange":
            return True
        else:
            return False


apple = Apple()
apple.init("red", 20)
print(apple.isfresh())


class Account:
    def init(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Niewystarczajace srodki")
        else:
            self.balance -= amount

    def transfer(self, amount, to_account):
        if amount > self.balance:
            print("Niewystarczajace srodki")
        else:
            self.withdraw(amount)
            to_account.deposit(amount)


class PrivateAccount(Account):
    def init(self, account_number, balance=0, salary=0):
        super().init(account_number, balance)
        self.salary = salary

    def pay_salary(self):
        self.deposit(self.salary)


class FirmAccount(Account):
    def init(self, account_number, balance=0, tax_number=None):
        super().init(account_number, balance)
        self.tax_number = tax_number

    def pay_tax(self, amount):
        self.withdraw(amount)
        print("Platnosc podatku w wysokosci {} na konto {}".format(amount, self.tax_number))


a1 = Account()
a1.init(123456789, 3500)
print("--------")
print(a1.balance)
print("--------")
a1.deposit(2000)
print(a1.balance)
print("--------")
a1.withdraw(900)
print(a1.balance)
print("--------")
a2 = Account()
a2.init(987654321, 2500)
print(a2.balance)
print("--------")
a1.transfer(1000, a2)
print(a1.balance)
print(a2.balance)
a1.transfer(900000, a2)
print("--------")
a3 = PrivateAccount()
a3.init(987123654, 10000, 4400)
a4 = PrivateAccount()
a4.init(543216789, 19000, 3300)
print(a3.balance)
print(a3.salary)
print(a4.balance)
print(a4.salary)
print("--------")
a3.pay_salary()
a4.pay_salary()
print(a3.balance)
print(a4.balance)
print("--------")
a5 = FirmAccount()
a5.init(987123654, 10000, 84758027580347580)
a6 = FirmAccount()
a6.init(543216789, 19000, 83485903885934859)
print(a5.balance)
print(a6.balance)
print("--------")
a5.pay_tax(2000)
a6.pay_tax(1500)
print("--------")
print(a5.balance)
print(a6.balance)
print("--------")

class Romanian:
    def init(self, value):
        self.value = value

    def to_roman(self):
        roman_numeral_map = (('M', 1000), ('CM', 900), ('D', 500),
                             ('CD', 400), ('C', 100), ('XC', 90),
                             ('L', 50), ('XL', 40), ('X', 10),
                             ('IX', 9), ('V', 5), ('IV', 4),
                             ('I', 1))
        num = self.value
        result = ''
        while num > 0:
            for roman, integer in roman_numeral_map:
                if num >= integer:
                    result += roman
                    num -= integer
                    break
        return result

    def to_arabic(self):
        roman_numeral_map = (('M', 1000), ('CM', 900), ('D', 500),
                             ('CD', 400), ('C', 100), ('XC', 90),
                             ('L', 50), ('XL', 40), ('X', 10),
                             ('IX', 9), ('V', 5), ('IV', 4),
                             ('I', 1))
        roman_numeral = self.value
        i = result = 0
        while i < len(roman_numeral):
            for roman, integer in roman_numeral_map:
                if roman_numeral[i:i+len(roman)] == roman:
                    result += integer
                    i += len(roman)
                    break
        return result

    def add(self, other):
        return Romanian(self.to_arabic()+other.to_arabic().to_roman())

    def sub(self, other):
        return Romanian(self.to_arabic()-other.to_arabic().to_roman())

    def mul(self, other):
        return Romanian(self.to_arabic()*other.to_arabic().to_roman())

    def str(self, other):
        return self.to_roman()


r1 = Romanian()
r1.init('MCMXX')
print(r1.to_arabic())
print("--------")
r2 = Romanian()
r2.init(1920)
print(r2.to_roman())
print("--------")
