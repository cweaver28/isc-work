s = "I love to write python"
for i in s:
   print i

print s[4]
print s[-1]
print len(s)

print s[0]
print s[0][0]
print s[0][0][0]

split_s =s.split()

print s.split()
for word in split_s:
   if word.find("i") > -1:
      print "I found 'i' in: '{0}'".format(word)

if "i" in word:
   print "I found 'i' in '{0}'".format(word)


