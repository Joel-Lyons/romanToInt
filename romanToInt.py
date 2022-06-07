class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rn = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
        char_count = len(s)
        i = 0
        rval = 0

        for _ in range(char_count):
            if (i + 1 <= char_count):
                if (i + 1 < char_count and s[i] + s[i+1] in rn.keys()):
                    key = s[i] + s[i+1]
                    i += 2
                else:
                    key = s[i]
                    i += 1
                amt = rn[key]
                rval += amt
        return rval