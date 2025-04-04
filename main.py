import mitsuba as mi
import matplotlib.pyplot as plt
import numpy as np

mi.set_variant('cuda_ad_rgb')

#Load Scene
scene = mi.load_file('asset/cave_scene_cut.xml')
image = mi.render(scene, spp= 1024)
bitmap = mi.Bitmap(image)
image = np.array(bitmap)

# plt.imshow(image)
plt.imshow(image ** (1.0 / 2.2)); # approximate sRGB tonemapping
# plt.imshow(image ** 0.3); # approximate sRGB tonemapping
plt.axis("off")
plt.show()