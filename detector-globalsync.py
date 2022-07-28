''' 
    Simple method of detecting global synchronization of two-state oscillators with the same periods
    Oscillators are on the same clock boundary.

    Program loops through each step of the oscillator and compares its peak with a reference signal (Arbitrary chosen to be oscillator 0).
    If any value does not match, then the oscillators are not globally synchronized.

    Runs at O(n * m) where n is the number of oscillators and m is the clock boundary.
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

# Initially declare synchronized to be true.
synchronized = True

# Loop down each column of each signal.
for i in range(len(signals[0])):

    ref_peak = signals[0][i] # The reference peak is obtained from the first signal in data.
                             # Its peak will be compared with all other signals.

    # Check if each signal matches the reference signal.
    for x in range(len(signals)):
        if signals[x][i] != ref_peak:
            print("Not synced at " + str(i))
            synchronized = False
            break 

    # If all signals are not globally synchronized, break out early.
    if not synchronized:
        break

if synchronized:
    print("Global Synchronization is occuring")
else:
    print("Global Synchronization is not occuring")
            




 
 




