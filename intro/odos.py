class Odometer(object):
    def __init__(self):
        self.mileage = 0

    def travel(self, miles):
        self.mileage += miles


class PalindromeOdometer(Odometer):
    def is_palindrome(self):
        return reverse_string(str(self.mileage)) == str(self.mileage)


if __name__=='__main__':
    odometer = PalindromeOdometer()
    print(odometer)
    odometer.travel(152251)
    print(odometer.is_palindrome())
