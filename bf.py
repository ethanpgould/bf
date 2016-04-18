import sys
import re


def execute(code):
  code = re.sub(r'[^><+-.,\[\]]', '', code)
  bracket_map = make_bracket_map(code)

  data = [0]
  data_idx = 0
  code_idx = 0

  while code_idx < len(code):
    command = code[code_idx]

    # tell the interpreter how to react to each Brainf*ck command symbol 
    if command == '>':
      if data_idx == len(data) - 1:
        data.append(0)

      data_idx += 1

    elif command == '<':
      if data_idx > 0:
        data_idx = data_idx - 1

    elif command == '+':
      data[data_idx] = data[data_idx] + 1

    elif command == '-':
      data[data_idx] = data[data_idx] - 1

    elif command == '.':
      print chr(data[data_idx]),

    elif command == ',':
      data[data_idx] = int(raw_input(""))

    elif command == '[':
      if data[data_idx] == 0:
        code_idx = bracket_map[code_idx]

    elif command == ']':
      if data[data_idx] != 0:
        code_idx = bracket_map[code_idx]

    code_idx += 1


def make_bracket_map(code):
  bracket_map = {}
  start_index_stack = []

  for i in range(len(code)):
    command = code[i]

    if command == '[':
      start_index_stack.append(i)
    elif command == ']':
      start = start_index_stack.pop()

      bracket_map[start] = i
      bracket_map[i] = start

    i += 1

  return bracket_map

if __name__ == '__main__':
  # with open(sys.argv[1]) as f:
    # code = f.read()

  # execute(code)
  execute(sys.argv[1])
