import os
import codecs

folders = ["food", "drinks", "desserts"]

for i in range(0,3):
    for x in os.listdir("input_raw/" + folders[i] + "/"):
        input_file = codecs.open("input_raw/" + folders[i] + "/" + x, encoding='utf-8', mode='r')
        line = input_file.readline()
        output_file = codecs.open("recipes/" + folders[i] + "/" + line.strip() + ".html",encoding='utf-8', mode='w+')
        output_file.write('<link rel="stylesheet" href="styles.css">' + '\n')
        output_file.write('<h1>' + line.strip() + '</h1>' + '\n')
        output_file.write('<article>' + '\n' + '<section id="ingredients">' + '\n' + '<h1>Ingredients</h1>' + '\n')
        line = input_file.readline()
        # ingredients ul and li
        output_file.write('<ul>\n')
        while(True):
            
            # read next line
            line = input_file.readline().strip()
            # check if line = Instuctions
            if line == 'Instructions':
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
            #if line starts with # make it a subcategory title
            if line.startswith('#'):
                output_file.write('<h1>'+ line[1:] +'</h1>')
            #if line starts with temp: make it 
            elif line.startswith("temp:"):
                output_file.write('<h1>'+ line [6:]+'</h1>')
            else:
                output_file.write('<label><input type="checkbox">' + line + '</label>')
            output_file.write('</li>\n')
        output_file.write('</ul>\n</section>\n</article>')
        # close file
for i in range(0,3):
    output_file = codecs.open("recipes/" + folders[i] + "_index.html",encoding='utf-8', mode='w+')

    output_file.write("<ul>\n")
    for x in os.listdir("input_raw/" + folders[i] + "/"):
        output_file.write('<il class="index">\n')
        output_file.write('<a href="/recipes/' + folders[i] + '/' + x[:-4] + '.html">')
        output_file.write(x[:-4] + "</a>\n")
        output_file.write("<ll>\n")
    output_file.write("</ul>\n")