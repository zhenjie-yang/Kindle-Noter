import shutil # 文件复制

# kindle 盘符，我电脑上是E盘
driver = "E:"

# 输入文件
# 先复制到当前文件夹下的tmp文件夹，也可以直接操作原文件
dir = "//documents//"
filename = "My Clippings.txt"
targetdir = ".//tmp//"

# 输出到文件当前目录下的note.txt
outfile = "note.txt"

# 复制My clippings.txt到当前文件夹下
shutil.copyfile(driver+dir+filename, targetdir+filename)

# 打开文件
f = open(targetdir+filename, 'r', encoding='UTF-8')

# 读取文件
data = []
for line in f:
    data.append(line)

# 定义笔记分隔符
div = "==========" 

# 数据处理
books = []
infos = []
notes = [[]]
i = 0
while i < len(data):
    book = data[i]  # 读取一条笔记第一行
    i = i + 1
    info = data[i]  # 读取笔记位置、时间信息
    i = i + 2   # 跳过空行
    note = []
    while i < len(data):
        s = data[i]
        if div in s:
            i = i + 1
            break
        else:
            i = i + 1
            note.append(s)

    if len(books) == 0 or book != books[len(books)-1]:
        books.append(book)
        notes.append([])

    notes[len(books)-1].append(note)

f.close()

# 输出到文件
with open(outfile, 'w', encoding='UTF-8') as f:
    for i in range(len(books)):
        f.write(div + books[i].replace('\n','') + div)
        f.write('\n\n')
        for j in range(len(notes[i])):
            f.write(str(j+1) + '.')
            for k in range(len(notes[i][j])):
                f.write(notes[i][j][k])
        f.write('\n')

# 清空原文件，慎重处理
# open(targetdir+filename, 'w').close()