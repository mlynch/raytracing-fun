import sys
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
fig = plt.figure() # make figure

frames = int(sys.argv[1])

print("Rendering", frames, "frames")

imglist = []
for i in range(0, frames):
  fname = "out-" + str(i) + ".ppm"
  im = Image.open(fname)
  imglist.append(im)

im = plt.imshow(imglist[0])
# function to update figure
def updatefig(j):
  # set the data in the axesimage object
  im.set_array(imglist[j])
  # return the artists set
  return [im]

ani = animation.FuncAnimation(fig, updatefig, frames=range(frames), 
                                  interval=50, blit=True)
plt.show()
