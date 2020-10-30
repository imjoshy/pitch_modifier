#####
# Src:
# https://stackoverflow.com/questions/38923438/does-pydub-support-pitch-modulation
#####

from pydub import AudioSegment
from pydub.playback import play


#####
# change_pitch:
#       Take in a .wav file (for now?) and a pitch to change the file by. The overall file's pitch will change accordingly, however the
#       speed will change in proportion to the value entered.
###
def change_pitch(file_name, pitch):

    original_wav = AudioSegment.from_file(file_name + '.wav', format="wav")     # the original file

    new_rate = int(original_wav.frame_rate * (2.0 ** pitch))        # new rate at which the .wav will be in (changes pitch and speed of song/sound)

    new_wav = original_wav._spawn(original_wav.raw_data, overrides={'frame_rate': new_rate})        # the new file

    new_wav_name = file_name + '_[' + str(pitch) + '].wav'
    new_wav.export(new_wav_name, format='wav')      # save new file


if __name__ == '__main__':
    print('='*50 + '\n' + '='*50)
    print('Pitch Modifier')
    print('='*50 + '\n' + '='*50)
    print('NOTES:\n\t- Input ONLY .WAV FILES!')
    print('\n\t- Speed of the file will change in\n\t  proportion to the pitch you want to\n\t  change it by.')
    print('\n\t- Pitch can be positive or negative!')
    print('\n\t- We recommend inputting a pitch change \n\t  between -1 and 1')
    print('='*50 + '\n' + '='*50)
    file = input('File Name (no extension): ')
    pitch_ = float(input('How much should we change it (float value)? '))

    change_pitch(file_name=file, pitch=pitch_)
