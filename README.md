# scaletheorymapper

Basic python3 framework for mapping chords and scale types to keys

The device independent "theory" portion chan be viewed like this:

## Example:  just run the notes.py file
```
import chromatics as c

for i in ['C', 'D', 'E', 'F', 'G', 'A', 'B']:
	c.showScaleNotes(scale='major', key=i)
	c.showScaleNotes(scale='minor', key=i)
	c.showScaleNotes(scale='pentMajor', key=i)
	c.showScaleNotes(scale='pentMinor', key=i)
	c.showScaleNotes(scale='hexBlues', key=i)
```

```
| => python3 notes.py
2017-05-03 15:24:51,670 - DEBUG - Cmajor : ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C']
2017-05-03 15:24:51,670 - DEBUG - Cminor : ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb', 'C']
2017-05-03 15:24:51,671 - DEBUG - CpentMajor : ['C', 'D', 'E', 'G', 'A', 'C']
2017-05-03 15:24:51,671 - DEBUG - CpentMinor : ['C', 'Eb', 'F', 'G', 'Bb', 'C']
2017-05-03 15:24:51,671 - DEBUG - ChexBlues : ['C', 'Eb', 'F', 'Gb', 'G', 'Bb', 'C']
2017-05-03 15:24:51,671 - DEBUG - Dmajor : ['D', 'E', 'F#', 'G', 'A', 'B', 'C#', 'D']
2017-05-03 15:24:51,671 - DEBUG - Dminor : ['D', 'E', 'F', 'G', 'A', 'A#', 'C', 'D']
2017-05-03 15:24:51,671 - DEBUG - DpentMajor : ['D', 'E', 'F#', 'A', 'B', 'D']
2017-05-03 15:24:51,671 - DEBUG - DpentMinor : ['D', 'F', 'G', 'A', 'C', 'D']
2017-05-03 15:24:51,671 - DEBUG - DhexBlues : ['D', 'F', 'G', 'G#', 'A', 'C', 'D']
2017-05-03 15:24:51,671 - DEBUG - Emajor : ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#', 'E']
2017-05-03 15:24:51,671 - DEBUG - Eminor : ['E', 'F#', 'G', 'A', 'B', 'C', 'D', 'E']
2017-05-03 15:24:51,671 - DEBUG - EpentMajor : ['E', 'F#', 'G#', 'B', 'C#', 'E']
2017-05-03 15:24:51,672 - DEBUG - EpentMinor : ['E', 'G', 'A', 'B', 'D', 'E']
2017-05-03 15:24:51,672 - DEBUG - EhexBlues : ['E', 'G', 'A', 'A#', 'B', 'D', 'E']
2017-05-03 15:24:51,672 - DEBUG - Fmajor : ['F', 'G', 'A', 'Bb', 'C', 'D', 'E', 'F']
2017-05-03 15:24:51,672 - DEBUG - Fminor : ['F', 'G', 'Ab', 'Bb', 'C', 'Db', 'Eb', 'F']
2017-05-03 15:24:51,672 - DEBUG - FpentMajor : ['F', 'G', 'A', 'C', 'D', 'F']
2017-05-03 15:24:51,672 - DEBUG - FpentMinor : ['F', 'Ab', 'Bb', 'C', 'Eb', 'F']
2017-05-03 15:24:51,672 - DEBUG - FhexBlues : ['F', 'Ab', 'Bb', 'B', 'C', 'Eb', 'F']
2017-05-03 15:24:51,672 - DEBUG - Gmajor : ['G', 'A', 'B', 'C', 'D', 'E', 'F#', 'G']
2017-05-03 15:24:51,672 - DEBUG - Gminor : ['G', 'A', 'A#', 'C', 'D', 'D#', 'F', 'G']
2017-05-03 15:24:51,672 - DEBUG - GpentMajor : ['G', 'A', 'B', 'D', 'E', 'G']
2017-05-03 15:24:51,672 - DEBUG - GpentMinor : ['G', 'A#', 'C', 'D', 'F', 'G']
2017-05-03 15:24:51,673 - DEBUG - GhexBlues : ['G', 'A#', 'C', 'C#', 'D', 'F', 'G']
2017-05-03 15:24:51,673 - DEBUG - Amajor : ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#', 'A']
2017-05-03 15:24:51,673 - DEBUG - Aminor : ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'A']
2017-05-03 15:24:51,673 - DEBUG - ApentMajor : ['A', 'B', 'C#', 'E', 'F#', 'A']
2017-05-03 15:24:51,673 - DEBUG - ApentMinor : ['A', 'C', 'D', 'E', 'G', 'A']
2017-05-03 15:24:51,673 - DEBUG - AhexBlues : ['A', 'C', 'D', 'D#', 'E', 'G', 'A']
2017-05-03 15:24:51,673 - DEBUG - Bmajor : ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#', 'B']
2017-05-03 15:24:51,673 - DEBUG - Bminor : ['B', 'C#', 'D', 'E', 'F#', 'G', 'A', 'B']
2017-05-03 15:24:51,673 - DEBUG - BpentMajor : ['B', 'C#', 'D#', 'F#', 'G#', 'B']
2017-05-03 15:24:51,673 - DEBUG - BpentMinor : ['B', 'D', 'E', 'F#', 'A', 'B']
2017-05-03 15:24:51,673 - DEBUG - BhexBlues : ['B', 'D', 'E', 'F', 'F#', 'A', 'B']
```

## Python on the Cell Phone 
I have been experimenting with Python3 on my IOS devices through the Pythonista app.  Pythonista has a simple sound module, and this script applies some of the theory to drive the sound module by playing tone sequences (scales, chords, arpeggio chord progressions, etc.).

```
### Run blue6.py from the Pythonista editor.
Inspect the last few lines for other demo sequences.

 pentMajor: ['C', 'D', 'E', 'G', 'A', 'C']
 pentMajor: ['G', 'A', 'B', 'D', 'E', 'G']
 pentMajor: ['D', 'E', 'F#', 'A', 'B', 'D']
 pentMajor: ['A', 'B', 'C#', 'E', 'F#', 'A']
 pentMajor: ['E', 'F#', 'G#', 'B', 'C#', 'E']
 pentMajor: ['B', 'C#', 'D#', 'F#', 'G#', 'B']
 pentMajor: ['F#', 'G#', 'A#', 'C#', 'D#', 'F#']
 pentMajor: ['C#', 'D#', 'F', 'G#', 'A#', 'C#']
 pentMajor: ['G#', 'A#', 'C', 'D#', 'F', 'G#']
 pentMajor: ['D#', 'F', 'G', 'A#', 'C', 'D#']
 pentMajor: ['A#', 'C', 'D', 'F', 'G', 'A#']
 pentMajor: ['F', 'G', 'A', 'C', 'D', 'F']

```