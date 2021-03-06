import sys
import os
from SubmissionFetcher import subFetch
from SubmissionDownloader import subDownload
from MossChecker import mossCheck


def PlagCheck(contest,submission):

    submissions = subFetch( contest , submission )

    if not os.path.exists('codes'):
        os.makedirs('codes')

    files = subDownload( contest , submission , submissions )

    urls = mossCheck( contest , submission , files )

    return urls


if __name__ == "__main__":    
    contest = None
    submission = None

    if len(sys.argv)==1:
        contest = int(input('Enter the contest id ( not the round number ): '))
        submission = int(input('Enter the submission id : '))
    elif len(sys.argv)==3:
        contest = int(sys.argv[1])
        submission = int(sys.argv[2])
    else:
        raise Exception('Provide proper arguments')

    urls = PlagCheck( contest , submission)

    fw=open('result.csv','w')

    for url in urls:
        print(str(url['match']) + ' , ' + url['moss_url'] + ' , ' + url['cf_url'] )
        fw.write(str(url['match']) + ' , ' + url['moss_url'] + ' , ' + url['cf_url']  + '\n' )

    fw.close()
