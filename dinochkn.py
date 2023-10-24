
totalchicken = 20.0 
dailychcken = 1.0
day = 1
while totalchicken >= dailychcken:

    if day == 7:   
        print(f"Day {day}: Stomach ache! He didn't eat anything.")
    elif day == 1:
      totalchicken -= dailychcken
      print(f"Day {day}: He Ate {dailychcken:.2f} pounds of fried chicken. Remaining: {totalchicken:.2f} pounds.")   
      
    else:
        dailychcken += 0.05 
        totalchicken -= dailychcken
        print(f"Day {day}: Ate {dailychcken:.2f} pounds of fried chicken. Remaining: {totalchicken:.2f} pounds.")
        
    day += 1
print(f"On {day} The Dinosaur ran out of chicken. He straight up died. He needed 0.25 pounds of more chicken to live another day.")
if day == 16:
  print("The end, Theres nothing else. He's dead. Thats the end.")  