/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* modifiedList(vector<int>& nums, ListNode* head) {
        unordered_set<int> to_rem(nums.begin(),nums.end());
        while(head && to_rem.count(head->val)){
            head = head->next;
        }
        ListNode* temp = head;
        while(temp && temp->next){
            if(to_rem.count(temp->next->val)){
                temp->next = temp->next->next;
            }
            else temp = temp->next;
        }
        return head;
    }
};