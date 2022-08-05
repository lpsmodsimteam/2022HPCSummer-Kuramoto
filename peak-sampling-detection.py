from tracemalloc import start
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import pylab as pl

# helpful https://new.pythonforengineers.com/blog/audio-and-digital-signal-processingdsp-in-python/
# also https://datacrayon.com/posts/signal-processing/sp-basics/sine-waves-in-the-time-domain/



frequency = 1
num_samples = 1000
sampling_rate = 1000
amplitude = 1
theta = 0

start_time = 0
end_time = 10
time = np.arange(start_time, end_time, 1/sampling_rate)

sine_wave = amplitude * np.sin(2 * np.pi * frequency * time + theta) 
cos_wave = amplitude * np.cos(2 * np.pi * frequency * time + theta)

sine_wave_two = amplitude * np.sin(2 * np.pi * frequency * time + theta) 
cos_wave_two = amplitude * np.cos(2 * np.pi * frequency * time + theta)

sine_peak = max(sine_wave)
cos_peak = max(cos_wave)

signals = []
signals.append(sine_wave)
signals.append(cos_wave)
signals.append(sine_wave_two)
signals.append(cos_wave_two)

signals_peaks = [sine_peak, cos_peak, sine_peak, cos_peak]
num_signals = len(signals)
print(num_signals)

signals_peak_times = [0] * num_signals
signals_phase_diff = [0] * num_signals

#algorithm:
#enable sampling at some arbitrary time in simulation
#step through time
#first peak measured becomes the reference wave.

#SAMPLING PORTION
ref_peak_time = 0
ref_peak_found = False

signals_peak_found = [False for i in range(num_signals)]

peaks_found = 0 # this logic should be removed when (A) is done

print(f"Parameters:\nFrequency: {frequency}\nNumber of Samples: {num_samples}\nSampling Rate: {sampling_rate}\nAmplitude: {amplitude}\nOffset: {theta}\n")
print(f"Starting Time: {start_time}\nEnding Time: {end_time}\nStride: {1/sampling_rate}\nNumber of Signals: {num_signals}\n")

print(f"Begin Sampling...")
for i in range(len(time)): # (A) this should be changed to scan through one period
    if peaks_found == num_signals:
        break
    for n in range(num_signals): 
        if signals_peak_found[n] == True:
            continue
        if signals[n][i] == signals_peaks[n]:
            if not ref_peak_found:
                ref_peak_time = time[i]
                ref_peak_found = True            
                signals_peak_times[n] = time[i]
                signals_phase_diff[n] = 0
                print(f"Signal {n}: Peak at time: {time[i]}, Reference Signal.")
                signals_peak_found[n] = True
                peaks_found += 1
            else:
                signals_peak_times[n] = time[i]
                signals_phase_diff[n] = (time[i] - ref_peak_time) * (2 * np.pi) 
                print(f"Signal {n}: Peak at time: {time[i]}, Phase diff to ref: {signals_phase_diff[n]}.")
                signals_peak_found[n] = True
                peaks_found += 1
        if peaks_found == num_signals:
            break

#POST PROCESSING/ANALYZING
'''
for n in range(num_signals):
    if signals_phase_diff[n] == 0 or signals_phase_diff[n] == (np.pi): 
        print(f"Signal {n} is synchronized with reference")
    else:
        print(f"Signal {n} is not synchronized with reference")
'''
print("\nSampling and Measuring finished. Comparing phase differences:")
for n in range(num_signals):
    for i in range(n, num_signals - 1):
        if signals_phase_diff[n] == signals_phase_diff[i + 1]:
            print(f"Signal {n} is synchronized with Signal {i + 1}")
        else:
            print(f"Signal {n} is not synchronized with Signal {i + 1}")

#for i in range(len(sine_wave)):
#    print(sine_wave[i])

#plt.plot(sine_wave[:100], color="red")


'''
total_signals = 2

x = pl.arange(0, 6.28, 0.01)
signal_0 = pl.sin(x)
signal_1 = pl.cos(x)

signal_0_amp = max(signal_0)
signal_1_amp = max(signal_1)

signals = []
signals.append(signal_0)
signals.append(signal_1)

print(signals)


pl.plot(x, signals[0])
pl.plot(x, signals[1])
pl.show()
'''
#plt.show()