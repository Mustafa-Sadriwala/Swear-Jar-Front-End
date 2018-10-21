
import time
import pandas as pd
import json


from rev_ai.speechrec import RevSpeechAPI


class revSpeechmod:
    def __init__(self):
        self.swearWords = []
        self.client = RevSpeechAPI('01DuAIahoMCykRyp2-xV6GC9BqjbtELzeh7GCiQ2DlfMdihYRTui2cTt1D9kOjPZHhrHLEa87RfnFdii-9Cy4v1n3-Mdc')
    def await_transcript(client, id_):
       while client.view_job(id_)['status'] == 'in_progress':
           print('waiting...')
           time.sleep(5)
       return client.get_transcript(id_)
    def addSwears(x, self):
        self.swearWords.append(x)
    def removeSwear(x,self):
        self.swearWords.remove(x)
    def getTranscript(self, file):
        result = self.client.submit_job_local_file(file)
        transcript = self.await_transcript(self.client, result['id'])
        print(transcript)
        print(transcript['monologues'][0]['elements'][:10])
        with open('data.json', 'w') as fp:
            json.dump(transcript, fp)
        return transcript

    def checkSwears(self, file, transcript = ""):
        if(transcript == ""):
            transcript = self.getTranscript(file)
        df = pd.Dataframe.from_dict(transcript)


