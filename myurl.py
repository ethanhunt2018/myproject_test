from urllib.request import urlopen
for line in urlopen('http://www.baidu.com'):
    line = line.decode('utf-8')  # Decoding the binary data to text.
    if 'EST' in line or 'EDT' in line:  # look for Eastern Time
        print("====if=====")
        print(line)
    else:
        #print("====else====")
        print(line)
