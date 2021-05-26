import os
"""
    Copyright (C) 2021  dani2318

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

"""
    THIS SCRIPT USES THE FOLLOWING RESOURCES AND PROGRAMS:
    ╔
    ║   Whitedeops Colors Repository: https://github.com/whitedevops/colors/blob/master/colors.go
    ║   FFMPEG: https://ffmpeg.org/legal.html -> Source Code: https://github.com/FFmpeg/FFmpeg
    ╚
"""

"""
    DISCLAIMER:
    I don't own any right over FFMPEG, but for anything you can find info on this site:
    https://www.ffmpeg.org/about.html
"""


from colors import colors
#Read the script running path!
pathToFile = os.path.realpath(__file__).replace("convert.py","")
print(colors.Bold+colors.BackgroundWhite+colors.Black+"Input the requested info:"+colors.ENDC+colors.ENDC+colors.ENDC)
#Ask the file to convert to the user:
print(colors.Red+"WARNING: THE FILE TO CONVERT MUST BE ON THE SAME FOLDER AS THIS SCRIPT AND FFMPEG!"+colors.ENDC)
name = input("Enter the name of the file to convert:\n\n")
print(colors.Red+"WARNING:THE EXTENSION MUST BE WRITEN AS IN THE EXAMPLE: EX:'mp3'\n"+colors.ENDC)
ext = input(colors.Underlined+"Enter the extention to convert the file into: (EX: 'mp3','mp4','wav' etc..)!\n"+colors.ENDC)

#Check if the output folder exist:
if(not(os.path.exists(pathToFile+"Converted"))):
    os.mkdir(pathToFile+"Converted")

#Building the paths:
filename = pathToFile+name
filename_output = "\""+filename.replace(name,"")+"\\converted\\"+name.replace(".mp3","."+ext)+"\""
filename_output.replace("\"","")
filename = '"'+pathToFile+name+'"'

#Conversion Handler:
def convert(filename,filename_output):
    print(colors.Bold+colors.BackgroundWhite+colors.Black+"Conversion Started!"+colors.ENDC+colors.ENDC+colors.ENDC)
    #Conversion!
    os.system('bin\\ffmpeg.exe -i '+ filename+ " " + filename_output)

convert(filename,filename_output)
print(colors.Green+"Conversion Completed!"+colors.ENDC)

print(colors.Bold+colors.BackgroundWhite+colors.Black+"You can find the converted file in the 'Converted' folder!"+colors.ENDC+colors.ENDC+colors.ENDC)
