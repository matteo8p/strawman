import spacy
import wordlib as wordlib 
nlp = spacy.load("en_core_web_sm")
frequency = 4                          #Every X NOUN, PROPN, VERB, or ADJ will be replaced by a new word. The lower the value, the more frequent our adlibs will be. Max value is 1 

#processMessage(message)
# Input: message in text format
# Output: 2d of array featuring its original text and its part of speech. 
def processMessage(message): 
    doc = nlp(message) 
    analysis = []                           

    for token in doc: 
        word = token.text 
        pos = token.pos_
        if word[0] == '@':
            pos = 'MENTION'
            word = word[1:]             #Remove @ tag to prevent program from tagging people. 
        analysis.append([word, pos])
    return analysis 

#translateMessage(analysis)
# Input: 2d Analysis array from processMessage()
# Output: The translated message 
def translateMessage(analysis): 
    counter = 0                 #Counter to control the frequency of our madlib insertion 
    translation = ''            #Final message to be returned 
    
    for pair in analysis:       #A pair is like ['Word', 'Part of speech']  
        word = ''
        if pair[1] == 'NOUN' or pair[1] == 'PROPN' or pair[1] == 'VERB' or pair[1] == 'ADJ': 
            if counter % frequency == 0:                #Only replace every {frequency} words 
                word += ' ' + wordlib.getRandomWord(pair[1])
            else: 
                word += ' ' + pair[0] 
            counter += 1                                
        elif pair[1] == 'PUNCT':                        #For punctuations, do not add space to beginning 
            word = pair[0]      
        else:                                           #If it's not a noun, proper noun, or verb, just replace it with the word itself 
            word += ' ' + pair[0]  
             
        translation += word         

    return translation

def doNLP(message): 
    processed = processMessage(message)
    translated = translateMessage(processed)
    return translated


