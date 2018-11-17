import basc_py4chan
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("thread", help="Thread to grab images from" )
args = parser.parse_args()

# Get URL to thread
threadURL = args.thread

URL_MATCH = "https://boards.4chan.org"

# Break down the URL
threadURL = threadURL[len(URL_MATCH) : ]

boardChar = threadURL[ : -len(threadURL)+2]
threadNum = threadURL[9 : ]

print "DEBUG: "
print "threadURL",threadURL
print "boardChar",boardChar
print "threadNum",threadNum
print "\n\n"

w = basc_py4chan.Board(boardChar)

thread = w.get_thread(threadNum)

print thread

if thread.sticky:
    print "Thread is stickied"

for post in thread.posts:
    print "Subject: ", post.subject
    print post.text_comment
