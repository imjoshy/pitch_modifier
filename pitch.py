# https://stackoverflow.com/questions/43963982/python-change-pitch-of-wav-file

import wave
import numpy as np

# change_pitch will change the pitch of the .wav file and produce a new .wav file with output
# name = name of output file
# hz = how much to change the pitch of the file by
def change_pitch(name, hz):

    # Open the .wav file
    original = wave.open(name + '.wav', 'r')
    # Set parameters for output file
    par = list(original.getparams())
    par[3] = 0
    par = tuple(par)
    
    new_name = name + '_modified[' + str(hz) + '].wav'

    # Create a new .wav file to write to, give same parameters as original file
    new_file = wave.open(new_name, 'w')
    new_file.setparams(par)

    # Process speed --
            # Bigger fr = less reverb
            # Smaller fr = more reverb
    fr = 20
    sz = original.getframerate()//fr
    c = int(original.getnframes()/sz)


    ##### change VARIABLE CONTROLS HOW MUCH TO RAISE/LOWER THE FREQUENCY BY
    change = hz//fr     # Change frequency based on how much hertz passed as param

    for num in range(c):

            # Regurgitated code from website above to test why the commented section below doesn't work
            # -- Results in ValueError: read of closed file
            # ** EVEN WHEN RUN AS ADMIN (file permissions for administrator are full control)
            da = np.fromstring(original.readframes(sz), dtype=np.int16)
            left, right = da[0::2], da[1::2]
            lf, rf = np.fft.rfft(left), np.fft.rfft(right)
            lf, rf = np.roll(lf, change), np.roll(rf, change)
            lf[0:change], rf[0:change] = 0, 0
            n1, nr = np.fft.irfft(lf), np.fft.irfft(rf)
            ns = np.column_stack((n1, nr)).ravel().astype(np.int16)
            new_file.writeframes(ns.tostring())

            original.close()
            new_file.close()
            # # Check if MONO (1 channel) or STEREO (2 channels)
            # channels = original.getnchannels()

            # if channels == 1: # MONO -- no need to split data
            #     data = np.frombuffer(original.readframes(sz), dtype=np.int16)

            #     # Extract frequencies using Fast Fourier Transform
            #     frequency = np.fft.rfft(data)

            #     # Roll array -- changes the pitch based on change variable
            #     frequency = np.roll(frequency, change)
            #     frequency[0:change] = 0

            #     # Inverse Fast Fourier Transform to convert back to amplitude
            #     new_frequency = np.fft.irrft(frequency)

            #     # Write to output
            #     new_file.writeframes(new_frequency)

            #     original.close()
            #     new_file.close()

            #     return
            
            # if channels == 2: # STEREO -- split data for LEFT and RIGHT ears
            #     data = np.frombuffer(original.readframes(sz), dtype=np.int16)
                
            #     # Split into channels
            #     l, r = data[0::2], data[1::2] # l for left channel; r for right channel
               
            #     # Get frequencies for the channels
            #     lf, rf = np.fft.rfft(l), np.fft.rfft(r) # lf for left frequency, rf for right frequency
               
            #     # Roll arrays -- change pitch
            #     lf, rf = np.roll(lf, change), np.roll(rf, change)
            #     # lf[0:change], rf[0:change] = 0, 0

            #     # Inverse Fast Fourier Transform to convert back to amplitude
            #     n1, nr = np.fft.irfft(lf), np.fft.irfft(rf)

            #     # Combine channels
            #     new_frequency = np.column_stack((n1, nr)).ravel().astype(np.int16)

            #     # Write to output
            #     new_file.writeframes(new_frequency)
            #     original.close()
            #     new_file.close()

            #     return

if __name__ == '__main__':
    # RECEIVE INPUT -- for now just type in name of .wav file
        # Eventually need to allow a click & drag, but that's for later
    name = input("Name of file (no extensions): ")
    hz = int(input("Hz to change by: "))
    change_pitch(name, hz)