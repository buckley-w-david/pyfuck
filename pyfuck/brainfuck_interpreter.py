

# Artisinal bespoke brainfuck interpreter
class BrainfuckInterpreter:
    def __init__(self, source_code):
        self.memory = [0]*30_000
        self.pointer = 0
        self.program_counter = 0

        self.instructions = source_code
        self.jumps = {}

        tmp = []
        for i, instruction in enumerate(self.instructions):
            if instruction == '[': # ]
                tmp.append(i)
            elif instruction == ']':
                start = tmp.pop()
                self.jumps[start] = i
                self.jumps[i] = start

    def run(self):
        while self.program_counter != len(self.instructions):
            instruction = self.instructions[self.program_counter]

            match instruction:
                case '>': self.increment_pointer()
                case '<': self.decrement_pointer()
                case '+': self.increment_memory()
                case '-': self.decrement_memory()
                case '.': self.output_memory()
                case ',': self.input_memory()
                case '[': self.jump_forward_if_zero()
                case ']': self.jump_backward_if_nonzero()
                case _: pass

            self.program_counter += 1

    def increment_pointer(self):
        self.pointer += 1

    def decrement_pointer(self):
        self.pointer -= 1

    def increment_memory(self):
        self.memory[self.pointer] += 1

    def decrement_memory(self):
        self.memory[self.pointer] -= 1

    def output_memory(self):
        print(chr(self.memory[self.pointer]), end='')

    def input_memory(self):
        self.memory[self.pointer] = ord(input())

    def jump_forward_if_zero(self):
        if self.memory[self.pointer] == 0:
            self.program_counter = self.jumps[self.program_counter]

    def jump_backward_if_nonzero(self):
        if self.memory[self.pointer] != 0:
            self.program_counter = self.jumps[self.program_counter]

    @classmethod
    def execute(cls, source_code: str):
        bf = cls(source_code)
        bf.run()
