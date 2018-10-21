
import time
import json
import re



from rev_ai.speechrec import RevSpeechAPI


class revSpeechmod:
    def __init__(self, transcript = ""):
        if transcript != "":
            with open(transcript, 'r') as fp:
                self.transcript = json.load(fp)
                print(self.transcript)
        self.swearWords=[]
        self.client = RevSpeechAPI('01DuAIahoMCykRyp2-xV6GC9BqjbtELzeh7GCiQ2DlfMdihYRTui2cTt1D9kOjPZHhrHLEa87RfnFdii-9Cy4v1n3-Mdc')
    def await_transcript(self, client, id_):
       while client.view_job(id_)['status'] == 'in_progress':
           print('waiting...')
           time.sleep(5)
       return client.get_transcript(id_)
    def setSwears(self, x):
        self.swearWords=[]
        with open(x, 'r') as fp:
            swears = json.load(fp)
            for a in swears:
                self.swearWords.append(a.lower())
    def getTranscript(self, file):
        result = self.client.submit_job_local_file(file)
        transcript = self.await_transcript(self.client, result['id'])
        print(transcript)
        print(transcript['monologues'][0]['elements'][:10])
        with open(str(file) + ".json", 'w') as fp:
            json.dump(transcript, fp)
        return transcript
    def setTranscript(self, file):
        self.transcript = file
    def checkSwears(self, file = ""):
        swears = 0;
        if(file != ""):
            self.transcript = self.getTranscript(file)
        bagOfWords = []
        x = self.transcript['monologues'][0]['elements']
        for i in x:
            if(re.search('[a-zA-Z]', i['value'])!=None):
                a = i['value'].lower()
                words = a.split(' ')
                for i in words:
                    bagOfWords.append(i)
        for i in bagOfWords:
            print(i)
            if i in self.swearWords:
                swears +=1
        print(swears)
