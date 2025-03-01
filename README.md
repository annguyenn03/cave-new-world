# Cave New World: Realistic Cave Rendering
## Introduction:
Natural caves typically have interesting structures. With limited opening to sunlight, light beams are created, and this phenomenon demonstrates the concept of global illumination with walls getting direct sunlight and walls getting light from higher-order bounces. Dust particles usually exist and can be realistically rendered with volumetric rendering. We want to use these techniques to render a realistic cave scene.

## Application:
It can help rebuild collapsed areas for history study, reduce risks for explorers by helping them visualize the real condition of the cave, serve educational purposes as it can be watched online, and improve film and video games.

## Framework:
* Blender to edit the 3D model
* Mitsuba 3 to render with an XML for loading the scene and modify futher with Python

## How to Run:
1. Clone the repository
2. Open terminal in the same folder and Run ```python main.py```

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
