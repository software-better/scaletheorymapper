# Play a blues melody on Pythonista on the iPad (iOS)
import sound
import time
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(message)s')

# notes as understood by the ios sound module
player_notes = {
    'C': ['C3', 'C3#', 'D3', 'D3#', 'E3', 'F3', 'F3#', 'G3', 'G3#', 'A3', 'A3#', 'B3', 'C4'],
    'C#': ['C3#', 'D3', 'D3#', 'E3', 'F3', 'F3#', 'G3', 'G3#', 'A3', 'A3#', 'B3', 'C3', 'C4#'],
    'Db': ['C3#', 'D3', 'D3#', 'E3', 'F3', 'F3#', 'G3', 'G3#', 'A3', 'A3#', 'B3', 'C3','C4#'],
    'D': ['D3', 'D3#', 'E3', 'F3', 'F3#', 'G3', 'G3#', 'A3', 'A3#', 'B3', 'C3', 'C3#', 'D4'],
    'D#': ['D3#', 'E3', 'F3', 'F3#', 'G3', 'G3#', 'A3', 'A3#', 'B3', 'C3', 'C3#', 'D3','D4#'],
    'Eb': ['D3#', 'E3', 'F3', 'F3#', 'G3', 'G3#', 'A3', 'A3#', 'B3', 'C3', 'C3#', 'D3', 'D4#'],
    'E': ['E3', 'F3', 'F3#', 'G3', 'G3#', 'A3', 'A3#', 'B3', 'C3', 'C3#', 'D3', 'D3#', 'E4'],
    'F': ['F3', 'F3#', 'G3', 'G3#', 'A3', 'A3#', 'B3', 'C3', 'C3#', 'D3', 'D3#', 'E3', 'F4'],
    'F#': ['F3#', 'G3', 'G3#', 'A3', 'A3#', 'B3', 'C3', 'C3#', 'D3', 'D3#', 'E3', 'F3', 'F4#'],
    'Gb': ['F3#', 'G3', 'G3#', 'A3', 'A3#', 'B3', 'C3', 'C3#', 'D3', 'D3#', 'E3', 'F3', 'F4#'],
    'G': ['G3', 'G3#', 'A3', 'A3#', 'B3', 'C3', 'C3#', 'D3', 'D3#', 'E3', 'F3', 'F3#','G4#'],
    'G#': ['G3#', 'A3', 'A3#', 'B3', 'C3', 'C3#', 'D3', 'D3#', 'E3', 'F3', 'F3#', 'G3', 'G4#'],
    'Ab': ['G3#', 'A3', 'A3#', 'B3', 'C3', 'C3#', 'D3', 'D3#', 'E3', 'F3', 'F3#', 'G3', 'G4#'],
    'A': ['A3', 'A3#', 'B3', 'C3', 'C3#', 'D3', 'D3#', 'E3', 'F3', 'F3#', 'G3', 'G3#', 'A3'],
    'A#': ['A3#', 'B3', 'C3', 'C3#', 'D3', 'D3#', 'E3', 'F3', 'F3#', 'G3', 'G3#', 'A3', 'A3#'],
    'Bb': ['A3#', 'B3', 'C3', 'C3#', 'D3', 'D3#', 'E3', 'F3', 'F3#', 'G3', 'G3#', 'A3', 'A3#'],
    'B': ['B3', 'C3', 'C3#', 'D3', 'D3#', 'E3', 'F3', 'F3#', 'G3', 'G3#', 'A3', 'A3#', 'B3'],
}

# for printout of tones matching key
sharpChromaticScales = {
    'C#' : ['C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#','A','A#','B', 'C', 'C#'],
    'D' : ['D', 'D#', 'E', 'F', 'F#', 'G', 'G#','A','A#','B', 'C', 'C#', 'D'],
    'D#' : ['D#', 'E', 'F', 'F#', 'G', 'G#','A','A#','B', 'C', 'C#', 'D', 'D#'],
    'E' : ['E', 'F', 'F#', 'G', 'G#','A','A#','B', 'C', 'C#', 'D', 'D#', 'E'],
    'F#' : ['F#', 'G', 'G#','A','A#','B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#'],
    'G' : ['G','G#','A','A#','B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G'],
    'G#' : ['G#','A','A#','B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#'],
    'A' : ['A','A#','B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#','A'],
    'A#' : ['A#','B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#','A','A#'],
    'B' : ['B','C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#','A','A#','B'],
}

flatChromaticScales = {
    'C' : ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab','A','Bb','B','C'],
    'Db' : ['Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab','A','Bb','B', 'C', 'Db'],
    'Eb' : ['Eb', 'E', 'F', 'Gb', 'G', 'Ab','A','Bb','B', 'C', 'Db', 'D', 'Eb'],
    'F' : ['F','Gb', 'G', 'Ab','A','Bb','B', 'C', 'Db','D', 'Eb', 'E', 'F'],
    'Gb' : ['Gb', 'G', 'Ab','A','Bb','B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb'],
    'Ab' : ['Ab','A','Bb','B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab'],
    'Bb' : ['Bb','B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab','A','Bb'],
    # 'C' : ['C','C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#','A','A#','B', 'C'],
}

# scales used loosely for tone patterns
scales = {
    'major': [0, 2, 4, 5, 7, 9, 11, 12],
    'minor': [0, 2, 3, 5, 7, 8, 10, 12],
    'hexBlues': [0, 3, 5, 6, 7, 10, 12],
    'pentMajor': [0, 2, 4, 7, 9, 12],
    'pentMinor': [0, 3, 5, 7, 10, 12],
    'bnotes': [0, 4, 7, 9, 10, 9, 7, 4], # basis of chord change sequences
    'tnotes': [0, 4, 7, 10, 0, 10, 7, 4],
}

def findNotes(key, player=False):
    L = []
    if key in flatChromaticScales.keys():
        L = flatChromaticScales[key]
    if key  in sharpChromaticScales.keys():
        L = sharpChromaticScales[key]
    if player:
        L = player_notes[key]
    return L

# break this into two functions
def showScaleNotes(scale='major', key='C', player=False):
    result = []
    notes = findNotes(key)
    #logging.debug(keyScaleNotes)
    for i in scales[scale]:
        result.append(notes[i])
    logging.debug(scale + ": " + str(result))
    return result

def playScaleNotes(scale='major', key='C', player=True):
    result = []
    notes = findNotes(key, True)
    #logging.debug(keyScaleNotes)
    for i in scales[scale]:
        result.append(notes[i])
    #logging.debug(key + scale + " : " + str(result))
    return result

def playNotes(inNotes, inWithEmphisis=False):
    for note in inNotes:
      sound.play_effect('Piano_' + note)
      if (inWithEmphisis):
          time.sleep(0.25)
          sound.play_effect('Piano_' + note)
          time.sleep(0.25)
      else:
        time.sleep(0.3)

fifths = {
	'A': 'E',
	'E': 'B',
	'B': 'F#',
	'F#': 'C#',
	'C#': 'G#',
	'G#': 'D#',
	'D#': 'A#',
	'A#': 'F',	
	'Gb': 'C#',
	'Db': 'G#',
	'Ab': 'D#',
	'Eb': 'A#',
	'Bb': 'F',
	'F': 'C',
	'C': 'G',
	'G': 'D',
	'D': 'A',
}
def circleOfFifths(scale):
	r = []
	k = 'C'
	keys = ['A', 'B','C','D','E','F','G','Bb','Eb','Ab','Db','Gb']
	for i in keys:
		showScaleNotes(scale, k)
		playNotes(playScaleNotes(scale, key=k, player=True))
		k = fifths[k]
	return r

# x for i in ['C', 'D', 'E', 'F', 'G', 'A', 'B']:
def demoScales(key):
	  showScaleNotes(scale='major', key=key)
	  showScaleNotes(scale='minor', key=key)
	  showScaleNotes(scale='pentMajor', key=key)
	  showScaleNotes(scale='pentMinor', key=key)
	  showScaleNotes(scale='hexBlues', key=key)
	  r = []
	  r += playScaleNotes(scale='major', key=key, player=True)
	  r += playScaleNotes(scale='minor', key=key, player=True)
	  r += playScaleNotes(scale='pentMajor', key=key, player=True)
	  r += playScaleNotes(scale='pentMinor', key=key, player=True)
	  r += playScaleNotes(scale='hexBlues', key=key, player=True)
	  r += playScaleNotes(scale='bnotes', key=key, player=True)
	  playNotes(r)
	  
# Example 1, 4, 5 progression
def play145():
  r=[]
  r += playScaleNotes(scale='bnotes', key='C', player=True)
  # playNotes(r)
  r += playScaleNotes(scale='bnotes', key='C', player=True)
  # playNotes(r)  
  r += playScaleNotes(scale ='bnotes', key='F', player=True)
  # playNotes(r)
  r += playScaleNotes(scale='bnotes', key='C', player=True)
  # playNotes(r)
  r += playScaleNotes(scale='bnotes', key='G', player=True)
  # playNotes(r)
  r += playScaleNotes(scale='bnotes', key='F', player=True)
  # playNotes(r)  
  r += playScaleNotes(scale='bnotes', key='C', player=True)
  # playNotes(r)
  r += playScaleNotes(scale='tnotes', key='G', player=True)
  playNotes(r)

#demoScales('A')
#play145()
#demoScales('E')

circleOfFifths('pentMajor')

