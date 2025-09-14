class Solution(object):
    def spellchecker(self, wordlist, queries):
        exact = set(wordlist)
        cap = {}
        vowel = {}
        result = []

        for w in wordlist:
            l = w.lower()
            if l not in cap:
                cap[l] = w

        for w in wordlist:
            pattern = ""
            for c in w.lower():
                if c in "aeiou":
                    pattern += "*"
                else:
                    pattern += c
            if pattern not in vowel:
                vowel[pattern] = w
        
        for q in queries:
            if q in exact:
                result.append(q)
            elif q.lower() in cap:
                result.append(cap[q.lower()])
            else:
                p = ""
                for c in q.lower():
                    if c in "aeiou":
                        p += "*"
                    else:
                        p += c
                if p in vowel:
                        result.append(vowel[p])
                else:
                        result.append("")

        return result
