import pygame, random, sys, copy
from pygame.locals import *

pygame.init()

WINDOWSIZE = (630, 700)
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

windowSurf = pygame.display.set_mode(WINDOWSIZE)
fpsClock = pygame.time.Clock()
pygame.display.set_caption("Pseudoku")

background1Img = pygame.image.load("background1.bmp")
background2Img = pygame.image.load("background2.bmp")
numEnterSoundObj = pygame.mixer.Sound("sounds/number_enter.wav")
winSoundObj = pygame.mixer.Sound("sounds/win.wav")

########################################################################
# TITLE SCREEN
########################################################################

def titleScreen():
	titleFontObj = pygame.font.Font('freesansbold.ttf', 72)
	title2FontObj = pygame.font.Font('freesansbold.ttf', 30)
	titleTextObj = titleFontObj.render("Pseudoku", True, WHITE)
	titleTextRect = titleTextObj.get_rect(center=(int(WINDOWSIZE[0] * .5), int(WINDOWSIZE[1] * .25)))
	title2TextObj = title2FontObj.render("Click anywhere to begin!", True, WHITE)
	title2TextRect = title2TextObj.get_rect(center=(int(WINDOWSIZE[0] * .5), int(WINDOWSIZE[1] * .65)))
	bg1 = True
	bgSwitchCounter = 0
	
	while True:
		bgSwitchCounter += 1
		if bgSwitchCounter > FPS * .5:
			bg1 = not bg1
			bgSwitchCounter = 0
		if bg1:
			windowSurf.blit(background1Img, (0, 0))
		else:
			windowSurf.blit(background2Img, (0, 0))
		windowSurf.blit(titleTextObj, titleTextRect)
		windowSurf.blit(title2TextObj, title2TextRect)
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				return
		
		fpsClock.tick(FPS)
		pygame.display.update()

########################################################################
# SELECT DIFFICULTY
########################################################################

def selectDifficulty():
	fontObj = pygame.font.Font('freesansbold.ttf', 30)
	difficultyTextObj = fontObj.render("Select difficulty: ", True, WHITE)
	difficultyTextRect = difficultyTextObj.get_rect(center=(int(WINDOWSIZE[0] * .5), int(WINDOWSIZE[1] * .2)))
	veryEasyTextObj = fontObj.render("Very Easy", True, WHITE)
	veryEasyTextRect = veryEasyTextObj.get_rect(center=(int(WINDOWSIZE[0] * .5), int(WINDOWSIZE[1] * .4)))
	easyTextObj = fontObj.render("Easy", True, WHITE)
	easyTextRect = easyTextObj.get_rect(center=(int(WINDOWSIZE[0] * .5), int(WINDOWSIZE[1] * .5)))
	mediumTextObj = fontObj.render("Medium", True, WHITE)
	mediumTextRect = mediumTextObj.get_rect(center=(int(WINDOWSIZE[0] * .5), int(WINDOWSIZE[1] * .6)))
	hardTextObj = fontObj.render("Hard", True, WHITE)
	hardTextRect = hardTextObj.get_rect(center=(int(WINDOWSIZE[0] * .5), int(WINDOWSIZE[1] * .7)))
	veryHardTextObj = fontObj.render("Very Hard", True, WHITE)
	veryHardTextRect = veryHardTextObj.get_rect(center=(int(WINDOWSIZE[0] * .5), int(WINDOWSIZE[1] * .8)))
	extremeTextObj = fontObj.render("Extreme", True, WHITE)
	extremeTextRect = extremeTextObj.get_rect(center=(int(WINDOWSIZE[0] * .5), int(WINDOWSIZE[1] * .9)))
	bg1 = True
	bgSwitchCounter = 0
	
	while True:
		bgSwitchCounter += 1
		if bgSwitchCounter > FPS * .5:
			bg1 = not bg1
			bgSwitchCounter = 0
		if bg1:
			windowSurf.blit(background1Img, (0, 0))
		else:
			windowSurf.blit(background2Img, (0, 0))
		windowSurf.blit(difficultyTextObj, difficultyTextRect)
		windowSurf.blit(veryEasyTextObj, veryEasyTextRect)
		windowSurf.blit(easyTextObj, easyTextRect)
		windowSurf.blit(mediumTextObj, mediumTextRect)
		windowSurf.blit(hardTextObj, hardTextRect)
		windowSurf.blit(veryHardTextObj, veryHardTextRect)
		windowSurf.blit(extremeTextObj, extremeTextRect)
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				if veryEasyTextRect.collidepoint(event.pos):
					return "veryEasy"
				elif easyTextRect.collidepoint(event.pos):
					return "easy"
				elif mediumTextRect.collidepoint(event.pos):
					return "medium"
				elif hardTextRect.collidepoint(event.pos):
					return "hard"
				elif veryHardTextRect.collidepoint(event.pos):
					return "veryHard"
				elif extremeTextRect.collidepoint(event.pos):
					return "extreme"
		
		mousePos = pygame.mouse.get_pos()
		if veryEasyTextRect.collidepoint(mousePos):
			pygame.draw.rect(windowSurf, RED, veryEasyTextRect, 3)
		elif easyTextRect.collidepoint(mousePos):
			pygame.draw.rect(windowSurf, RED, easyTextRect, 3)
		elif mediumTextRect.collidepoint(mousePos):
			pygame.draw.rect(windowSurf, RED, mediumTextRect, 3)
		elif hardTextRect.collidepoint(mousePos):
			pygame.draw.rect(windowSurf, RED, hardTextRect, 3)
		elif veryHardTextRect.collidepoint(mousePos):
			pygame.draw.rect(windowSurf, RED, veryHardTextRect, 3)
		elif extremeTextRect.collidepoint(mousePos):
			pygame.draw.rect(windowSurf, RED, extremeTextRect, 3)
		
		fpsClock.tick(FPS)
		pygame.display.update()

########################################################################
# RUN MAIN GAME
########################################################################

class Clock:
	fontObj = pygame.font.Font('freesansbold.ttf', 50)
	
	def __init__(self):
		self.minutes = 0
		self.seconds = 0
		self.frameCounter = 0
		
	def update(self):
		self.frameCounter += 1
		if self.frameCounter > 60:
			self.seconds += 1
			if self.seconds == 60:
				self.seconds = 0
				self.minutes += 1
			self.frameCounter = 0
		textObj = Clock.fontObj.render('{:02}'.format(self.minutes)+":"+'{:02}'.format(self.seconds), True, BLACK)
		textRect = textObj.get_rect(center=(315, 670))
		windowSurf.blit(textObj, textRect)

def drawLines():
	# draw thin lines
	for x in range(70, 700, 70):
		pygame.draw.line(windowSurf, BLACK, (x, 0), (x, 630))
	for y in range(70, 700, 70):
		pygame.draw.line(windowSurf, BLACK, (0, y), (630, y))
	
	# draw thick lines
	for x in range(210, 630, 210):
		pygame.draw.line(windowSurf, BLACK, (x, 0), (x, 630), 4)
	for y in range(210, 630, 210):
		pygame.draw.line(windowSurf, BLACK, (0, y), (630, y), 4)
		
def getBigBoxes(boxes):
	bigBoxes = {'topleft': [[boxes[x][x2] for x2 in range(3)] for x in range(3)], \
				'topmid': [[boxes[x][x2] for x2 in range(3, 6)] for x in range(3)], \
				'topright': [[boxes[x][x2] for x2 in range(6, 9)] for x in range(3)], \
				'midleft': [[boxes[x][x2] for x2 in range(3)] for x in range(3, 6)], \
				'midmid': [[boxes[x][x2] for x2 in range(3, 6)] for x in range(3, 6)], \
				'midright': [[boxes[x][x2] for x2 in range(6, 9)] for x in range(3, 6)], \
				'bottomleft': [[boxes[x][x2] for x2 in range(3)] for x in range(6, 9)], \
				'bottommid': [[boxes[x][x2] for x2 in range(3, 6)] for x in range(6, 9)], \
				'bottomright': [[boxes[x][x2] for x2 in range(6, 9)] for x in range(6, 9)]}
	return bigBoxes
	
def checkNumPlace(newNum, place, boxes):
	# check big boxes to see if newNum already is in there
	if boxes[place[0]][place[1]] != 0:
		return False
	bigBoxes = getBigBoxes(boxes)
	bigBox = ''
	if place[0] >= 0 and place[0] <= 2:
		bigBox += 'top'
	elif place[0] >= 3 and place[0] <= 5:
		bigBox += 'mid'
	elif place[0] >= 6 and place[0] <= 8:
		bigBox += 'bottom'
	if place[1] >= 0 and place[1] <= 2:
		bigBox += 'left'
	elif place[1] >= 3 and place[1] <= 5:
		bigBox += 'mid'
	elif place[1] >= 6 and place[1] <= 8:
		bigBox += 'right'
	for row in bigBoxes[bigBox]:
		for num in row:
			if newNum == num:
				return False
	# check column
	for row in boxes:
		if row[place[1]] == newNum:
			return False
			
	return True
		
def getNumPlaces(num, row, boxes):
	places = []
	for column in range(9):
		if checkNumPlace(num, [row, column], boxes):
			places.append(column)
	return places
		
def populateBoxes(boxes, difficulty):
	# randomly place 1-9 in first row
	nums = [x for x in range(1, 10)]
	random.shuffle(nums)
	for i, column in enumerate(boxes[0]):
		boxes[0][i] = nums.pop()
	# place rest of rows
	for row in range(1, 9):
		numPlaces = {}
		for num in range(1, 10):
			numPlaces[num] = getNumPlaces(num, row, boxes)
		while len(numPlaces) > 0:
			toDelete = None
			for num in numPlaces:
				numPlaces[num] = getNumPlaces(num, row, boxes)
			lowestNum = 9
			for num in numPlaces:
				if len(numPlaces[num]) < lowestNum:
					lowestNum = len(numPlaces[num])
			for num in numPlaces:
				if len(numPlaces[num]) == lowestNum:
					try:
						boxes[row][random.choice(numPlaces[num])] = num
					# try again if board locks up
					except:
						runGame(difficulty)
					toDelete = num
					break
			del numPlaces[toDelete]
		
def drawBoxes(boxesDict):
	numFontObj = pygame.font.Font('freesansbold.ttf', 30)
	for box in boxesDict:
		if boxesDict[box][0] != 0:
			if boxesDict[box][2]:
				numText = numFontObj.render(str(boxesDict[box][0]), True, RED)
			else:
				numText = numFontObj.render(str(boxesDict[box][0]), True, BLACK)
			windowSurf.blit(numText, numText.get_rect(center=boxesDict[box][1].center))
			
def updateBoard(boxes2, boxesDict):
	horizPixelCounter, vertPixelCounter = 0, 0
	for i, row in enumerate(boxes2):
		for i2, column in enumerate(row):
			boxes2[i][i2] = boxesDict['box'+str(horizPixelCounter)+'_'+str(vertPixelCounter)][0]
			horizPixelCounter += 70
		horizPixelCounter = 0
		vertPixelCounter += 70
		
def checkForWin(boxes, boxes2):
	for row in range(9):
		for column in range(9):
			if boxes[row][column] != boxes2[row][column]:
				return False
	return True

def runGame(difficulty):
	if difficulty == "veryEasy":
		numMissing = 1
	elif difficulty == "easy":
		numMissing = 20
	elif difficulty == "medium":
		numMissing = 30
	elif difficulty == "hard":
		numMissing = 35
	elif difficulty == "veryHard":
		numMissing = 40
	elif difficulty == "extreme":
		numMissing = 55
	clock = Clock()
	boxes = [[0,0,0,0,0,0,0,0,0], \
			[0,0,0,0,0,0,0,0,0], \
			[0,0,0,0,0,0,0,0,0], \
			[0,0,0,0,0,0,0,0,0], \
			[0,0,0,0,0,0,0,0,0], \
			[0,0,0,0,0,0,0,0,0], \
			[0,0,0,0,0,0,0,0,0], \
			[0,0,0,0,0,0,0,0,0], \
			[0,0,0,0,0,0,0,0,0]]
			
	populateBoxes(boxes, difficulty)
	# boxes now equals the solution; boxes2 is the current board
	boxes2 = copy.deepcopy(boxes)
	horizPixelCounter, vertPixelCounter = 0, 0
	boxesDict = {}
	for row in boxes2:
		for column in row:
			boxesDict['box'+str(horizPixelCounter)+'_'+str(vertPixelCounter)] = [column, Rect((horizPixelCounter, vertPixelCounter), (70, 70)), False]
			horizPixelCounter += 70
		horizPixelCounter = 0
		vertPixelCounter += 70
	# remove numbers to create puzzle
	for _ in range(numMissing):
		while True:
			randBox = boxesDict[random.choice(list(boxesDict.keys()))]
			if randBox[0] != 0:
				randBox[0] = 0
				randBox[2] = True
				break
	currentBox = None
	
	while True:
		windowSurf.fill(WHITE)
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
				if currentBox and event.key in (K_0, K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9):
					numEnterSoundObj.play()
					# minus 48 because of event code corresponding to each actual number
					currentBox[0] = event.key - 48
			if event.type == MOUSEBUTTONDOWN:
				for box in boxesDict:
					if boxesDict[box][2] and boxesDict[box][1].collidepoint(event.pos):
						currentBox = boxesDict[box]
		
		updateBoard(boxes2, boxesDict)
		
		if checkForWin(boxes, boxes2):
			winFontObj = pygame.font.Font('freesansbold.ttf', 72)
			winTextObj = winFontObj.render("You win!", True, RED)
			winTextRect = winTextObj.get_rect(center=(int(WINDOWSIZE[0] / 2), int(WINDOWSIZE[1] / 2)))
			windowSurf.blit(winTextObj, winTextRect)
			fpsCounter = 0
			winSoundObj.play()
			while True:
				fpsCounter += 1
				if fpsCounter > FPS * 3:
					break
				
				fpsClock.tick(FPS)
				pygame.display.update()
			pygame.quit()
			sys.exit()
		
		drawLines()
		drawBoxes(boxesDict)
		clock.update()
		
		if currentBox:
			pygame.draw.rect(windowSurf, RED, currentBox[1], 3)
	
		fpsClock.tick(FPS)
		pygame.display.update()

def main():
	titleScreen()
	difficulty = selectDifficulty()
	runGame(difficulty)
	
	return 0

if __name__ == '__main__':
	main()
