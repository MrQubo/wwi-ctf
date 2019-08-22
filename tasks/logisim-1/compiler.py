#!/usr/bin/python3

INST = {
        'add': 0,
        'sub': 1,
        'mul': 2,
        'rem': 3, #shift left
        'xor': 4,
        'wnn': 5, #write if not negative
        'wne': 6, #write if negativei
        'mov': 7, #uses only A
        'shl': 8,
        'shr': 9,
        'rtl': 10,
        # 'unimp': 11,
        # 'unimp': 12,
        # 'unimp': 13,
        # 'unimp': 14,
        # 'unimp': 15
}

two_param_inst = ['mov']

REG = {
        'r0': 0,
        'r1': 1,
        'r2': 2,
        'r3': 3,
        'r4': 4,
        'r5': 5,
        'r6': 6,
        'r7': 7,
        'adr': 8,    # "adr" register device
        'mem': 9,    # RAM[adr]
        'kbd': 10,   # keyboard, read - 0-6 bit ASCII 7bit "has data", write - clear
        'tty': 11,   # "stdout", write - 0-6 bit ASCII
        'd4': 12,    # not connected
        'd5': 13,    # not connected
        'ip': 14,    # instruction pointer
        'data': 15,  # instruction data
}


class Mark(str):
    pass


def is_number(x):
    return x.isdecimal() or x.startswith('0x')


def to_number(x):
    if x.isdecimal():
        num = int(x)
    elif x.startswith('0x'):
        x_num = x[2:]
        if len(x_num) not in [2,4]:
            raise AssemblyException("Invalid hex literal %s" % x)
        try:
            num = int(x_num, 16)
        except ValueError:
            raise AssemblyException("Invalid hex literal %s" % x)
    elif x.startswith("$"):
        return Mark(x[1:])
    else:
        raise AssemblyException("Not a number %s" % x)
    if num < 0 or num > 2**16 - 1:
        raise AssemblyException("Number not in range %s (from %s)" % (num, x))
    return num


class AssemblyException(Exception):
    pass


class Instruction:
    def __init__(self, line):
        line = line.split(" ")
        if len(line) == 3:
            line.append('r0')
            is_two_param_inst = True
        else:
            is_two_param_inst = False

        if len(line) != 4:
            raise AssemblyException("Invalid line element count: %s" % line)

        self.inst = line[0]
        self.arg1 = line[1]
        self.arg2 = line[2]
        self.res = line[3]

        if inst not in INST:
            raise AssemblyException("Invalid instruction %s" % inst)
        if is_two_param_inst and inst not in two_param_inst:
            raise AssemblyException("Two arguments provided, but %s is not a two argument instruction" % inst)

        self.data = None
        if is_number(self.arg1):
            self.data = to_number(self.arg1)
            self.arg1 = 'data'
        elif self.arg1 not in REG:
            raise AssemblyException("Invalid register %s" % self.arg1)

        if is_number(self.arg2):
            if self.data is not None:
                raise AssemblyException("You can only have one data")
            self.data = to_number(self.arg2)
            self.arg2 = 'data'
        elif self.arg2 not in REG:
            raise AssemblyException("Invalid register %s" % self.arg2)

    def craft(self):
        inst_bin = (REG[self.arg1] | REG[self.arg2] << 4 | REG[self.res] << 8 | INST[self.inst] << 12).to_bytes(2, byteorder='little')
        if self.data is not None:
            return inst_bin + self.data.to_bytes(2, byteorder='little')
        return inst_bin

    def size(self):
        if self.data is not None:
            return 2
        else:
            return 1


class Program:
    def __init__(self, code):
        self.marks = {}
        self.instructions = []

        line_number = -1
        for line in code:
            try:
                line_org = line
                line_number += 1
                line = line.split(';')[0]  # remove comment
                line = line.strip()
                if len(line) == 0:
                    continue

                mark = None
                if ":" in line:
                    line = line.split(":")
                    if len(line) != 2:
                        raise AssemblyException("Two many ':' in line")
                    mark = line[0].strip()
                    if len(mark) == 0:
                        raise AssemblyException("Empty mark")
                    if mark in self.marks:
                        raise AssemblyException("Mark already defined %s" % mark)
                    line = line[1]
                new_instruction = Instruction(line)
                self.marks[mark] = new_instruction
                new_instruction.mark = mark
                new_instruction.line_org = line_org
            except AssemblyException as e:
                print("Error on line %s" % line_number)
                raise e

        self.calculate_offsets()
        self.calculate_marks()

    def calculate_offsets(self):
        offset = 0
        for inst in self.instructions:
            inst.offset = offset
            offset += inst.size()

    def calculate_marks(self):
        for inst in self.instructions:
            if type(inst.data) is Mark:
                inst.data = self.marks[str(inst.data)].offset

    def get_bytecode(self):
        bytecode = bytes()
        for inst in self.instructions:
            inst_bytes = inst.craft()
            bytecode += inst_bytes
            if debug:
                str_bytes = inst_bytes[::-1].hex()
                if len(str_bytes) == 4:
                    str_bytes += " " * 4
                print(str_bytes, inst.line_org)
        return bytecode

def assemble():
    bytecode = bytes()
    code = ""
    try:
        while True:
            line = input()
            code += line + "\n"
            line = line.split(" ")
            if len(line) == 3:
                line.append('r0')
            data = None
            if line[2].isdecimal():
                data = int(line[2])
                line[2] = 'data'
            if line[3].isdecimal():
                if data is not None:
                    raise Exception("You can have only one data :(")
                data = int(line[3])
                line[3] = 'data'
            inst = craft(line[0], line[1], line[2], line[3], data)
            bytecode += inst
            print(inst[::-1].hex())
    except (KeyboardInterrupt, EOFError):
        print(bytecode.hex())
        with open('a.assembled', 'wb') as f:
            f.write(bytecode)
        with open('a.code', 'w') as f:
            f.write(code)


if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    prog = Program(linex)
    with open(sys.argv[2], 'wb') as f:
        f.write(prog.get_bytecode())
