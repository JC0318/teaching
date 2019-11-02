'''
[
[None, None, None, None, None, None, None ],
[None, None, None, None, None, None, None ],
[None, None, None, None, None, None, None ],
[None, None, None, None, None, None, None ],
[None, None, None, None, None, None, None ],
[None, None, None, None, None, None, None ],
[None, None, None, None, None, None, None ]
]
'''

from qipan import fivePoint

fivePointQipan = fivePoint()

for i in range (len(fivePointQipan.qipan)):
	for k in range(len(fivePointQipan.qipan[i])):
		fivePointQipan.qipan[i][k] ="N" 

def placePieceA(x,y):
	if fivePointQipan.qipan[x][y]== 'N':
		fivePointQipan.qipan[x][y] = 'A'
		return True
	else:
		return False
def placePieceB(x,y):
	if fivePointQipan.qipan[x][y] == 'N':
		fivePointQipan.qipan[x][y] = 'B'
		return	True
	else:
		return False

def placePiece(x,y, mark):
	if fivePointQipan.qipan[x][y] == 'N':
		fivePointQipan.qipan[x][y] = mark
		return	True
	else:
		return False

def ifWin(x,y,mark):
	testing = ''.join([mark]*5)

	# first part
	sentance = ''.join(fivePointQipan.qipan[x])
	if testing in sentance:
		return True


	#second part
	sentance = []
	for i in range(len(fivePointQipan.qipan[x])):
		sentance.append(fivePointQipan.qipan[i][y])
	sentance = ''.join(sentance)
	if testing in sentance:
		return True

	if fivePointQipan.qipan[x+1][y+1] == mark or fivePointQipan.qipan[x-1][y-1] == mark:

























