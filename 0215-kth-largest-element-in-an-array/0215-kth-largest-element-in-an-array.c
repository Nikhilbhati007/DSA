
void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void heapifyDown(int heap[], int size, int i) {
    int smallest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < size && heap[left] < heap[smallest])
        smallest = left;
    if (right < size && heap[right] < heap[smallest])
        smallest = right;

    if (smallest != i) {
        swap(&heap[i], &heap[smallest]);
        heapifyDown(heap, size, smallest);
    }
}

void heapifyUp(int heap[], int i) {
    int parent = (i - 1) / 2;
    if (i > 0 && heap[i] < heap[parent]) {
        swap(&heap[i], &heap[parent]);
        heapifyUp(heap, parent);
    }
}

int findKthLargest(int* nums, int n, int k) {
    int* heap = (int*)malloc(k * sizeof(int));
    int heapSize = 0;

    for (int i = 0; i < n; i++) {
        if (heapSize < k) {
            heap[heapSize] = nums[i];
            heapifyUp(heap, heapSize);
            heapSize++;
        } else if (nums[i] > heap[0]) {
            heap[0] = nums[i];
            heapifyDown(heap, k, 0);
        }
    }

    int result = heap[0];
    free(heap);
    return result;
}
