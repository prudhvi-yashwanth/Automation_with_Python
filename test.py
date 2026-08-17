list_of_values = [2,2,8,9,6,1,9,6,7,5,7,1,0,0]

unique_values = set(list_of_values)
repeted_values = []
print(unique_values)

for value in unique_values:
  if list_of_values.count(value) > 1:
    repeted_values.append(value)

print(f"Repeated values: {repeted_values}")


# #####################################################################

user_data = input("Enter the input to check for palindrome: ")


def check_palindrome():
  if not isinstance(user_data, str):
    return("Error: Invalid input. Try with string!")
  
  converted_text = user_data.lower()
  reversed_text = user_data[::-1]
  if(converted_text == reversed_text):
    return("The string is a palindrome")
  else:
    return("Not a palindrome. Try with new one")

result = check_palindrome()
print(result)

#######################################################################

user_input1 = input("Enter the  1st number to swap:  ")
user_input2 = input("Enter the 2nd number to swap:  ")

def swapping_numbers(num1,num2):
  try:
    num1 = int(num1)
    num2 = int(num2)
  except ValueError:
    raise ValueError("Failed to convert the input into integer. Please enter only integer")
  

  num1 = num1 + num2
  num2 = num1 - num2
  num1 = num1 - num2
  return num1, num2

num1, num2 = swapping_numbers(user_input1, user_input2)
print(f"Numbers after swapped are: {num1}, {num2}")

