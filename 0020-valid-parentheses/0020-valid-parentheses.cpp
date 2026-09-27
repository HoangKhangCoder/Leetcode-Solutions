class Solution {
public:
    bool isValid(string s) {

        vector<char> stack;
        for (char c:s) {
            if (c == ')') {
                if (stack.size() == 0 || stack[stack.size() - 1] != '(') {
                    return false;
                }
                stack.pop_back(); continue;
            }

            if (c == ']') {
                if (stack.size() == 0 || stack[stack.size() - 1] != '[') {
                    return false;
                }
                stack.pop_back(); continue;
            }

            if (c == '}') {
                if (stack.size() == 0 || stack[stack.size() - 1] != '{') {
                    return false;
                }
                stack.pop_back(); continue;
            }

            stack.push_back(c);
        }
        return stack.empty();
    }
};