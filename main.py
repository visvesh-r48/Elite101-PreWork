
def chatbot():
  print("Hello, welcome to the ChatBot.\n")
  name = input("Please enter your name: \n")
  age = input("Please enter your age: \n")
  print(f"Nice to meet you {name}. I am happy to help you with your needs.\n")
  print("Please choose from the following options:\n")
  print("1. Option 1\n2. Option 2\n3. Option 3\n4. Exit ChatBot")
  choice = int(input("Enter the choice number: "))

  if(choice == 4):
    print("Thank you for using ChatBot. Goodbye.")
    exit()

chatbot()

