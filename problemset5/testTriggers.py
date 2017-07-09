from ps5 import *

koala     = NewsStory('', 'Koala bears are soft and cuddly', '', '', '')
pillow    = NewsStory('', 'I prefer pillows that are soft.', '', '', '')
soda      = NewsStory('', 'Soft drinks are great', '', '', '')
pink      = NewsStory('', "Soft`s the new pink!", '', '', '')
football  = NewsStory('', '"Soft!" he exclaimed as he threw the football', '', '', '')
microsoft = NewsStory('', 'Microsoft announced today that pillows are bad', '', '', '')
nothing   = NewsStory('', 'Reuters reports something really boring', '', '' ,'')
caps      = NewsStory('', 'soft things are soft', '', '', '')


s1 = TitleTrigger('SOFT')
print 'koala: '+str(s1.evaluate(koala))
print 'pillow: '+str(s1.evaluate(pillow))
print 'pink: '+str(s1.evaluate(pink))
print 'football: '+str(s1.evaluate(football))
print 'microsoft: '+str(s1.evaluate(microsoft))
print 'nothing: '+str(s1.evaluate(nothing))
print 'caps: '+str(s1.evaluate(caps))
