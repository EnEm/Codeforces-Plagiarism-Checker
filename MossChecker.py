import os
import requests
import time

def MossCheck(contest,submission,files):

    urls=[]

    BLOCK_SIZE=100

    print('Starting Comparing codes')

    for file_start in range(0,len(files),BLOCK_SIZE):

        command = 'perl moss.pl -l cc codes/' + str(submission) + '.cpp '

        for file_number in range( file_start , min( len(files) , file_start + BLOCK_SIZE ) ):

            if files[file_number][6:-4] != str(submission):

                command += files[file_number] + ' '

        stream = os.popen(command)
        output = stream.read().split('\n')

        print('Comparing Codes : ' + str(file_start+1) + '/' + str(len(files)) + ' on ' + output[-2])

        try:
            lines = requests.get(output[-2]).text.split('\n')

            for line in lines:
                if line.find(str(submission))!=-1:
                    urls.append(( int(line[-8:-6]) , line[ line.find('\"') + 1 : line.find( '\"' , line.find('\"') + 1 ) ] ))
        except:
            file_start -= BLOCK_SIZE

    urls.sort

    return urls