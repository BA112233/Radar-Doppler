#Lulu's answer for Q4
import numpy as np
import matplotlib.pyplot as plt

T = 3 #duration (s)
LFMrate = 10 #frequency rate (Hz/s)
oversampling = 20 #oversampling ratio

def LFM(T, LFMrate, oversampling):
    """
    Parameters:
        T: integer
            duration of the signal
        LFMrate: integer
            rate of linear frequency modulation
        oversampling: integer
            Oversampling ratio
    Returns:
        u: array
            LFW waveform
        t: array
            times at which LFM waveform was evaluated at
    """
    bandwidth = LFMrate * T
    f = oversampling * bandwidth # sampling frequency
    
    t = np.arange(0, T, 1/f)
    u = np.exp(1j*2*np.pi*(0.5*LFMrate)*t**2)
    return u, t

u, t = LFM(T, LFMrate, oversampling)

plt.plot(t, u.real)
plt.title('Linear Frequency Modulated Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (Real)')
plt.show()

def FT(t, u, T, LFMrate, oversampling):
    """
    Parameters:
        t: array
            Array of times of the wave
        u: array
            Array of wave amplitudes
        T: integer
            Duration of the wave
        LFMrate: integer
            Rate of linear frequency modulation
        oversampling: integer
            Ratio of oversampling
    Returns:
        FFTres: array
            Fourier transform magnitudes
        FFTfreq: array
            Fourier transform frequencies
    """
    f = oversampling * LFMrate * T #sampling frequency
    FFTfreq = np.fft.fftfreq(len(t), d=1/f)
    FFTres = np.fft.fft(u)
    
    return FFTres, FFTfreq

FFTres, FFTfreq = FT(t, u, T, LFMrate, oversampling)


beat = 0.0001
#r = beat/(2*LFMrate)
r = beat * 3*10**8 * 3/(2 * LFMrate * 3)
print(f'The range is {r:.2f} m')


plt.plot(FFTfreq, 10*np.log(np.abs(FFTres)))
plt.title('Fourier Transform of LFM wave')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude, log')
plt.xlim([-400,400])
plt.grid(True)
plt.show()

