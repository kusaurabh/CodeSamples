#!/usr/bin/python3

import sys
import string

def encode_str(text, num_rot):
    result_str =""
    if len(text) > 0:
        for i in range(len(text)):
            current_ch_num = ord(text[i])
            if text[i].islower():
                MAX_LIMIT = ord('z')
                char_range = ord('z') - ord('a')
                num_rot = num_rot % char_range
                #Check if wrapping is required
                if current_ch_num + num_rot > ord('z'):
                    encode_ch_num = ord('a') + (current_ch_num + num_rot - ord('z'))
                else:
                    encode_ch_num = current_ch_num + num_rot
                     
            elif text[i].isupper():
                MAX_LIMIT = ord('Z')
                char_range = ord('Z') - ord('A')
                num_rot = num_rot % char_range
                #Check if wrapping is required
                if current_ch_num + num_rot > ord('Z'):
                    encode_ch_num = ord('A') + (current_ch_num + num_rot - ord('Z'))
                else:
                    encode_ch_num = current_ch_num + num_rot
            else:
                encode_ch_num = current_ch_num
                     
            result_str = result_str + chr(encode_ch_num)

    return result_str


if __name__ == "__main__":
    if len(sys.argv) == 3:
        text = sys.argv[1]
        try:
            rot_amount = int(sys.argv[2])
            result = encode_str(text, rot_amount)
            print(result)
        except e:
            print(e)
            print("Secong argument shoud be number")
             
    else:
        print("Usage : encode <string> <encode number>")
