import mitsuba as mi
# from mitsuba import ScalarTransform4f as T
import matplotlib.pyplot as plt
import numpy as np

# mi.set_variant('cuda_ad_rgb')
mi.set_variant('scalar_rgb')
#Load Scene
scene = mi.load_file('asset/cave_scene.xml')
image = mi.render(scene)
bitmap = mi.Bitmap(image)
image = np.array(bitmap)

plt.imshow(image)
plt.axis("off")
plt.show()