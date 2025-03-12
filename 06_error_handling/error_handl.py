file = open('youtube.text', 'w')

try:
    file.write('chao aur code')
finally:
    file.close()


with open('youtube.text', 'w') as file:
    file.write('chai aur code')    


