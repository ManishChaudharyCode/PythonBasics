password = "hy123"

#if len(password)< 6:
 #   strength = "Weak"

#elif len(password)<=10:
 #   strength ="Medium"

#else:
  #  strength = "Strong"

#print("password strength is: ", strength)            

password_length = len(password)

if password_length < 6:
    strength = "Weak"