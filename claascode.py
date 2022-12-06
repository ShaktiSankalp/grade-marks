fin = open('InputData2.txt','r')
charCount = wordCount = lineCount = 0
for line in fin:
    lineCount += 1
    wordCount += len(line.split())
    charCount += len(line)
print('Line count = ',lineCount)
print('Word count = ', charCount)
print('Char count = ', charCount)


f = open('Input.txt','w')
f.write('Hello\nwelcome\nBye')
f.close()
fin = open('Input.txt','r')
charCount = wordCount = lineCount = 0
for line in fin:
    lineCount += 1
    wordCount += len(line.split())
    charCount += len(line)
print('Line count = ',lineCount)
print('Word count = ', charCount)
print('Char count = ', charCount)

fw = open('NewFile.txt','w')
fw.write('Hello')
fw.write('welcome')
fw.close()
fr1 = open('NewFile.txt','r+')
print(fr1.read(4))
print(fr1.tell())
print(fr1.write('This is the new text'))
print(fr1.seek(5))
print(fr1.read(1))
print(fr1.read())
fr1.close()

