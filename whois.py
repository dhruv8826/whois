import urllib2

s = "" i = 0 def find_str(s, char): index = 0

if char in s:
    c = char[0]
    for ch in s:
        if ch == c:
            if s[index:index+len(char)] == char:
                return index

        index += 1

return -1
a = raw_input("enter the site url") 
a_file = urllib2.urlopen('https://who.is/whois/' + a) 
for line in a_file:
  if 'rawWhois' in line:
    i = find_str(line, 'src')
    print i
    s="https://who.is"+line[i+5: i+76] 
print s
