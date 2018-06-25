"""
TODO:
check for inputs
change change_time function to work on negative numbers
"""


from os import listdir
from os.path import isfile, join
from sys import exit

"""
str time_string: time in the format: "00:00:00,000 --> 00:00:00,000"
int change: how many miliseconds to change
"""
def change_time(time_string, change):
	hour = int(time_string[0:2])
	minute = int(time_string[3:5])
	second = int(time_string[6:8])
	milisecond = int(time_string[9:12])
	
	milisecond += change
	
	if (milisecond > 999):
		second += milisecond // 1000 #// is integer division
		milisecond = milisecond % 1000
	if (second > 59):
		minute += second // 60
		second = second % 60
	if (minute > 59):
		hour += minute // 60
		minute = minute % 60
	
	result = "%02d:%02d:%02d,%03d" % (hour, minute, second, milisecond)
	
	return result

mypath = './'
files = [f for f in listdir(mypath) if isfile(join(mypath, f))] #list of files in the same directory of the program

#print files (user interface)
for i in range(len(files)):
	print(str(i) + ". " + files[i])

sub_index = int(input("What is your subtitle file's index? "))
if sub_index >= len(files):
	print("\nERROR!: Subtitle file index is too big.")
	exit()

video_index = int(input("What is the index of corresponding video file? "))
if video_index >= len(files):
	print("\nERROR!: Video file index is too big.")
	exit()
elif video_index == sub_index:
	print("\nERROR!: Video file cannot be same as subtitles file.")
	exit()

synch = int(input("What is synchronization value (in miliseconds)? "))
	
print("\n")
print("Subtitle file: " + files[sub_index]) 
print("Video file: " + files[video_index]) 
print("Synch value: " + str(synch))


proceed = input("\nPress enter to proceed, CTRL-C to exit.\n")




new_subtitles = files[video_index]
new_subtitles = new_subtitles[:-3] + "srt"

	
subfile = open(files[sub_index], "r")




lines = subfile.readlines()

#new subtitle file
new_subfile = open(new_subtitles, "a")


for i in lines:
	if '-->' in i:
		first_part = change_time(i[0:12], synch)
		second_part = change_time(i[17:29], synch)
		i = first_part + " --> " + second_part + "\n"

	new_subfile.write(i)


		

		
		

