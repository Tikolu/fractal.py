import fractal
from random import randrange

print("Fractal Screensaver. Click to Exit.")
width = int(input("Width: "))
height = int(input("Height: "))
updatemode = int(input("Update Frequency: "))

d = fractal.display(width, height, True)

while True:
    iterations = randrange(5,25)
    power = randrange(-5,5)
    
    r = randrange(1,8)
    g = randrange(1,8)
    b = randrange(1,8)
    hue = r, g, b
    
    darkmode = randrange(0,2)
    
    fractal.generate(d, iterations, power, hue, darkmode, updatemode)
