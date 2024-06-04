class MyClass():
    def get_name(self):
       self.str = input("What is your name? ")

    def print_name(self):
        print(self.str.upper())


in_out_string = MyClass()
in_out_string.get_name()
in_out_string.print_name()

