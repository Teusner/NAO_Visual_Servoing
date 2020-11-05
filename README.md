# NAO Visual Servoing

## Introduction

This repository is a school project to introduce visual servoing in robotics. The goal is to control a NAO robot using his camera and some image processing in python3. Then the robot will be able to play football using a ball detection algorithm.

## :barber: Tracker :barber:
Here is a tracker for each task we have to do.

| Task                     | Progression      |
| -------------------------|:----------------:|
| Ball detection           |:heavy_check_mark:|
| Read and show NAO images |:x:               |
| Realtime detection       |:x:               |
| Head heading control     |:x:               |
| Distance control         |:x:               |

## Ball detection

The script *visual_servoing.py* provide a ball tracker class which let us track a yellow ball like a tennis ball in a video stream.

![](imgs/ball_tracking.png)

This algorithm detect the center of gravity of the biggest circular yellow object in the HSV color space of the video stream.

## Authors

* **Quentin Brateau** -  [Teusner](https://github.com/Teusner) :sunglasses:
* **Paul-Antoine Le Tolguenec** - 

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details
