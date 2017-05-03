# scaletheorymapper

Basic python3 framework for mapping chords and scale types to keys

## Example:  just run the notes.py file

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