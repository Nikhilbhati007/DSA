struct ListNode* createnode(int data, struct ListNode* head1) {
    struct ListNode* newnode = (struct ListNode*)malloc(sizeof(struct ListNode));
    newnode->val = data;
    newnode->next = NULL;

    if (head1 == NULL || data < head1->val) {
        newnode->next = head1;
        head1 = newnode;
        return head1;
    }

    struct ListNode* temp = head1;
    struct ListNode* prev = NULL;

    while (temp != NULL && temp->val < data) {
        prev = temp;
        temp = temp->next;
    }

    newnode->next = temp;

    if (prev != NULL)
        prev->next = newnode;
    else
        head1 = newnode;

    return head1;
}

struct ListNode* insertionSortList(struct ListNode* head) {
    if (head == NULL) return NULL;

    struct ListNode* head1 = NULL;
    struct ListNode* temp = head;

    while (temp != NULL) {
        head1 = createnode(temp->val, head1);
        temp = temp->next;
    }

    return head1;
}