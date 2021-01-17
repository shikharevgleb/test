import random as rnd
input("отгадай число от 1-100\n")
x1 = int(input("сколько попыток тебе нужно\n"))
print("Я загадал\n")
while(1,100):
  def number(number):
   if player_number(rnd.randit(1,100)) > computer(rnd.randit(1,100)):
       print("больше, давай меньше")
   elif plaer_number(rnd.randit(1,100)) < computer(rnd.randit(1,100)):
       print("Мало,давай меньше")
   elif player_number(rnd.randit(1,100)) == computer(rnd.randit(1,100)):
       print("молодец угадал")
  break