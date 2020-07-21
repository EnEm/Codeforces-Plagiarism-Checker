import requests
import json

def subFetch(contest,submission):

    print('Fetching submission ids')
            
    r = requests.get( 'https://codeforces.com/api/contest.status?contestId=' + str(contest) )

    problem = None

    for sub in r.json()['result']:
        if sub['id'] == submission:
            problem = sub['problem']

    if problem == None:
        raise Exception('Submission not in this Contest.')

    submissions=[]

    for sub in r.json()['result']:
        if sub['problem'] == problem and sub['verdict'] == 'OK':
            submissions.append( sub['id'] )
            
    print('Completed Submissions Fetching')

    return submissions