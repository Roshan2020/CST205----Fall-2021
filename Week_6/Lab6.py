# Lab 6
# Time: Fall 2021
# School: CSUMB
# Author: Roshan Indika Menik Arachchi Menik Arachchige
##########################################################################################
from PIL import Image
# ----------------------------------- Task 1 ---------------------------------------------
# In the file (https://github.com/python-pillow/Pillow/blob/master/src/PIL/Image.py) the line 387 is one of many definitions
#
# ----------------------------------- Task 2 ---------------------------------------------
# In the file (https://github.com/python-pillow/Pillow/blob/master/src/PIL/Image.py) the line range from 2926 to 2952 is one of the docstring
#
# ----------------------------------- Task 3 ---------------------------------------------
img = Image.open('images/lab6_task3_tree.jpg')
print(dir(img))
# Description: The summary of this in-built function is to change the dimensions of the img to the size (width & height) to your design.
#
# ----------------------------------- Task 4 ---------------------------------------------
class Song:
    """ A Class created to define a Song"""

    def __init__(self, artist, genre, length, album, name):
        self.artist = artist
        self.genre = genre
        self.length = length
        self.album = album
        self.name = name

song1 = Song('BIGBANG', 'K-Pop', 3.75, 'E', "Let's Not Fall In Love")
song2 = Song('Clare Duan', 'C-Pop', 3.75, 'Love Scenery OST', "Never Stop")
song3 = Song('Owl City', 'Pop', 3.75, 'Mobile Orchestra', "I Found Love")
song4 = Song('Walk Off The Earth', 'Pop', 2.75, 'The Journey Starts Today (Theme from Pokémon Journeys)', "The Journey Starts Today")

print("1st Song Description")
print("Name: " + song1.name)
print("Artist: " + song1.artist)
print("Album: " + song1.album)
print("Genre: " + song1.genre)
print("Duration: " + str(song1.length))