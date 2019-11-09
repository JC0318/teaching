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

		maxX = len(fivePointQipan.qipan)
		maxY = len(fivePointQipan.qipan[0])
	if fivePointQipan.qipan[x+1][y+1] == mark or fivePointQipan.qipan[x-1][y-1] == mark:


		previousX = x-1
		previousY = y-1
		targetStr = ''
		while (previousY >=0) | (previousX>=0):
			targetStr = targetStr + fivePointQipan.qipan[previousX][previousY]
			previousX -=1
			previousY -=1
		targetStr = targetStr[::-1] + fivePointQipan.qipan[x][y]
		nextx = x+1
		nexty = y+1
		maxX = len(fivePointQipan.qipan)
		maxY = len(fivePointQipan.qipan[0])

		while (nextx < maxX )|(nexty<maxY):
			targetStr = targetStr + fivePointQipan.qipan[nextx][nexty]
			nextx += 1
			nexty += 1
		if testing in targetStr:
			retuen True

	if fivePointQipan.qipan[x+1][y-1] == mark | fivePointQipan.qipan[x-1][y+1]==mark:
		previousX = x+1
		previousY = y-1
		targetStr = ''
		while (previousX < maxX)|(previousY >= 0):
			
			
			





















