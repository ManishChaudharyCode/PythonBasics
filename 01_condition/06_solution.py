distance = 76

if distance < 3:
    transpot = "Walk"
elif distance <= 15:
    transpot = "Bike"
else:
    transpot = "car"

print("AI recommends you the transport of: ", transpot)            
    