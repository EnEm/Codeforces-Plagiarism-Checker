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

            for i in range(len(lines)):
                if lines[i].find(str(submission))!=-1:
                    urls.append({'match': int(lines[i][-8:-6]), 'moss_url': lines[i][ lines[i].find('\"') + 1 : lines[i].find( '\"' , lines[i].find('\"') + 1 ) ], 'cf_url': 'https://codeforces.com/contest/' + str(contest) + '/submission/' + lines[i+1][ lines[i+1].find('codes/') + 6 : lines[i+1].find( '.' , lines[i+1].find('codes/') +6) ]})
        except:
            file_start -= BLOCK_SIZE

    urls = sorted(urls, key = lambda k: k['match'], reverse = True)

    return urls