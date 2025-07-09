
def decompress(compressed):
    def do_decompress(compressed, cursor):
        i = cursor
        uncompressed = ""
        while i < len(compressed):
            character = compressed[i]

            if ord(character) >= 97 and ord(character) <= 122:
                uncompressed += character
                i += 1
                continue

            if character == "]":
                break

            digits = ""
            while i < len(compressed) and compressed[i].isdigit():
                digits += compressed[i]
                i += 1

            # where at [

            inner, i = do_decompress(compressed, i+1)

            # returns at ]
            repeat = int("".join(digits))
            uncompressed += "".join([inner for i in range(repeat)])
            i+=1

        return uncompressed, i


    uncompressed, _ = do_decompress(compressed, 0)
    return uncompressed

print(decompress("ab3[2[cd]e]f"))
print(decompress("abc"))
