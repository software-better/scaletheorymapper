import chromatics as c

for i in ['C', 'D', 'E', 'F', 'G', 'A', 'B']:
	c.showScaleNotes(scale='major', key=i)
	c.showScaleNotes(scale='minor', key=i)
	c.showScaleNotes(scale='pentMajor', key=i)
	c.showScaleNotes(scale='pentMinor', key=i)
	c.showScaleNotes(scale='hexBlues', key=i)
