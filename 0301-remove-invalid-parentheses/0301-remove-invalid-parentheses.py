class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        res=set()
        n=len(s)
        def backtrack(i,path,depth):
            if i==n:
                if depth==0:
                    res.add("".join(path.copy()))
                return 

            if s[i]=="(":
                backtrack(i+1,path,depth)
                path.append("(")
                backtrack(i+1,path,depth+1)
                path.pop()
            
            elif s[i]==")":
                backtrack(i+1,path,depth)
                if depth<=0:
                    return
                path.append(")")
                backtrack(i+1,path,depth-1)
                path.pop()
            else:
                path.append(s[i])
                backtrack(i+1,path,depth)
                path.pop()

        backtrack(0,[],0)
        mx=max(len(x) for x in res)
        return [x for x in res if len(x)==mx]
        

