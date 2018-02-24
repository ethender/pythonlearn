from ps5 import *

##koala     = NewsStory('', 'Koala bears are soft and cuddly', '', '', '')
##pillow    = NewsStory('', 'I prefer pillows that are soft.', '', '', '')
##soda      = NewsStory('', 'Soft drinks are great', '', '', '')
##pink      = NewsStory('', "Soft's the new pink!", '', '', '')
##football  = NewsStory('', '"Soft!" he exclaimed as he threw the football', '', '', '')
##microsoft = NewsStory('', 'Microsoft announced today that pillows are bad', '', '', '')
##nothing   = NewsStory('', 'Reuters reports something really boring', '', '' ,'')
##caps      = NewsStory('', 'soft things are soft', '', '', '')
##
##
##s1 = TitleTrigger('SOFT')
##print s1.evaluate(koala)
##print s1.evaluate(pillow)
##print s1.evaluate(soda)
##print s1.evaluate(pink)
##print s1.evaluate(football)
##print s1.evaluate(microsoft)
##print s1.evaluate(nothing)
##print s1.evaluate(caps)


##class TrueTrigger:
##    def evaluate(self, story): return True
##
##class FalseTrigger:
##    def evaluate(self, story): return False
##
##tt = TrueTrigger()
##ft = FalseTrigger()
##
##b = NewsStory("guid", "title", "subj", "summary", "link")
##
##
##n = NotTrigger(tt)
##print 'False',n.evaluate(b)
##
##y = NotTrigger(ft)
##print 'True',y.evaluate(b)






pt = PhraseTrigger("New York City")
a = NewsStory('', "asfdNew York Cityasfdasdfasdf", '', '', '')
b = NewsStory('', '', "asdfasfdNew York Cityasfdasdfasdf", '', '')
c = NewsStory('', '', '', "asdfasfdNew York Cityasfdasdfasdf", '')
noa = NewsStory('', "something something new york city", '', '', '')
nob = NewsStory('', '', "something something new york city", '', '')
noc = NewsStory('', '', '', "something something new york city", '')


t = [a,b,c]
f = [noa, nob, noc]

print 'True Value' 
for tItem in t:
    print pt.evaluate(tItem)

print 'False Value'
for fItem in f:
    print pt.evaluate(fItem)

