- [Description](#pycoinflipper)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Settings](#settings)
- [Performance](#performance)


## Status
Finished! I don't know what to do next but this was an eye-opening experiment where i actually completed a python project, even with the basics of both python and github as i just pushed everything to the master branch. Maybe i'll do better next time!
## PyCoinFlipper
An Advanced Python program that flips coins and finds out the data from it. It takes advantage of directories and is my first big project where I made something with multiple libraries, files ,directories and it even had settings, which is a development in my learning of python hugely.
## Prerequisites
Python3.xx
- Random Libary
- Time Library
- Os Library
# Command To install prerequisites
**Installation in Pip**
```
pip install random os time
```

## Usage
simply enter the number of coins you want to calculate and then it will create the following data:
- Number of heads
- Number of tails
- Total number of heads and tails (total coin count)
- List of all the 1's and 2's in the coin data
## Settings
If you want to change the settings after disabling the startup text you can go into settings.txt.
Currently there are 2 settings available.
## Performance
Single-Core Performance on an intel core i5-3770 (explicitly handled threads are not used in this program for better performance)
| Number Of Coins  | Time Taken(seconds) |
| ------------- | ------------- |
| 10000  | 0.01007  |
| 100000  | 0.09397  |
| 1000000  | 0.8385  |
| 10000000  | 8.6002  |
| 100000000  | 84.2302  |
A test of 1000000 coins is printed out in a text file called CoinDataFile.txt