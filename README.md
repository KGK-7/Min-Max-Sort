# Min-Max Sort Algorithm 🚀

## Introduction  
Min-Max Sort is an optimized version of Selection Sort that improves efficiency  
by sorting both ends of the array simultaneously. This implementation is available  
in Java and Python.

## 📌 How It Works?  
1️⃣ Identify the minimum and maximum elements in the array in a single iteration.  
2️⃣ Swap the minimum with the leftmost element and the maximum with the rightmost.  
3️⃣ Shrink the search space by incrementing 'left' and decrementing 'right' after each iteration.  
4️⃣ Repeat until the array is fully sorted.  

This approach reduces the number of passes, making it nearly twice as fast as Selection Sort!

## 📊 Comparison with Selection Sort  

| Sorting Algorithm | Time Complexity | Space Complexity | Key Difference |
|-------------------|----------------|------------------|---------------|
| Selection Sort   | O(n²)          | O(1)            | Finds only min in each pass |
| Min-Max Sort     | O(n²)          | O(1)            | Finds both min & max in each pass |

🔹 Both have O(n²) worst-case complexity, but Min-Max Sort reduces iterations and comparisons, improving practical performance.

## 📌 Example Walkthrough  

### 🟢 Selection Sort  
For the array **[5, 3, 8, 1, 2]**:  

🔄 **Iteration 1**: Find min = 1, swap with 5 → `[1, 3, 8, 5, 2]`  
🔄 **Iteration 2**: Find min = 2, swap with 3 → `[1, 2, 8, 5, 3]`  
🔄 **Iteration 3**: Find min = 3, swap with 8 → `[1, 2, 3, 5, 8]`  
🔄 **Iteration 4**: Find min = 5, swap with 5 (no change) → `[1, 2, 3, 5, 8]`  

### 🚀 Min-Max Sort  
For the array **[5, 3, 8, 1, 2]**:  

🔄 **Iteration 1**: Find min = 1, max = 8 → Swap min with 5 and max with 2 → `[1, 3, 2, 5, 8]`  
🔄 **Iteration 2**: Find min = 2, max = 5 → Swap min with 3 and max with 5 → `[1, 2, 3, 5, 8]`  
🔄 **Iteration 3**: The array is already sorted.  

## 📊 Performance Comparison  

| Feature                      | Selection Sort | Min-Max Sort |
|------------------------------|---------------|-------------|
| Elements Placed per Iteration | 1 (minimum)   | 2 (min & max) |
| Comparisons per Iteration    | O(n)         | O(n) (slightly higher) |
| Swaps per Iteration          | 1           | 2  |
| Time Complexity              | O(n²)      | O(n²) (but fewer iterations) |
| Space Complexity             | O(1)        | O(1) (iterative version) |
