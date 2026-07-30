class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs:
            encoded_string = "@121".join(strs)
            return encoded_string
        return "1.1.1.1.12"
    def decode(self, s: str) -> List[str]:
        if s == "1.1.1.1.12":
            return []
        return s.split('@121')
