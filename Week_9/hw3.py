# Homework 3
# Time: Fall 2021
# Date: 19-Oct.-2021
# School: CSUMB
# Author: Roshan Indika Menik Arachchi Menik Arachchige
# Description: GUI for an enhanced image search engine.
#################################################################################################################
import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QComboBox, QVBoxLayout, QLineEdit
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtCore import Slot
from PySide2 import QtCore
from PIL import Image
from image_info import image_info

######################################################################################
# A QComboBox will allow the user to select one of the following image manipulations
######################################################################################
manipulations = ["None", "Sepia", "Negative", "Grayscale", "Thumbnail"]

###########################################
# New window which will contain the image
###########################################
class NewWindow(QWidget):
    def __init__(self):
        super().__init__()

################################################
# Main Window
################################################
class Main(QWidget):
    def __init__(self):
        super().__init__()

        # Window Heading Name
        self.setWindowTitle("Homework 3")
        # box search the match with tags
        self.search = QLineEdit(self)
        # combo box to edit the choosen image w/t manipulations
        self.mainCombo = QComboBox()
        self.mainCombo.addItems(manipulations)
        # create the 'Search' btn
        self.searchBtn = QPushButton('Search')

        # sets the layout
        vbox = QVBoxLayout()
        # add the search bar, combo box, and 'Search' btn
        vbox.addWidget(self.search)
        vbox.addWidget(self.mainCombo)
        vbox.addWidget(self.searchBtn)

        self.setLayout(vbox)
        self.searchBtn.clicked.connect(self.open_window)

    ####################################################
    # List of Functions
    ####################################################
    ####################################################
    # Function
    # Check if sub-string is in a larger string
    # Location: search bar
    ####################################################
    def isInString(self, substring, fullstring):
        if substring.lower() in fullstring.lower():
            return True
        else:
            return False

    ########################################################
    # Sub-function
    # Action: Formula for Every pixel change into GrayScale
    # Location: GrayScale Function
    ########################################################
    def rgb2gray(self, p):
        new_red = int(p[0] * 0.2989)
        new_green = int(p[1] * 0.5870)
        new_blue = int(p[2] * 0.1140)
        gray = new_red + new_green + new_blue
        return (gray,) * 3

    ####################################################
    # Function
    # Action: Edit IMG into GrayScale
    ####################################################
    def grayscale(self, path):
        img = Image.open(path)

        gray_list = map(self.rgb2gray, img.getdata())
        img.putdata(list(gray_list))

        img.save('hw3_images/grayScale.jpg')

    ####################################################
    # Function
    # Action: Edit IMG with Sepia filter
    ####################################################
    def sepia(self, path):
        img = Image.open(path)

        sepia_list = []
        for i in img.getdata():
            new_val = (0.3 * i[0] + 0.59 * i[1] + 0.11 * i[2])
            new_red = int(new_val * 2)

            if new_red > 255:
                new_red = 255
            new_green = int(new_val * 1.5)
            if new_green > 255:
                new_green = 255
            new_blue = int(new_val)
            if new_blue > 255:
                new_blue = 255

            sepia_list.append((new_red, new_green, new_blue))
        img.putdata(sepia_list)
        img.save('hw3_images/sepia.jpg')

    ########################################################
    # Sub-function
    # Action: Formula for Every pixel change Negative filter
    # Location: Negative filter Function
    ########################################################
    def rgb2neg(self, pixel):
        return tuple(map(lambda a : 255 - a, pixel))

    ####################################################
    # Function
    # Action: Edit IMG with Negative filter
    ####################################################
    def negative(self, path):
        img = Image.open(path)

        negative_list = map( self.rgb2neg, img.getdata() )
        img.putdata(list(negative_list))
        img.save('hw3_images/negative.jpg')

    ############################################################
    # Function
    # Action: Edit IMG by Decreases the size of an image by 1/2
    ############################################################
    def thumbnail(self, path):
        img = Image.open(path)
        width, height = img.size
        img = img.resize((int(width / 2), int(height / 2)), Image.ANTIALIAS)
        img.save('hw3_images/thumbnail.jpg')

    @Slot()
    # The fucntion is called after the search btn is pressed
    # Open a new Window w/t img
    # The process and result of the search is done below
    def open_window(self):
        count = []

        # collects and sets the info of the set imgs into an array called data
        for info in image_info:
            img = {
                "id" : info['id'],
                "count" : 0,
                "title" : info['title']
            }
            count.append(img)
            
        # reads user's input from the search bar
        searched = self.search.text()
        # splits the input into an array of strings
        searchedSplit = searched.split()

        # nested loop to search for every img name and tags with the searched words
        # add counter by 1 for every match found
        for letter in searchedSplit:
            for x in range(0, len(image_info)):
                if(self.isInString(letter, image_info[x]['title'])):
                    count[x]['count'] = count[x]['count'] + 1
                for tag in image_info[x]['tags']:
                    if(self.isInString(letter, tag)):
                        count[x]['count'] = count[x]['count'] + 1
            
        # Sort the list of img info with the img counter
        countSort = sorted(count, key=lambda k: k['count'], reverse=True)

        tie = []
        isTie = False

        # check for ties  in the 'count'
        # if 'True' = add to new list ('tie')
        for x in range(0, len(count)):
            if(countSort[0]['count'] == countSort[x]['count']):
                if(x == 0):
                    imgZero = {
                        "id" : countSort[x]['id'],
                        "count" : countSort[x]['count'],
                        "title" : countSort[x]['title']
                    }
                    tie.append(imgZero)
                else:
                    isTie = True
                    img = {
                        "id" : countSort[x]['id'],
                        "count" : countSort[x]['count'],
                        "title" : countSort[x]['title']
                    }
                    tie.append(img)
            
        # condition : if 'isTie' == True
        # action    : sort by 'Title' using ascending order
        if(isTie == True):
            sorted(tie, key = lambda i: i['title'])
            
        # create a file path with the closest match to the user's search
        path = "hw3_images/" + tie[0]['id'] + ".jpg"

        # input           : takes the selected manipulated setting
        # action & output : apply the selected manipulation & save the edited img in the same directory
        selected_manipulation = self.mainCombo.currentText()

        if(selected_manipulation == "Grayscale"):
            self.grayscale(path)
            path = 'hw3_images/grayscale.jpg'
            
        elif(selected_manipulation == "Sepia"):
            self.sepia(path)
            path = 'hw3_images/sepia.jpg'

        elif(selected_manipulation == "Negative"):
            self.negative(path)
            path = 'hw3_images/negative.jpg'

        elif(selected_manipulation == "Thumbnail"):
            self.thumbnail(path)
            path = 'hw3_images/thumbnail.jpg'

        # action : display the img in the new window
        self.new_window = NewWindow()
        new_vbox = QVBoxLayout()
        pixLabel = QLabel(self.new_window)
        pixmap = QPixmap(path)
        pixLabel.setPixmap(pixmap)
        new_vbox.addWidget(pixLabel)

        self.new_window.setLayout(new_vbox)
        self.new_window.resize(pixmap.width(), pixmap.height())
        self.new_window.show()

app = QApplication(sys.argv)
main = Main()
main.show()
sys.exit(app.exec_())


