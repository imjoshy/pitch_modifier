# https://www.thetopsites.net/article/58183597.shtml

# changes pitch
import wave
import numpy as np

# see if file exists
import os.path
from os import path

def change_pitch(name, change_by):
    wr = wave.open(name + '.wav', 'r')
    
    # Set the params for output file
    par = list(wr.getparams())
    par[3] = 0 # The number of samples will be set by writeframes
    par = tuple(par)
    if path.exists(name + '[' + change_by + ']' + '.wav'):
        os.remove(name + '[' + change_by + ']' + '.wav')
    ww = wave.open(name + '[' + change_by + ']' + '.wav', 'w')
    ww.setparams(par)

    fr = 60
    sz = wr.getframerate()//fr  # Read and process 1/fr second at a time.
    # A larger number for fr means less reverb.
    c = int(wr.getnframes()/sz)  # count of the whole file
    shift = int(change_by)//fr  # shifting 100 Hz

    for num in range(c):
        da = np.fromstring(wr.readframes(sz), dtype=np.int16)
        left, right = da[0::2], da[1::2]  # left and right channel
        lf, rf = np.fft.rfft(left), np.fft.rfft(right)
        lf, rf = np.roll(lf, shift), np.roll(rf, shift)
        lf[0:shift], rf[0:shift] = 0, 0
        nl, nr = np.fft.irfft(lf), np.fft.irfft(rf)
        ns = np.column_stack((nl, nr)).ravel().astype(np.int16)
        ww.writeframes(ns.tostring())

    wr.close()
    ww.close()

if __name__ == '__main__':
    name = input('Name of file (no extensions): ')
    change_by = input('How much to change it by (in Hertz): ')
    change_pitch(name, change_by)