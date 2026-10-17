class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)

        arr = []
        for i in range(n):
            arr.append((nums[i], i))

        arr.sort(key=lambda x: (sum(map(int, str(x[0]))), x))

        # 3. Mảng/Set để theo dõi các phần tử đã được duyệt qua trong chu trình
        visited = [False] * n # Khởi tạo tất cả là False

        num_swaps = 0

        # Duyệt qua từng phần tử trong danh sách đã sắp xếp
        for i in range(n):
            # arr[i] là (giá_trị_đã_sắp_xếp, chỉ_số_ban_đầu)
            
            # Nếu phần tử đã được duyệt HOẶC đã ở đúng vị trí của nó (chỉ số ban đầu == chỉ số hiện tại)
            if visited[i] or arr[i][1] == i:
                continue

            # Nếu chưa duyệt và chưa ở đúng vị trí, bắt đầu một chu trình mới
            cycle_size = 0
            j = i # Bắt đầu duyệt chu trình từ chỉ số 'i' hiện tại
            
            while not visited[j]:
                visited[j] = True # Đánh dấu là đã duyệt
                cycle_size += 1   # Tăng kích thước chu trình
                
                # Di chuyển đến vị trí tiếp theo trong chu trình
                # Vị trí tiếp theo là chỉ số ban đầu của phần tử mà arr[j] chỉ tới
                j = arr[j][1] 

            # Số lượt hoán đổi cho một chu trình có độ dài L là L - 1
            if cycle_size > 0: # Đảm bảo chỉ cộng nếu có chu trình thực sự
                num_swaps += (cycle_size - 1)

        return num_swaps