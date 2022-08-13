
#you will have to change the username if u want
username = input("Enter username:")

if username == "password": #<-- change username here
  input("success")
  #put whatever u want here
else:
  try2 = input("Press Enter To Try Agian")
  print("Trys Remaing:1")
if try2 == "":
  password2 = input("Enter Password:")
if password2 == "bob": #<-- change username here
  input("success")
  #put whatever u want here
  
else:
  print("Access Denied")
  quit()

  
  
