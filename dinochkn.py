
totalchicken = 20.0 
dailychicken = 1.0
day = 1
while totalchicken >= dailychicken:

    if day == 7:   
        print(f"Day {day}: Stomach ache! He didn't eat anything.")
    elif day == 1:
      totalchicken -= dailychicken
      print(f"Day {day}: Ate {dailychicken:.2f} pounds of fried chicken. Remaining: {totalchicken:.2f} pounds.")   
      
    else:
        dailychicken += 0.05 
        totalchicken -= dailychicken
        print(f"Day {day}: Ate {dailychicken:.2f} pounds of fried chicken. Remaining: {totalchicken:.2f} pounds.")
        
    day += 1
print(f"On {day} days to run out of fried chicken.")
if day == 16:
  print("blahblah")  