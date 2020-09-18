from collections import deque
import numpy as np

class Averager(object):
    def __init__(self, sz, numSamples):
        self.numSamples = numSamples if numSamples >= 2 else 2
        
        zeros = np.zeros(sz, dtype='float64')
        self.__sigs = deque(self.numSamples * [zeros], self.numSamples)
        self.__sum  = zeros

    def calc(self, newsig):
        if not self._isndarray(newsig):
            newsig = np.array(newsig, dtype='float64')

        self.__sum += newsig
        self.__sigs.append(newsig)
        self.__sum -= self.__sigs[0];

        av = self.__sum / self.numSamples
           
        return av

    def _isndarray(self, arr):
        return isinstance(arr, np.ndarray)
