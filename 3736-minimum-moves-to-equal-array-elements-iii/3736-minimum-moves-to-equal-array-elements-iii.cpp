class Solution {
public:
    int minMoves(vector<int>& nums) {
        int maxNum, s; maxNum = s = 0;
        for (int num:nums) {
            if (num > maxNum) maxNum = num;
            s += num;
        }
        return maxNum * nums.size() -  s;
    }
};