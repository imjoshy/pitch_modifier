#####
# Src:
# https://stackoverflow.com/questions/38923438/does-pydub-support-pitch-modulation
#####

from pydub import AudioSegment
from pydub.playback import play
import tkinter as tk


#####
# change_pitch:
#       Take in a .wav file (for now?) and a pitch to change the file by. The overall file's pitch will change accordingly, however the
#       speed will change in proportion to the value entered.
###
#def change_pitch(file_name, pitch):

def change_pitch():

    file_name = enter_file.get()
    pitch = float(pitch_modify["text"])

    print("This is the file name: " + file_name)

    original_wav = AudioSegment.from_file(file_name + '.wav', format="wav")     # the original file

    new_rate = float(original_wav.frame_rate * (2.0 ** pitch))        # new rate at which the .wav will be in (changes pitch and speed of song/sound)

    new_wav = original_wav._spawn(original_wav.raw_data, overrides={'frame_rate': new_rate})        # the new file

    new_wav_name = file_name + '_[' + str(pitch) + '].wav'
    new_wav.export(new_wav_name, format='wav')      # save new file

# Increase the pitch of a file
def increase():
    value = float(pitch_modify["text"])
    pitch_modify["text"] = f"{value + float(0.05)}"
    "{0:.2f}".format(pitch_modify["text"])

# Decrease the pitch of a file
def decrease():
    value = float(pitch_modify["text"])
    pitch_modify["text"] = f"{value - float(0.05)}"
    "{0:.2f}".format(pitch_modify["text"])

if __name__ == '__main__':
    # print('='*50 + '\n' + '='*50)
    # print('Pitch Modifier')
    # print('='*50 + '\n' + '='*50)
    # print('NOTES:\n\t- Input ONLY .WAV FILES!')
    # print('\n\t- Speed of the file will change in\n\t  proportion to the pitch you want to\n\t  change it by.')
    # print('\n\t- Pitch can be positive or negative!')
    # print('\n\t- We recommend inputting a pitch change \n\t  between -1 and 1')
    # print('='*50 + '\n' + '='*50)
    # file = input('File Name (no extension): ')
    # pitch_ = float(input('How much should we change it (float value)? '))

    # change_pitch(file_name=file, pitch=pitch_)

    window = tk.Tk()

    window.rowconfigure([0, 1, 2, 3, 4, 5], minsize=50, weight=1)
    window.columnconfigure([0, 1, 2], minsize=50, weight=1)

    prj_name = tk.Label(master=window, text="Alvin")
    prj_name.grid(row=0, column=1)

    enter_file_lbl = tk.Label(master=window, text="1. Enter .wav here")
    enter_file_lbl.grid(row=1, column=1)

    enter_file = tk.Entry(master=window)
    enter_file.grid(row=2, column=1)

    pitch_label = tk.Label(master=window, text="Change by:")
    pitch_label.grid(row=3, column=1)

    # Changing the pitch
    btn_decrease = tk.Button(master=window, text='-', command=decrease)
    btn_decrease.grid(row=4, column=0, sticky="nsew")

    pitch_modify = tk.Label(master=window, text="0")
    pitch_modify.grid(row=4, column=1)

    btn_increase = tk.Button(master=window, text='+', command=increase)
    btn_increase.grid(row=4, column=2, sticky="nsew")

    # Generate the modified .wav file
    btn_generate = tk.Button(master=window, text="Generate", command=change_pitch)
    btn_generate.grid(row=5, column=1)


    window.mainloop()

