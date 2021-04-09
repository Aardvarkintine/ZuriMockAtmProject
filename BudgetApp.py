# Task Title: Python: Classes and Objects
# Create a Budget class that can instantiate objects based on different budget categories like food, clothing, and entertainment. These objects should allow for
# 1.  Depositing funds to each of the categories
# 2.  Withdrawing funds from each category
# 3.  Computing category balances
# 4.  Transferring balance amounts between categories

# Push your code to GitHub, and submit the repo link.

class Budget:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, amountToDeposit):
        self.balance += amountToDeposit

        response = '===============================\n'
        response += f'Your new balance is: {self.balance} in {self.name} budget'
        return response

    def withdrawal(self, amountToWithdraw):
      if self.balance < amountToWithdraw:
        response = '===============================\n'
        response += 'Insufficient Funds \n'
        response += 'Transaction not successful!'

        return response

      else:
        self.balance -= amountToWithdraw

        response = '===============================\n'
        response += 'Transaction Successful\n'
        response += f'Your new balance is {self.balance} in {self.name}'

        return response

    def getBalance(self):
      response = '===============================\n'
      response += f'Your balance for {self.name} is {self.balance}'

      return response
    
    def fundsTransfer(self, amountToTransfer, categoryObject):
      if(self.balance < amountToTransfer):

        response = '===============================\n'
        response += 'Transaction not successful!'
        response += 'Insufficient Funds \n'

        return response
      
      else:
        self.balance -= amountToTransfer
        categoryObject.balance += amountToTransfer
        
        response = '================================== \n'
        response += 'Transaction Successful\n'
        response += f'Your new balance is {self.balance} in {self.name} \n'
        response += f'Your new balance is {categoryObject.balance} in {categoryObject.name}'

        return response



food = Budget('Food')
clothing = Budget('Clothing')
entertainment = Budget('Entertainment')

print(food.deposit(3000))
print(clothing.deposit(4000))
print(entertainment.deposit(5000))

print(food.withdrawal(1200))
print(clothing.withdrawal(2300))
print(entertainment.withdrawal(3400))

print(food.getBalance())
print(clothing.getBalance())
print(entertainment.getBalance())

print(food.fundsTransfer(500, clothing))
print(clothing.fundsTransfer(600, entertainment))
print(entertainment.fundsTransfer(700, food))


