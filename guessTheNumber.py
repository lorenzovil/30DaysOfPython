import random 

print("HELLO WELCOME GUESS THE NUMBER")

choose= int(input("choose dificulty 1 easy 2 hard : ")) 

if choose == 1 :
   select_number1 = random.randint(1,100)
    
elif choose == 2 :
   select_number1 = random.randint(1,1000)

else :
  print ("wrong number entering to easy mode")
  select_number1 = random.randint(1,100)

attempts = 0 

while True :
  guess = int(input("guess the number : "))
  attempts += 1

  if attempts == 10 :
    print("you LOOSE ")
    print("too meny attempts")
    break
 
  if select_number1 > guess :
   print ("too low try again ")
  elif select_number1 < guess :
   print ("number too high try again lol ")
  else : 
   print ("you guess it right the number is ",select_number1)
   print ("you attempts is ", attempts)
   break
    
  
