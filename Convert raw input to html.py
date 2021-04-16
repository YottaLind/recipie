import os
import codecs

input_folders = ["input_raw/food/", "input_raw/drinks/", "input_raw/desserts/"]
output_folders = ["recipes/food/","recipes/drinks/","recipes/desserts/"]

for i in range(0,3):
    for x in os.listdir(input_folders[i]):
        if x.endswith(".txt"):
            input_file = codecs.open(input_folders[i] + x, encoding='utf-8', mode='r')
            line = input_file.readline()
            output_file = codecs.open(output_folders[i] + line.strip() + ".html",encoding='utf-8', mode='w+')
            output_file.write('<link rel="stylesheet" href="styles.css">' + '\n')
            output_file.write('<h1>' + line.strip() + '</h1>' + '\n')
            output_file.write('<article>' + '\n' + '<section id="ingredients">' + '\n' + '<h1>Ingredients</h1>' + '\n')
            line = input_file.readline()
            # line = input_file.readline()
            # output_file.write('<p>' + line.strip() + '</p>' + '\n')
            # ingredients ul and li
            output_file.write('<ul>\n')
            while(True):
                
                # read next line
                line = input_file.readline().strip()
                
                # check if line = Instuctions
                if line == 'Instuctions':
                    break
                output_file.write('<li>')
                if line.startswith("#"):
                    output_file.write('<h1>'+ line[1:] +'</h1>')
                elif line.startswith("amount:"):
                    output_file.write('<p>' + line[7:] + '</p>' + '\n')
                else:
                    output_file.write('<label><input type="checkbox">' + line + '</label>')
                output_file.write('</li>\n')
            output_file.write('</ul>\n</section>\n')
            # instructions ul and li
            output_file.write('<section id="instructions">\n<h1>Instructions</h1>\n')
            output_file.write('<ul>\n')
            while(True):
                # read next line
                line = input_file.readline().strip()
                # check if line = Instuctions
                if  not line:
                    break
                output_file.write('<li>')
                if line.startswith('#'):
                    output_file.write('<h1>'+ line[1:] +'</h1>')
                elif line.startswith("temp:"):
                    output_file.write('<h1>'+ line +'</h1>')
                else:
                    output_file.write('<label><input type="checkbox">' + line + '</label>')
                output_file.write('</li>\n')
            output_file.write('</ul>\n</section>\n</article>')
            # close file

