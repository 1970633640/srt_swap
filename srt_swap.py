import srt, io

filename = 'test.srt'

f = io.open(filename, 'r', encoding='utf-8-sig')
subtitles = list(srt.parse("".join(f.readlines())))
f.close()

for i in range(0, len(subtitles)):
    subtitles[i].content = subtitles[i].content.strip()
    if subtitles[i].content.count('\n') == 2:
        subtitles[i].content = subtitles[i].content.replace('\n', ' ', 1)
for i in range(0, len(subtitles)):
    if subtitles[i].content.count('\n') == 1:
        t = subtitles[i].content.split('\n')
        subtitles[i].content = t[1] + '\n' + t[0]
    if subtitles[i].content.count('\n') == 3:
        t = subtitles[i].content.split('\n')
        subtitles[i].content = t[1] + '    ' + t[3] + '\n' + t[0] + '    ' + t[2]

f2 = io.open('out.srt', 'w', encoding='utf-8-sig')
f2.write(srt.compose(subtitles))
f2.close()
