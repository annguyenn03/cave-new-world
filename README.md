# Cave New World: Realistic Cave Rendering
## Introduction:
Natural caves typically have interesting structures. With limited opening to sunlight, light beams are created, and this phenomenon demonstrates the concept of global illumination with walls getting direct sunlight and walls getting light from higher-order bounces. Dust particles usually exist and can be realistically rendered with volumetric rendering. We want to use these techniques to render a realistic cave scene.

## Application:
It can help rebuild collapsed areas for history study, reduce risks for explorers by helping them visualize the real condition of the cave, serve educational purposes as it can be watched online, and improve film and video games.

## Framework:
* Blender version 4.3 (Used as the baseline and mofify the 3D model)
* Mitsuba 3 with Python 3.13.2 (Render the scene)

## Main Components:
* **asset/cave_scene_cut.xml defines the scene:**<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Integrator:** Method for rendering is volpath (Volumetric Path Tracing) with a max depth of 24<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Sensor:** Capture the image output with Perspective with fov, clipping plane, translate value and rotation<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Material of the cave:** Defined in bsdf twosided and principled with texture in shape type = "ply" section<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Light:** Area light in a rectangle shape<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Participating media:** Homogeneous medium<br>
* **main.py:** main program to render the scene. This scene was render with 1024 samples per pixel

* **asset/cave_camera_cut_sun_withScatter.blend:** The baseline for god rays in Blender (including the 3D cave model, camera location, directional light, a volume scatter cube)
* **asset/cave_camera_cut_sun.blend:** Cave model with camera location and sky texture for light


## How to Run:
1. Clone the repository by using command line ```git clone https://github.com/annguyenn03/cave-new-world.git``` in the terminal
2. Open terminal in the same folder (cave-new-world) and Run ```python main.py```

## Citation:
3D Cave model was modified from "North Head tunnels" (https://skfb.ly/6VFpq) by b_nealie is licensed under Creative Commons Attribution (http://creativecommons.org/licenses/by/4.0/)

```
@software{jakob2022mitsuba3,
    title = {Mitsuba 3 renderer},
    author = {Wenzel Jakob and Sébastien Speierer and Nicolas Roussel and Merlin Nimier-David and Delio Vicini and Tizian Zeltner and Baptiste Nicolet and Miguel Crespo and Vincent Leroy and Ziyi Zhang},
    note = {https://mitsuba-renderer.org},
    version = {3.0.1},
    year = 2022,
}
```
