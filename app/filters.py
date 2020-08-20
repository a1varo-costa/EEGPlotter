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

def lowPass(sig, fs, fc):
    ''' Perform a one pole low pass filter '''
    
    time_const = 1./(2*np.pi*fc)
    dt = 1./fs
    alpha = dt / (time_const + dt)

    y = np.zeros_like(sig)
    y[0] = alpha * sig[0]

    for k in range(len(y)):
        y[k] = y[k-1] + alpha * (sig[k] - y[k-1])
        
    return y

def highPass(sig, fs, fc):
    ''' Perform a one pole high pass filter '''

    time_const = 1./(2*np.pi*fc + 10e-20)
    dt = 1./fs
    alpha = time_const / (time_const + dt)

    y = np.zeros_like(sig)
    y[0] = sig[0]

    for k in range(len(y)):
        y[k] = alpha * (y[k-1] + sig[k] - sig[k-1])
        
    return y
