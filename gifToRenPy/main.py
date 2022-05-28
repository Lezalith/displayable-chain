# Path 
resultPath = "results/"

# Lets you pick a file and returns it.
import easygui
def pickFile():

    a = easygui.fileopenbox( title = "Pick .gif to split:" )

    # Raise exception if a file wasn't picked
    if not a:
        raise Exception("Nothing selected!")
        
    return a

# File path
file = pickFile()

# File name with extension.
filename = file.split("\\")[-1]

if filename.count(".") > 1:
    print("Warning: Multiple dots in the filename might result in weird result folder name.")

# File name without extension.
filename = filename.split(".")[0]


# Preparing the export directory.
import os

# Creating folder for the frames
try:
    os.mkdir( resultPath + filename )

# Error:
except:

    # Result folder not created yet
    try:
        os.mkdir( resultPath )
        os.mkdir( resultPath + filename )

    # Folder for frame export exists.
    except:
        raise Exception("It looks like a folder where a result would be placed already exists.")


# For the (gif -> png) conversion.
from PIL import Image

# Open chosen file.
im = Image.open(file)

# Path to all frame files.
framePaths = []

# For every frame inside the Image:
for frameIndex in range( im.n_frames ):

    # Point at the current frameIndex.
    im.seek(frameIndex)

    # Path to the exported frame.
    pathToFrame = resultPath + filename + "/" + filename + str(frameIndex) + ".png"

    # Save the frame.
    im.save( pathToFrame )

    # Add frame path to the list.
    framePaths.append( pathToFrame )


# Interval of pause statements
pauseInterval = 0.2
# Whether "repeat" should be added at the end.
repeat = False

# Create a file for the image statement inside Ren'Py.
with open(resultPath + filename + "/" + "image_statement.txt", "w+") as f:

    # Write an image path, followed by a pause.
    for framePath in framePaths:

        f.write( framePath + "\n" )
        f.write( "pause " + str(pauseInterval) + "\n" )

    # Optionally finish with a repeat.
    if repeat:

        f.write("repeat")