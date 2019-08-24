lines = [None] * 2

with open('ids', 'r') as f:
    lines[0] = [l for l in f.read().split('\n') if l.strip() != '']

with open('AiO-script-with-flag.txt', 'r') as f:
    lines[1] = [l for l in f.read().split('\n') if l.strip() != '']

assert len(lines[0]) == len(lines[1])

d = dict(zip(*lines))
print(d)
