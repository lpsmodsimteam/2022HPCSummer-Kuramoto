from tracemalloc import start
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import pylab as pl

# helpful https://new.pythonforengineers.com/blog/audio-and-digital-signal-processingdsp-in-python/
# also https://datacrayon.com/posts/signal-processing/sp-basics/sine-waves-in-the-time-domain/
# also https://en.wikipedia.org/wiki/Phase_synchronization

'''
This is a rough implentation of an algorithm that will detect which oscillators in a set are synchronized and which are not.
It can be expanded on and optimized. It could also be a step in the wrong direction for detecting synchronization of more complicated oscillators.
It has only been tested on simple harmonic oscillators.
This implementation assumes that the user already knows the frequency and amplitudes of each oscillator in the set
'''

# Signal Parameters
frequency = 1
num_samples = 1000
sampling_rate = 1000
amplitude = 1
theta = 0

# Time Parameters (Seconds)
start_time = 0
end_time = 10
time = np.arange(start_time, end_time, 1/sampling_rate)

# Create simple harmonic oscillators
sine_wave = amplitude * np.sin(2 * np.pi * frequency * time + theta) 
cos_wave = amplitude * np.sin(2 * np.pi * frequency * time + theta)

# Pre-determine the amplitude of the oscillators before analyzing them.
sine_peak = max(sine_wave)
cos_peak = max(cos_wave)

# Add the oscillators to a signals list.
signals = []
signals.append(sine_wave)
signals.append(cos_wave)

# Add the oscillator's amplitude to the signals_peak list in the same order the oscillators were added to the signals list.
signals_peaks = []
signals_peaks.append(sine_peak)
signals_peaks.append(cos_peak)

# Set total number of signals.
num_signals = len(signals)

# Create list to store time in which oscillator's first peak is found during sampling.
signals_peak_times = [0] * num_signals

# Create list to store phase difference of each oscillator in reference to the reference oscillator.
signals_phase_diff = [0] * num_signals

# Reference peak time and if it was found.
ref_peak_time = 0
ref_peak_found = False

# A list of boolean values associated with each oscillator and if its peak has been found.
signals_peak_found = [False for ts in range(num_signals)]

# Number of peaks found.
peaks_found = 0 

print(f"Parameters:\nFrequency: {frequency}\nNumber of Samples: {num_samples}\nSampling Rate: {sampling_rate}\nAmplitude: {amplitude}\nOffset: {theta}\nNumber of Signals: {num_signals}\n")
print(f"Starting Time: {start_time}\nEnding Time: {end_time}\nStride: {1/sampling_rate}\n")
print(f"Begin Sampling...")
# Sample the entire time duration of time. (ts = step in time)
for ts in range(len(time)): # this should be changed to scan through one period

    # If the first peak for all signals are found, end sampling.
    if peaks_found == num_signals:
        break

    # For each step in time, loop through every oscillator and check its value.
    for curr_signal in range(num_signals): 

        # If the first peak for current oscillator has already been found, continue to the next oscillator in the list.
        if signals_peak_found[curr_signal] == True:
            continue

        # If the current oscillator's value is equal to its amplitude, its first peak has been found.
        if signals[curr_signal][ts] == signals_peaks[curr_signal]:

            # If this is the first peak found in the list of oscillators, the oscillator being analyzed current will become the reference oscillator.
            if not ref_peak_found:

                # Track the time in which the reference oscillator's first peak occured.
                ref_peak_time = time[ts]
                ref_peak_found = True

                # As it is the reference oscillator, its phase difference is with itself so its zero.
                signals_phase_diff[curr_signal] = 0
                print(f"Signal {curr_signal}: Peak at time: {time[ts]}, Reference Signal.")

            # Reference oscillator has already been found, go here.
            else:

                # The phase difference for the currently analyzed oscillator will be the time of its first peak, subtracted from the time of the reference oscillator's first peak multipled by 2pi.
                signals_phase_diff[curr_signal] = (time[ts] - ref_peak_time) * (2 * np.pi) 
                print(f"Signal {curr_signal}: Peak at time: {time[ts]}, Phase diff to ref: {signals_phase_diff[curr_signal]}.")
            
            # For debugging.
            signals_peak_times[curr_signal] = time[ts]

            # Stop further analysis of this oscillator since its peak was found.
            signals_peak_found[curr_signal] = True

            # Increment peaks found.
            peaks_found += 1


#POST PROCESSING/ANALYZING
print("\nSampling and Measuring finished. Comparing phase differences:")

# Loop through each oscillator's phase difference with the reference oscillator.
for curr_signal in range(num_signals):

    # Compare the oscillator's phase difference with oscillators stored after it.
    # This prevents oscillator A comparing with Oscillator B and then Oscillator B comparing with Oscillator A
    for i in range(curr_signal, num_signals - 1):
        # TODO, check for antiphase as well.
        if signals_phase_diff[curr_signal] == signals_phase_diff[i + 1]:
            print(f"Signal {curr_signal} is synchronized with Signal {i + 1}")
        else:
            print(f"Signal {curr_signal} is not synchronized with Signal {i + 1}")