# コロンでiとsを分割する関数
def split_colon(row):
    i = row.split(':')[0]
    s = row.split(':')[1]
    return i, s

def main():
    pair = []
    row_no = 0

    # input.txtの読み込み(i:sとmをリストpairに格納)
    fileobj = open("input.txt", "r", encoding="utf_8")
    while True:
      line = fileobj.readline()
      if line:
        row_no += 1
        line = line.replace('\n', '')
        pair.append(line)
      else:
        break
    
    # iとsを分割し，それぞれ別のリストに格納
    i = []
    s = []
    m = int(pair[len(pair)-1])
    for j in range(len(pair)-1):
        i_, s_ = split_colon(pair[j])
        i.append(int(i_))
        s.append(s_)
    
    # リストi,sをiの数値に従って昇順にソート
    zip_is = list(zip(i, s))
    zip_is.sort()
    i, s = zip(*zip_is)
    
    # mを割り切れるか判定したのち，output_sにsを結合
    output_s = ""
    for j in range(len(pair)-1):
        if(m % i[j] == 0):
            output_s += s[j]
    
    # output_sが空白(割り切れるiが無かった)の場合mを出力
    if(output_s == ""):
        print(m)
    # output_sを出力
    else:
        print(output_s)

if __name__ == "__main__":
    main()
