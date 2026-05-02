# Write a program that takes a string input from the user and prints the total number of characters present in the string.
user_input = input("Enter a String : ")
def count_char(str):
    count = 0
    for i in str:
        count += 1
    print(f"Total number of characters in the String: {count}")
count_char(user_input)

    
    