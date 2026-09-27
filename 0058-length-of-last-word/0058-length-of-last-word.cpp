class Solution {
public:
    int lengthOfLastWord(string s) {
        int endIdx = s.size() - 1;
        while (endIdx >= 0 && s[endIdx] == ' ') {
            endIdx --;
        }

        int start = endIdx;
        while (start >= 0 && s[start] != ' ') {
            start --;
        }

        return endIdx - start;
    }
};