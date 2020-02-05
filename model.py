import numpy as np
import pickle
<<<<<<< HEAD

=======
import nltk
import random
>>>>>>> 047c5a8e6fd6ff5d4064b15a3d2af201b9b0312d

class myBert():

    def __init__(self):
        self.words = []

    def get_probabilities(self, sentence):
        self.words = sentence.split(' ')
        scores = np.random.randint(10, size=len(self.words))
        probs  = scores /np.sum(scores)
        sent_probs = { word : probs[indx] for indx, word in enumerate(self.words)}
        result={}
        result['sentence_probs'] = sent_probs
        for head in range(12):
            result['head_#'+str(head)] = np.random.rand(len(self.words),len(self.words)).tolist()
        return result

<<<<<<< HEAD

#class myHMM():
#    def __init__(self):
#        self.model = pickle.load(open('cprob_nkra', 'rb'))
#        
#    def get_propobabilities(self, sentence):
#        self.words = sentence.split(' ')
#        sentence_probs = {self.words[0]: 0}
#        for indx, word in enumerate(self.words[:-1])
#            sentence_probs[word] = self.model[word].prob(self.words[indx+1])
#        return setence_probs
        
=======
class myHMM():

    def __init__(self):
        with open('./cprob_nkra', 'rb') as f:
            self.HMM = pickle.load(f)

    def get_words(self, word, count = 10):
        self.clear = str(word).strip()
        d = self.HMM[self.clear].freqdist()
        result = sorted(d.items(), key=lambda x: x[1],reverse=True)[:count]
        if result == []:
            return random.choice(list(self.HMM))
        else:
            result = [{i:j} for i,j in result]
            return result
>>>>>>> 047c5a8e6fd6ff5d4064b15a3d2af201b9b0312d
