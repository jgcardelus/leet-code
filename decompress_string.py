## This is wrong, try again later!!


# Uncompress
#   Get char, if is letter, uncompressed
#   Get digits
#   inner = uncompress()
#   unfold
#   return


from collections import deque


def uncompress(compressed):
    compressed = deque([char for char in compressed])

    def do_uncompress(compressed):
        curr_char = compressed.popleft()

        uncompressed = []
        while ord(curr_char) >= 97 and ord(curr_char) <= 122 and compressed:
            uncompressed.append(curr_char)
            curr_char = compressed.popleft()

        if curr_char == "]" or not compressed:
            return "".join(uncompressed)

        digits = []
        while curr_char.isdigit():
            digits.append(curr_char)
            curr_char = compressed.popleft()

        repetitions = int("".join(digits))

        inner = do_uncompress(compressed)
        uncompressed = [inner for i in range(repetitions)]

        return "".join(uncompressed)

    uncompressed = []
    while compressed:
        uncompressed.extend(do_uncompress(compressed))

    return "".join(uncompressed)

print(uncompress("3[abc]4[ab]c"))
# print(uncompress("3[3[a]]"))
# print(uncompress("a"))
