
def f(player1, player2):
    value1 =0
    value2 =0
    for x in player1:
         if x == "A" or x=="K" or x=="Q" or x=="J" or x=="T" :
             value1 += 10
         else:
             value1 += int(x)
    for x in player2:
         if x == "A" or x=="K" or x=="Q" or x=="J" or x=="T" :
             value2 += 10
         else:
              value2 += int(x)     
    return  value1> value2
 

#def count( value):       
  #  result =0
   # for x in value:
    #    if x == "A" or x=="K" or x=="Q" or x=="J" or x=="T" :
    #        result +=  10
   #     else:
   #          result = result + int(x)
   #     return result

player1 = input("player1: ")
player2 = input("player2: ")

print(f(player1,player2))




