fname = input('Enter the mailbox file name: ')


try:
    in_file = open(fname)
    outfname = input('Enter the output file name: ')
    out_file = open(outfname, 'w')
except:  #FileNotFoundError:
    print('That file was not found.')
    quit()
else:
    for a_line in in_file:
        if a_line.startswith('From:') and a_line.find('uct.ac.za') != -1:
            #print(a_line, end='')
            #a_line = a_line.strip()
            #print(a_line)
            out_file.write(a_line)



if in_file != None:
    in_file.close()
if out_file != None:
    out_file.close()
