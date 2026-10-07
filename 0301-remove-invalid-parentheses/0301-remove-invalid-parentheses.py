class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        res = []
        def is_valid(string):
            count = 0
            for ch in string:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        def dfs(index, left, right, path):
            if left == 0 and right == 0:
                remaining = s[index:]

                for ch in remaining:
                    if ch == '(':
                        path += '('
                    elif ch == ')':
                        path += ')'
                    else:
                        path += ch
                if is_valid(path):
                    res.append(path)
                return

            if index == len(s):
                return
            ch = s[index]
            if ch == '(' and left > 0:
                dfs(index + 1, left - 1, right, path)
            if ch == ')' and right > 0:
                dfs(index + 1, left, right - 1, path)

            dfs(index + 1, left, right, path + ch)

        left_remove = 0
        right_remove = 0

        for ch in s:
            if ch == '(':
                left_remove += 1
            elif ch == ')':
                if left_remove > 0:
                    left_remove -= 1
                else:
                    right_remove += 1

        # Use BFS to guarantee minimum removals
        queue = [s]
        visited = {s}
        while queue:
            found = False
            for current in queue:
                if is_valid(current):
                    res.append(current)
                    found = True
            if found:
                return list(set(res))
            next_queue = []
            for current in queue:
                for i in range(len(current)):
                    if current[i] not in "()":
                        continue
                    if i > 0 and current[i] == current[i - 1]:
                        continue
                    new_string = current[:i] + current[i + 1:]
                    if new_string not in visited:
                        visited.add(new_string)
                        next_queue.append(new_string)
            queue = next_queue

        return res