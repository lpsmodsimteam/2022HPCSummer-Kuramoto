''' 
    Simple method of detecting global synchronization of two-state oscillators with the same periods
    Oscillators are on the same clock boundary.

    Program adds up the signals and checks that all states have amplitude 0 or the summation of all signal's amplitudes. 
    
    Runs at O(n + m) where n is the number of oscillators and m is the clock boundary.

    Naive implementation: Only works on up to 9 oscillators in a set.
'''

# Open 'simulated' oscillator data and read it into the signals list.
signals = []
with open("oscillators_that_are_synchronized.dat") as f:
    signals = f.readlines()

# Convert the oscillator data into a string that can be indexed for certain cycles of time in the sample.
# (i.e) signals[0][4] returns the first oscillators state at cycle 4.
for i in range(len(signals)):
    signals[i] = str(signals[i].strip())
    
# Debug -> Print out each column horizontally into console.
for i in range(len(signals[0])):
    for y in range(len(signals)):
        print(signals[y][i], end = " ")
    print(f"Time: {i} unit")

num_signals = len(signals) # Obtain number of signals being analyzed
amplitude = 1 # Amplitude of all signals.

print(num_signals * amplitude)

# Add signals together into one signal
result_signal = 0
for i in range(len(signals)):
    result_signal += int(signals[i]) 

# Convert resulting signal to a string so it can be indexed.
result_signal = str(result_signal)

print(result_signal)

# Initially declare synchronized to be true.
synchronized = True

# Assuming all signals share the same clock boundary, loop through the resulting signal and check
# that the resulting signal only contains 0 and (amplitude * num_signals).
for i in range(len(result_signal)):
    if int(result_signal[i]) is not (0 or 9):
        print(f"{result_signal[i]}")
        synchronized = False
        break

if synchronized:
    print("Global Synchronization is occuring")
else:
    print("Global Synchronization is not occuring")