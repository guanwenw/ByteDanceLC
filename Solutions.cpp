class Solution {
public:
    // 977 Squares of a Sorted Array
    vector<int> sortedSquares(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(n);
        for(int i = 0; i < n; i++){
            ans[i] = nums[i] * nums[i];
        }
        sort(ans.begin(), ans.end());
        return ans;
    }

    // 206 Reverse Linked List
    ListNode* reverseList(ListNode* head) {
        ListNode* newHead = nullptr;
        ListNode* cur = head;
        while(cur != nullptr){
            ListNode* tmp = cur->next;
            cur->next = newHead;
            newHead = cur;
            cur = tmp;
        }
        return newHead;
    }

};
