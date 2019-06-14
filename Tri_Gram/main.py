"""
# Author:   Hop N Pham
# Version:     6/10/2019
# Assigment:   Trigram	model	of	English
"""
import timeit
import random
STORY_LEN = 1000 # len of the story to generates.

class Tri_Gram:
    
    # Initializes
    def __init__(self, count, theTri_Sequence):
        self.structor = []
        self.appeared = 1
        self.count = count
        self.element = theTri_Sequence[0]
        self.__insert(len(theTri_Sequence) > 1, theTri_Sequence)
		
    def chooseWord(self):
        story = []
        if (len(self.structor) < 1): return ''
        choiceWord = random.choice(self.structor)
        story.append(choiceWord.element)
        story += choiceWord.chooseWord()
        return story
		
    def __insert(self,len,theTri_Sequence):
        if (len) : self.structor.append(Tri_Gram(self.count + 1, theTri_Sequence[1:]))	
		
    def gramUpdate(self, tri_Sequence):
        flag = True
        self.appeared += 1
        for word in self.structor:
            if  word.element == tri_Sequence[0]:                
                word.gramUpdate(tri_Sequence[1:])
                flag = False
                break
        if flag and len(tri_Sequence) > 0:
            self.structor.append(Tri_Gram(self.count + 1, tri_Sequence))
	
			
def loadWords(stories):
    words = []
    for story in stories:
        print story, ' is loading...'
        with open(story, 'r') as lines:
            for line in lines:
                words.extend(line.lower().split())
    print 'Stories loaded.'
    return words   
	
def generateStory(theStructor):
    story = []
    story.append(random.choice(theStructor).element) # Randomly select first word.
    # Generate the story base on the requirement length.
    while len(story) < STORY_LEN:
        for word in theStructor:
            if word.element == story[-1]:
                story += word.chooseWord()
                break			
    for i in range (STORY_LEN, len(story)):
        story[i] = '';
    with open('output.txt','w') as f:
        f.write( ' '.join( story ) )
    print 'Finished, please check the output file output.txt'
	
def updateModel(elem, target):	
    if (elem.element == target[0]):
        elem.gramUpdate(target[1:])
        return True
    return False
	
if __name__ == '__main__':
    start = timeit.default_timer()
    stories = ['alice-27.txt','doyle-27.txt','doyle-case-27.txt','london-call-27.txt','melville-billy-27.txt','twain-adventures-27.txt']
    tri_Sequence = []
    words = loadWords(stories)
    structor = []     
    print 'Generating tri-gram model for stories...'
    for word in words:
        tri_Sequence.append(word)
        if len(tri_Sequence) == 3: #find new sequence
            if not any(updateModel(elem,tri_Sequence) for elem in structor): structor.append(Tri_Gram(0, tri_Sequence))
            tri_Sequence.remove(tri_Sequence[0])
        #print len(structor)
    print 'The program is generating story...'   
    generateStory(structor)
    stop = timeit.default_timer()
    print('Time: ', stop - start) 