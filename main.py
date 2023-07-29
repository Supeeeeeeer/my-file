def sayHi():
  print("Hi!")
def sayBye():
  print("bye!")
a = input("Select function:Say Hi(print 'hi'), Say Bye(print 'bye')")
if a == "hi":
  sayHi()
elif a == "bye":
  sayBye()
else:
  print("Invalid function. Try again")
