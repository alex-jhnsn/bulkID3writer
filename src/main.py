import eyed3
import sys
import json
import os
from os import listdir
from os.path import isfile, join

def isMp3(file):
    file, ext = os.path.splitext(file)
    if ext == '.mp3':
        return True
    return False

def setTags(file, template):

    track = eyed3.load(file)

    # if template is None: 
    #     track.tag.album = "Lol"
    #     return

    if (track.tag.album == None):
        print("No album title")
        track.tag.album = track.tag.title
        
    sys.stdout.write(track.tag.title + "\n")

    # track.tag.album = template[''] or "Lol"
    track.tag.save()

def run():

    path = None

    if len(sys.argv) == 2: 
        if sys.argv[1] == "--help":
            sys.stdout.write("Usage: foo [DIRECTORY_PATH] [TEMPLATE]\n")
            sys.stdout.write("Leave both blank for defaults\n")
            return
        path = sys.argv[1]

    path = path or os.path.dirname(os.path.realpath(__file__))
    sys.stdout.write(path + "\n")

    mp3files = [f for f in listdir(path) if isfile(join(path, f)) and isMp3(f)]

    sys.stdout.write(str(len(mp3files)) + "\n")
    for index, mp3file in enumerate(mp3files):
        print("Editing track " + str(index + 1) + " of " + str(len(mp3files)))
        setTags(mp3file, None)

run()
