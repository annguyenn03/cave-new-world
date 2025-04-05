import mitsuba as mi
import matplotlib.pyplot as plt
import numpy as np

mi.set_variant('cuda_ad_rgb')

#Load Scene and Render
scene = mi.load_file('asset/cave_scene_cut.xml')
image = mi.render(scene, spp= 1024)
bitmap = mi.Bitmap(image)
image = np.array(bitmap)

#Show the output
plt.imshow(image ** (1.0 / 2.2)); # approximate sRGB tonemapping
plt.axis("off")
plt.show()