import os
import subprocess
import time
import sys
from shutil import copyfile



dir_input = "/home/steve/Pictures/HollywoodHeads/JPEGImages"
dir_output = "/home/steve/Pictures/HollywoodHeads/subset_JPEG"

dir_input2 = "/home/steve/Pictures/HollywoodHeads/Annotations"
dir_output2 = "/home/steve/Pictures/HollywoodHeads/subset_annotations"


i = 0
for file in os.listdir(dir_input):
    if file.endswith("001.jpeg"):
        i+=1
        
        input_path = dir_input + "/" + file
        output_path = dir_output + "/" + file
        print(input_path)
        print(output_path)

        copyfile(input_path, output_path)

        print(i)

i = 0
for file in os.listdir(dir_input2):
    if file.endswith("001.xml"):
        i+=1
        
        input_path_2 = dir_input2 + "/" + file
        output_path_2 = dir_output2 + "/" + file
        print(input_path_2)
        print(output_path_2)

        copyfile(input_path_2, output_path_2)

        print(i)


