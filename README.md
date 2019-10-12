# Tikolu Fractal
A very simple Mandelbrot fractal generator made in python

![Positive Fractal](https://raw.githubusercontent.com/Tikolu/Fractal/master/screenshots/positive_fractal.png)
![Negative Fractal](https://raw.githubusercontent.com/Tikolu/Fractal/master/screenshots/negative_fractal.png)
![Square Fractal](https://raw.githubusercontent.com/Tikolu/Fractal/master/screenshots/square_fractal.png)

`screensaver.py` is a demo project which is not required to use `fractal.py`  

---

To import `fractal.py`:
```python
import fractal
```  

---

To initialize a Pygame screen for generating fractals:
```python
d = fractal.display(width, height, fullscreen, colour)
```
`width` - The width of the screen in pixels. Default is `800`.  
`height` - The height of the screen in pixels. Default is `600`.  
`fullscreen` - Whether or not the screen should be initialized in fullscreen mode. Default is `False`.  
`colour` - An RGB value for the background colour of the screen. Default is `(0,0,0)` black.  
The function returns the screen which then needs to be passed on to the `fractal.generate` function. It is best to store it in a variable.  

---

To generate a fractal on the Screen
```python
fractal.generate(screen, iterations, power, hue, darkmode, updatemode):
```
`screen` - The display on which the fractal is to be generated.  
`iterations` - The amount of complex operations the generator calculates before moving onto the next pixel. Higher values lead to more detailed fractals but take longer to generate. Default is `15`.  
`power` - The amount to which each point is raised to, causes the fractal to have more arms. `2` generates a classic Mandelbrot. Negative values cause spotty shapes and floats lead to more chaotic merged fractals. Default is `2`.  
`hue` - A value which the result of the calculation is divided by, gives simple control over the colour of the fractal. Default is `(2,2,2)`.  
`darkmode` - Whether or not the colours should be flipped, leading to the inside of the fractal being rendered as black. Note that this is done before the `hue` calculation, so only brightness is affected. Default is `False`.  
`updatemode` - How frequently should the image be updated while generating. `0` waits until generation is finished, `1` updates after every horizontal line, `2` after every second line, and so on. Default is `1`.
