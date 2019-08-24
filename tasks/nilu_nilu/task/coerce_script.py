with open('AiO-script.txt', 'r') as f:
    lines = f.read().split('\n')

prev_line = ''

for idx, line in enumerate(lines):
    if len(prev_line) > 1 and line.startswith(prev_line):
        l = line[len(prev_line):].strip()
        if len(l) > 1:
            print(l)
    prev_line = line
