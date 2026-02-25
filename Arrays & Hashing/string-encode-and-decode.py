class Solution:
    # # non-ascii character as a delimiter.
    # def encode(self, strs: List[str]) -> str:
    #     code = ""
    #     for text in strs:
    #         code += ' '.join(format(byte, '08b') for byte in text.encode('utf-8'))
    #         code += " _ "
    #     return code
    
    # # non-ascii character as a delimiter.
    # def decode(self, s: str) -> List[str]:
    #     result = []
    #     text = ""
    #     for binary in s.split():
    #         if binary == "_":
    #             result.append(text)
    #             text = ""
    #             continue
    #         text += ''.join(chr(int(binary, 2)))
    #     return result
    
    # get the size of each str
    def encode(self, strs: List[str]) -> str:
        code = ""
        for text in strs:
            code += str(len(text))
            code += "+"
        code += "_"
        
        for text in strs:
            code += text
        return code

    # get the size of each str
    def decode(self, s: str) -> List[str]:
        lengths = []
        end = 0
        result = []
        text = ""
        for i in range(0,len(s)):
            if s[i] == "_":
                end = i+1
                break
            if s[i] == "+":
                lengths.append(int(text))
                text = ""
            else:
                text += s[i]

        for length in lengths:
            text = ""
            for i in range(0, length):
                text += s[end + i]
            end += length
            result.append(text)
        return result

code = Solution().encode(["Hello","World"])
print(code)
print(Solution().decode(code))
