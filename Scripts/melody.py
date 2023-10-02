import win32api
import time

# Define the notes for our melody (frequency in Hz)
notes = {
    'C4': 262,
    'D4': 294,
    'E4': 330,
    'F4': 349,
    'G4': 392,
    'A4': 440,
    'B4': 494,
    'C5': 523
}

# Define the rhythm for our melody (duration in milliseconds)
rhythm = {
    'whole': 1600,
    'half': 800,
    'quarter': 400,
    'eighth': 200,
    'sixteenth': 100
}

# Define our melody as a list of tuples (note, rhythm)
melody = [
    ('C4', 'quarter'),
    ('D4', 'quarter'),
    ('E4', 'quarter'),
    ('F4', 'quarter'),
    ('G4', 'quarter'),
    ('A4', 'quarter'),
    ('B4', 'quarter'),
    ('C5', 'whole')
]

# Loop through the melody and play each note using the Beep method
for note, duration in melody:
    frequency = notes[note]
    duration_ms = rhythm[duration]
    win32api.Beep(frequency, duration_ms)
    # Pause briefly between notes
    time.sleep(0.1)
