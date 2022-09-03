import numpy as np
import pygame as pg
import scipy as sp
import sympy
import wave as wv
from audioHandling import *
from matplotlib import pyplot as plt


input_file = ['sin_c.wav', 'sin_a.wav']

for file in input_file:
        
    sampling_rate, signal = read_audio_generic(file)

    signal = stereo_to_mono(signal)

    plt.plot(signal)
    plt.xlim = 8000
    plt.show()

    



