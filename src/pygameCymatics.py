import numpy as np
import os


class Scene:

    def __init__(self, audiofile):
        
        if not os.path.isfile(audiofile):
            raise Exception("Input path not found!")

        self.audiofile = audiofile

    
    def output(self):

        #visual
        pass

