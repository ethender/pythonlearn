# 6.00 Problem Set 5
# RSS Feed Filter

import feedparser
import string
import time
from project_util import translate_html
from news_gui import Popup

#-----------------------------------------------------------------------
#
# Problem Set 5

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        summary = translate_html(entry.summary)
        try:
            subject = translate_html(entry.tags[0]['term'])
        except AttributeError:
            subject = ""
        newsStory = NewsStory(guid, title, subject, summary, link)
        ret.append(newsStory)
    return ret

#======================
# Part 1
# Data structure design
#======================

# Problem 1

# TODO: NewsStory

class NewsStory(object):

    def __init__(self,guid,title,subject,summary,link):
        self.guid = guid
        self.title = title
        self.subject = subject
        self.summary = summary
        self.link = link


    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title

    def get_subject(self):
        return self.subject

    def get_summary(self):
        return self.summary

    def get_link(self):
        return self.link


#======================
# Part 2
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

# Whole Word Triggers
# Problems 2-5

# TODO: WordTrigger

class WordTrigger(Trigger):


    """ construtor
        word String"""
    def __init__(self, word):
        self.word = word

    def is_word_in(self,text):
        temp = ""
        for char in text:
            if char in string.punctuation:
                temp += str(' ')
            else:
                temp += str(char)
        wordsList = temp.split(' ')
        if self.word in wordsList:
            return True
        return False
        
##
## Below class  should have to implement the evaluate()  function and must return value
##  
## remove punctuation from string 
##
##  
##


# TODO: TitleTrigger
class TitleTrigger(WordTrigger):
    
    def __init__(self,word):
        self.word = word
        self.trig = WordTrigger(self.word.lower())

    def evaluate(self, story):
        return self.trig.is_word_in(story.get_title().lower())
        
    
# TODO: SubjectTrigger
class SubjectTrigger(WordTrigger):
    def __init__(self,word):
        self.word = word
        self.trig = WordTrigger(self.word.lower())

    def evaluate(self, story):
        return self.trig.is_word_in(story.get_subject().lower())

    
# TODO: SummaryTrigger
class SummaryTrigger(WordTrigger):
    def __init__(self, word):
        self.word = word
        self.trig = WordTrigger(self.word.lower())

    def evaluate(self, story):
        return self.trig.is_word_in(story.get_summary().lower())

# Composite Triggers
# Problems 6-8

# TODO: NotTrigger

class NotTrigger(WordTrigger):

    def __init__(self, notTrigger):
        self.trig = notTrigger
    
    def evaluate(self,story):
        return not self.trig.evaluate(story)

# TODO: AndTrigger

class AndTrigger(WordTrigger):
    def __init__(self, trigger1, trigger2):
        self.trig1 = trigger1
        self.trig2 = trigger2
    def evaluate(self,story):
        return self.trig1.evaluate(story) and self.trig2.evaluate(story)
# TODO: OrTrigger
    
class OrTrigger(WordTrigger):
    def __init__(self, trigger1, trigger2):
        self.trig1 = trigger1
        self.trig2 = trigger2
    def evaluate(self,story):
        return self.trig1.evaluate(story) or self.trig2.evaluate(story)
    

# Phrase Trigger

class PhraseTrigger(WordTrigger):
    def __init__(self,text):
        self.text = text
        print 'word: ',self.text
        self.trig = WordTrigger(self.text.lower())

    def evaluate(self,word):
        return self.text in word.get_title() or self.text in word.get_subject() or self.text in word.get_summary()
        

# Question 9

# TODO: PhraseTrigger


#======================
# Part 3
# Filtering
#======================

def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory-s.
    Returns only those stories for whom
    a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder (we're just returning all the stories, with no filtering) 
    # Feel free to change this line!
    ##return stories
    listOfStories = []
    for trig in triggerList:
        for story in stories:
            if trig.evaluate(story) and story not in listOfStories:
                    listOfStores.append(story)
    return listOfStories
                    
                

#======================
# Part 4
# User-Specified Triggers
#======================

def readTriggerConfig(filename):
    """
    Returns a list of trigger objects
    that correspond to the rules set
    in the file filename
    """
    # Here's some code that we give you
    # to read in the file and eliminate
    # blank lines and comments
    triggerfile = open(filename, "r")
    all = [ line.rstrip() for line in triggerfile.readlines() ]
    lines = []
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)

    # TODO: Problem 11
    # 'lines' has a list of lines you need to parse
    # Build a set of triggers from it and
    # return the appropriate ones
    dicts = {}
    triggerList = []
    for li in lines:
        temp = li.split(' ')
        if str.lower(temp[1]) == 'subject':
            trig = SubjectTrigger(temp[2])
            dicts[temp[0]] = trig
        elif str.lower(temp[1]) == 'title':
            trig = TitleTrigger(temp[2])
            dicts[temp[0]] = trig
        elif str.lower(temp[1]) == 'summary':
            trig = SummaryTrigger(temp[2])
            dicts[temp[0]] = trig
        elif str.lower(temp[1]) == 'pharse':
            trig = PhraseTrigger(temp[2])
            dicts[temp[0]] = trig
        elif str.lower(temp[1]) == 'not':
            trig = NotTrigger(temp[2])
            dicts[temp[0]] = trig
        elif str.lower(temp[1]) == 'and':
            trig = AndTrigger(temp[2],temp[3])
            dicts[temp[0]] = trig
        elif str.lower(temp[1]) == 'or':
            trig = OrTrigger(temp[2],temp[3])
            dicts[temp[0]] = trig
        else:
            if str.lower(temp[0]):
                for i in range(1,len(temp)):
                    triggerList.append(dicts.get(temp[i]))
        return triggerList

    
    
import thread

def main_thread(p):
    # A sample trigger list - you'll replace
    # this with something more configurable in Problem 11
    t1 = SubjectTrigger("Obama")
    t2 = SummaryTrigger("MIT")
    t3 = PhraseTrigger("Supreme Court")
    t4 = OrTrigger(t2, t3)
    triggerlist = [t1, t4]
    
    # TODO: Problem 11
    # After implementing readTriggerConfig, uncomment this line 
    triggerlist = readTriggerConfig("triggers.txt")

    

    guidShown = []
    
    while True:
        print "Polling..."

        # Get stories from Google's Top Stories RSS news feed
        stories = process("http://news.google.com/?output=rss")
        # Get stories from Yahoo's Top Stories RSS news feed
        stories.extend(process("http://rss.news.yahoo.com/rss/topstories"))

        # Only select stories we're interested in
        stories = filter_stories(stories, triggerlist)
    
        # Don't print a story if we have already printed it before
        newstories = []
        for story in stories:
            if story.get_guid() not in guidShown:
                newstories.append(story)
        
        for story in newstories:
            guidShown.append(story.get_guid())
            p.newWindow(story)

        print "Sleeping..."
        time.sleep(SLEEPTIME)

SLEEPTIME = 60 #seconds -- how often we poll
if __name__ == '__main__':
    p = Popup()
    thread.start_new_thread(main_thread, (p,))
    p.start()

