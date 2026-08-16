class Solution {

    int ht(TreeNode* root)
    {
        if(!root) return 0;
        return max(ht(root->left),ht(root->right)) + 1;
    }

    void xyz(TreeNode* root, int& i, vector<int>& a)
    {
        if(!root) return;

        if(a[i] < root->val) a[i] = root->val;

        i++;
        xyz(root->left,i,a);
        xyz(root->right,i,a);
        i--;

        return;
    }

public:
    vector<int> largestValues(TreeNode* root) {
        int maxht = ht(root);
        if(!root) return {};

        vector<int> a(maxht, INT_MIN);

        int i = 0;
        xyz(root,i,a);

        return a;
    }
};