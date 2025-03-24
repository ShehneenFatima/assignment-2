#1. Print the following pattern using for loop:
#A) 
#**********
#**********
#**********
#**********
for i in range(4):  # Loop for 4 rows
    print("*" * 10)  # Print 10 asterisks in each row
#B)
#1 2 3 4 5 6 7 8 9 10
#2 4 6 8 10 12 14 16 18 20
#3 6 9 12 15 18 21 24 27 30
#4 8 12 16 20 24 28 32 36 40
#5 10 15 20 25 30 35 40 45 50
for i in range(1, 6):  # Loop for rows (1 to 5)
    for j in range(1, 11):  # Loop for columns (1 to 10)
        print(i * j, end=" ")  # Print the product of row and column numbers
    print()  # Move to the next line after each row
#C)
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5
for i in range(1, 6):  # Loop for rows (1 to 5)
    for j in range(1, i + 1):  # Loop for columns (1 to i)
        print(j, end=" ")  # Print numbers in a row
    print()  # Move to the next line after each row
