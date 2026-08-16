/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    void xyz(TreeNode* root, vector<int>& a)
    {
        if(!root) return;
        a.push_back(root->val);
        xyz(root->left,a);
        xyz(root->right,a);
        return;
    }
public:
    int getMinimumDifference(TreeNode* root) {
        vector<int> a;
        xyz(root,a);
        sort(a.begin(),a.end());
        int mn = 1e9;
        for(int i=1;i<a.size();i++)
        {
            mn = min(mn,abs(a[i]-a[i-1]));
        }
        return mn;
    }
};