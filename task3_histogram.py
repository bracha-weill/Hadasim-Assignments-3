from PIL import Image
import numpy ,matplotlib.pyplot as plt

img = Image.open("img.jpg")
data = numpy.array(img)
colors = ['red','green','blue']
for i, color in enumerate(colors):
    plt.hist(data[:,:,i].flatten(), bins=256, color=color, alpha=0.5)

plt.show()