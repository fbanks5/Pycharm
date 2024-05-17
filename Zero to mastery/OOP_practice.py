
class PlayerCharacter:
    # Class object attribute
    membership = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')
        return 'done'

    def shout(self):
        print(f'my name is {self.name} and my age is {self.age}')
        print('shout')
        return 'done'

    @classmethod
    def new_member(cls, name, age):
        return cls('Fella', 3)

    @staticmethod
    def adding_things(num1, num2):
        return num1 + num2


player1 = PlayerCharacter('Harry', 50)
player2 = PlayerCharacter('Peter', 21)
player3 = PlayerCharacter('Jim', 15)
player4 = PlayerCharacter.new_member('Fella', 3)

print(player1.name, player1.age)
print(player2.name, player2.age)
print(player3.name, player3.age)
print(player4.name, player4.age)
# player1.shout()
# player1.run()
