income=int(input("Enter your monthly income:"))
expense=int(input("Enter your monthly expense:"))
monthlysaving=income-expense
projsaving=round(monthlysaving*12+(monthlysaving*12*0.05))
print(f"Your monthly savings are ${monthlysaving}.")
print(f"Projected savings after one year, with interest, is: ${projsaving}.")
