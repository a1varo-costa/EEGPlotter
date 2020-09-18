from scipy import signal
import numpy as np

def fftUtil(x, y, d=None):
    ''' Perform FFT in input data '''

    if d is None:
        dx = np.diff(x)
        uniform = not np.any(np.abs(dx-dx[0]) > (abs(dx[0]) / 1000.))
        
        if not uniform:
            x2 = np.linspace(x[0], x[-1], len(x))
            y = np.interp(x2, x, y)
            x = x2
            d = float(x[-1]-x[0]) / (len(x)-1)

    n = len(y)
    f = np.fft.rfft(y) / n
    
    x = np.fft.rfftfreq(n, d)
    y = np.abs(f)
   
    return x, y

def butterworth(sig, fs, fc, order, fopt='low'):
    ''' Perform Butterworth Low/High/Band Pass Filter '''

    if (__validCutoff(fs, fc)):
        fc = __normalize(fc, fs/2) # normalize fc
        b, a = signal.butter(order, fc, fopt)
        out = signal.filtfilt(b, a, sig)
        return out
        
    else:
        return sig

def __validCutoff(fs, fc):
    try:
        isValid = True
        for i in fc:
            isValid = isValid and (i > 0 and i <= fs/2)
        return isValid
    except:
        return fc > 0 and fc <= fs/2

def __normalize(a, b):
    try:
        a = [x/b for x in a]
        return a
    except:
        return a/b
