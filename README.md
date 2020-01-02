# LightsOutSolver

A small project to analyze a "Light's Out" game from images (using openCV) and solving them using pure python.

## Getting Started

Wikipedia describes the game as follows:
"Lights Out is an electronic game released by Tiger Electronics in 1995. The game consists of a 5 by 5 grid of lights. When the game starts, a random number or a stored pattern of these lights is switched on. Pressing any of the lights will toggle it and the adjacent lights. The goal of the puzzle is to switch all the lights off, preferably in as few button presses as possible." 

The purpose of the program is to create an easy way to solve this puzzles. By leveraging OpenCV, the program can analyze and detect the gridlines of the board as well as detect which tiles are on by using OpenCV in python. From this knowledge, the method of chasing the lights, was implemented in pure python as to solve the puzzle and provide the user with step-by-step solutions.

### Python Version

The proyect was tested and working with Python 3.

## Download and Running

First, donwload the files and unzip in the desired location.
Then, open the terminal window and navigate towards the location of the downloaded project.
To test the program, the files provide a folder containing 4 digital images of "Light's Out" game boards that can be used.
As an example, using one of the provided image files, run the following command: 

```
python LightsOutSolver.py --image images/Sample3.png
```

After running the command above, three images should appear.
The images are the Original image, and 2 threashold images that that program will use to solve the puzzle.

To continue, press any key.

After this, the terminal will show each step needed to solve the puzzle.
As an example, using the Sample3.png image, the first steps shown in the terminal are as follows:

```
1 1 0 1 0

1 0 1 0 0

0 1 1 1 1

1 0 1 0 0

1 0 0 1 0

Click position  5
Click position  6
Click position  8
0 0 0 0 0

1 0 1 1 1

1 0 1 0 1

1 0 1 0 0

1 0 0 1 0

Click position  10
Click position  12
Click position  13
Click position  14
```


## Authors

* **Daniel Alfaro R.** (https://github.com/danyalfaro)


## Acknowledgments

Many thanks to Adrian Rosebrock and his blog at https://www.pyimagesearch.com/ for the resources needed to complete this project.
