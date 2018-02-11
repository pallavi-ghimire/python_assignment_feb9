class Upper:
    def get_string(self):
        self.str = input("Enter a string: ")

    def print_string(self):
        print(self.str.upper())


U = Upper()
str = U.get_string()
U.print_string()


class email:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def em(self):
        print(self.fname.lower() + self.lname.lower() + "@gmail.com")


firstn = input("Enter first name: ")
lastn = input("Enter last name: ")
e = email(firstn, lastn)
print(e.em())
