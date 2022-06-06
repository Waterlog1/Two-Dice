from random import randint

class Die():

	def __init__(self,sides=6):
		self.sides=sides

	def roll_dice(self):
		return randint(1,self.sides)
    
    

d6=Die()
d6=Die()

dice1=[]
for roll_num in range(1):
	result= d6.roll_dice()
	dice1.append(result)

dice2=[]
for roll_num in range(1):
	result= d6.roll_dice()
	dice2.append(result)



print(f'Record each roll of 6 sided dice:{dice1}')
print(f'Record each roll of 6 sided dice:{dice2}')
print(f"{dice1} + {dice2}")