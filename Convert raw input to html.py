import os
#Food
for x in os.listdir("input_raw/food/"):
    if x.endswith(".txt"):
        input_file = open("input_raw/food/" + x, "r")
        line = input_file.readline()
        output_file = open("recipes/food/" + line.strip() + ".html", "w")
        output_file.write('<link rel="stylesheet" href="styles.css">' + '\n')
        output_file.write('<h1>' + line.strip() + '</h1>' + '\n')
        output_file.write('<article>' + '\n' + '<section id="ingredients">' + '\n' + '<h1>Ingredients</h1>' + '\n')
        line = input_file.readline()
        line = input_file.readline()
        output_file.write('<p>' + line.strip() + '</p>' + '\n')
        # ingredients ul and li
        output_file.write('<ul>\n')
        while(True):
            
            # read next line
            line = input_file.readline().strip()
            
            # check if line = Instuctions
            if line == 'Instuctions':
                break
            output_file.write('<li>')
            if line[0] == '#':
                output_file.write('<h1>'+ line[1:] +'</h1>')
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
            if line[0] == '#':
                output_file.write('<h1>'+ line[1:] +'</h1>')
            else:
                output_file.write('<label><input type="checkbox">' + line + '</label>')
            output_file.write('</li>\n')
        output_file.write('</ul>\n</section>\n</article>')

        # close file
#Desserts
for x in os.listdir("input_raw/desserts/"):
    if x.endswith(".txt"):
        input_file = open("input_raw/desserts/" + x, "r")
        line = input_file.readline()
        output_file = open("recipes/food/" + line.strip() + ".html", "w")
        output_file.write('<link rel="stylesheet" href="styles.css">' + '\n')
        output_file.write('<h1>' + line.strip() + '</h1>' + '\n')
        output_file.write('<article>' + '\n' + '<section id="ingredients">' + '\n' + '<h1>Ingredients</h1>' + '\n')
        line = input_file.readline()
        line = input_file.readline()
        output_file.write('<p>' + line.strip() + '</p>' + '\n')
        # ingredients ul and li
        output_file.write('<ul>\n')
        while(True):
            
            # read next line
            line = input_file.readline().strip()
            
            # check if line = Instuctions
            if line == 'Instuctions':
                break
            output_file.write('<li>')
            if line[0] == '#':
                output_file.write('<h1>'+ line[1:] +'</h1>')
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
            if line[0] == '#':
                output_file.write('<h1>'+ line[1:] +'</h1>')
            else:
                output_file.write('<label><input type="checkbox">' + line + '</label>')
            output_file.write('</li>\n')
        output_file.write('</ul>\n</section>\n</article>')

        # close file
#Drinks
for x in os.listdir("input_raw/drinks/"):
    if x.endswith(".txt"):
        input_file = open("input_raw/drinks/" + x, "r")
        line = input_file.readline()
        output_file = open("recipes/drinks/" + line.strip() + ".html", "w")
        output_file.write('<link rel="stylesheet" href="styles.css">' + '\n')
        output_file.write('<h1>' + line.strip() + '</h1>' + '\n')
        output_file.write('<article>' + '\n' + '<section id="ingredients">' + '\n' + '<h1>Ingredients</h1>' + '\n')
        line = input_file.readline()
        line = input_file.readline()
        output_file.write('<p>' + line.strip() + '</p>' + '\n')
        # ingredients ul and li
        output_file.write('<ul>\n')
        while(True):
            
            # read next line
            line = input_file.readline().strip()
            
            # check if line = Instuctions
            if line == 'Instuctions':
                break
            output_file.write('<li>')
            if line[0] == '#':
                output_file.write('<h1>'+ line[1:] +'</h1>')
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
            if line[0] == '#':
                output_file.write('<h1>'+ line[1:] +'</h1>')
            else:
                output_file.write('<label><input type="checkbox">' + line + '</label>')
            output_file.write('</li>\n')
        output_file.write('</ul>\n</section>\n</article>')

        # close file