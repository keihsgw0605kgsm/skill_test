def split_colon(row):
    i = row.split(':')[0]
    s = row.split(':')[1]
    return i, s

def main():
    pair = []
    row_no = 0

    fileobj = open("input.txt", "r", encoding="utf_8")
    while True:
      line = fileobj.readline()
      if line:
        row_no += 1
        line = line.replace('\n', '')
        pair.append(line)
      else:
        break
    
    i = []
    s = []
    m = int(pair[len(pair)-1])
    for j in range(len(pair)-1):
        i_, s_ = split_colon(pair[j])
        i.append(int(i_))
        s.append(s_)
    
    zip_is = list(zip(i, s))
    zip_is.sort()
    i, s = zip(*zip_is)
    
    output_s = ""
    for j in range(len(pair)-1):
        if(m % i[j] == 0):
            output_s += s[j]
    
    if(output_s == ""):
        print(m)
    else:
        print(output_s)

if __name__ == "__main__":
    main()
