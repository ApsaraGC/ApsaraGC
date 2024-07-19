print('hello')

file=open('python.txt','r')
line=file.readline()
print(line)
file.close()

with open('python.txt', 'w') as f:
    data='some data to be written to file'
    f.write(data)