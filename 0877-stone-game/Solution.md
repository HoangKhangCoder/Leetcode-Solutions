# 💡 [Python] 1-Line O(1) Solution | Detailed Mathematical Proof 🧠


# 💡O(1) Solution | Detailed Mathematical Proof 🧠
![Screenshot 2026-08-02 at 08.49.04.png](https://assets.leetcode.com/users/images/547ea98c-b261-4f35-9a2b-e63b37744f01_1785635363.0753534.png)

### ⚡ Direct Answer First
The answer is always `return True`. Since the number of piles is even and the total number of stones is odd, Alice (the first player) can **always** force a win by choosing a strategy that Bob cannot counter.

---

### 🎨 Intuition & Strategy
Let's break down why Alice always wins. The game has two key constraints:
1. The total number of piles is **even**.
2. The total number of stones is **odd** (no ties possible).

Alice can color the piles alternately into two groups: **Odd indexed piles** and **Even indexed piles**.

* **Example:** `piles = [5, 3, 4, 5]`
  * Even indices (0, 2): `piles[0] = 5`, `piles[2] = 4` → Total = 9 stones.
  * Odd indices (1, 3): `piles[1] = 3`, `piles[3] = 5` → Total = 8 stones.

Alice can calculate the sum of both groups before making her first move. Since the total number of stones is odd, one group **must** have more stones than the other. In this case, the even group (9 stones) is larger.

---

### 🔍 How Alice Controls the Game (The Proof)
Alice wants to take all the piles from the larger group (e.g., the **even** group). 

1. **Alice's 1st move:** She takes `piles[0]` (an even index).
2. **The situation now:** The remaining piles are `[3, 4, 5]`. Notice that both available ends (`piles[1]` and `piles[3]`) are **odd indices**.
3. **Bob's move:** No matter what Bob chooses, he is forced to take an **odd index** pile.
4. **Alice's next move:** After Bob takes an odd index, he exposes another **even index** pile for Alice.

By repeating this strategy, Alice takes **all even-indexed piles**, leaving Bob with **all odd-indexed piles**. Since Alice chose the larger group at the beginning, she is guaranteed to win.

---

### ⚙️ Code Implementation

Here is the implementation in Python. This runs in O(1) time and space complexities.

```python []
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # Alice can always choose the strategy to win
        return True
```
```C++ []
class Solution {
public:
    bool stoneGame(vector<int>& piles) {
        // Alice always wins due to the even number of piles and odd total stones
        return true;
    }
};
```
```java []
class Solution {
    public boolean stoneGame(int[] piles) {
        // Alice can always pick the winning group (odd vs even indices)
        return true;
    }
}
```
```ruby []
# @param {Integer[]} piles
# @return {Boolean}
def stone_game(piles)
    # Alice always has a winning strategy
    true
end
```
```Go []
func stoneGame(piles []int) bool {
    // Alice can always force a win based on parity
    return true
}
```


---

### 📊 Complexity Analysis

* **Time Complexity:** $\mathcal{O}(1)$ — No loops, no recursion, just a constant-time return statement.
* **Space Complexity:** $\mathcal{O}(1)$ — No extra space is used.

---

### 💡 Hidden Hints (Click to expand)

<details>
<summary>Hint 1</summary>

Can Alice split the piles into 2 groups that she can completely control?
</details>

<details>
<summary>Hint 2</summary>

If Alice divides the piles into odd indices and even indices and chooses the larger group, how can she force Bob to take the other group?
</details>
