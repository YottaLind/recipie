"""
This code will go through all files in the input folder and format the contents to
conform to the html format I have created and save the html file to the output folder.
Trying to streamline the adding of new recepies
"""
import os

print("Starting to generate html files")
input_file = open("input/chivapchichi.txt", "r")
output_file = open("output/test.html", "w")
line = input_file.readline()
output_file.write('<link rel="stylesheet" href="styles.css">' + '\n')
output_file.write('<h1>' + line.strip() + '</h1>' + '\n')
output_file.write('<article>' + '\n' + '<section id="ingredients">' +
                  '\n' + '<h1>Ingredients</h1>' + '\n')
line = input_file.readline()
line = input_file.readline()
output_file.write('<p>' + line.strip() + '</p>')
# ingredients ul and li
while(True):
	# read next line
	line = input_file.readline().strip()
	# check if line = Instuctions
	if line() == 'Instuctions':
		break
    output_file.write(line + "test\n")
    # if line[0] == '#':
    #     output_file.write('<h1>'+ line[1:-1] +'</h1>')
    # else:
	#     output_file.write(line + "\n")
# instructions ul and li
while(True):
	# read next line
	line = input_file.readline()
	# check if line = Instuctions
	if  not line:
		break

	output_file.write(line.strip() + "\n")

# close file
input_file.close
output_file.close
