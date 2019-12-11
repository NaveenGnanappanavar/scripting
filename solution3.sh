#!/bin/bash
echo "aaAA bbBB" > text2

#Output the number of readable characters in the input text
cat text2 |tr -d [:blank:] | wc -c

#Output the number of words in the input text
wc -w text2

#No of times the most commonly occurring alphabet occurs
sed 's/\(.\)/\1\n/g' text2 |  uniq -ic | sort -nr  |  head -n 1

#Output the number of characters in the input text that are alphabets
sed 's/[^a-zA-Z]//g' text2 | tr -d [:blank:] | wc -c       