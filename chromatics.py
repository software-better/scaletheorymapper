
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

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

scales = {
	'major': [0, 2, 4, 5, 7, 9, 11, 12],
	'minor': [0, 2, 3, 5, 7, 8, 10, 12],
	'hexBlues': [0, 3, 5, 6, 7, 10, 12],
	'pentMajor': [0, 2, 4, 7, 9, 12],
	'pentMinor': [0, 3, 5, 7, 10, 12],
}

def findNotes(key):
	L = []
	if key in flatChromaticScales.keys():
		L = flatChromaticScales[key]
	if key  in sharpChromaticScales.keys():
		L = sharpChromaticScales[key]
	return L


def showScaleNotes(scale='major', key='C'):
	result = []
	keyScaleNotes = findNotes(key)
	for i in scales[scale]:
		result.append(keyScaleNotes[i])
	logging.debug(key + scale + " : " + str(result))
	return result
