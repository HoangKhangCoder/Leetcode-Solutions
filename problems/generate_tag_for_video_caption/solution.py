class Solution:
    def generateTag(self, caption: str) -> str:
        result = ['#']
        space = 0
        len_result = 0
        for i in range(len(caption)):
            charac = caption[i]
            if charac == ' ' and len_result > 0:
                space = 1
                continue
                
            if not charac.isalpha():
                continue
                
            if len_result == 0:
                result.append(charac.lower())
            else:
                if space == 1:
                    result.append(charac.upper())
                    space = 0
                else:
                    result.append(charac.lower())
            len_result += 1
                
        return ''.join(result[:100])