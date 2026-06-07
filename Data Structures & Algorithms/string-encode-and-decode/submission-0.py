class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s

        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            size = int(s[i:j])
            result.append(s[j + 1 : j + 1 + size])
            i = size + j + 1
        return result