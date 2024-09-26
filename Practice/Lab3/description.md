# Project 1 IEM
## Pesudo code
``` pesudo
Algorithm 1: Common, greedy algorithm that only adds common seeds

1. S1 ← ∅   // Initialize set S1 as an empty set
2. S2 ← ∅   // Initialize set S2 as an empty set

3. while |S1| + |S2| ≤ k do
4.     c ← argmax_c Φ(S1 ∪ {c}, S2 ∪ {c})   // Find the common seed c that maximizes the heuristic function Φ
5.     s1 ← argmax_s∈I1 Φ(S1, S2 ∪ {s})   // Find the seed s from set I1 that maximizes the heuristic function Φ when added to S2
6.     s2 ← argmax_s∈I2 Φ(S1 ∪ {s}, S2)   // Find the seed s from set I2 that maximizes the heuristic function Φ when added to S1

7.     // Choose the best option among adding common seed c, adding s1 to S1, or adding s2 to S2
8.     if Φ(S1 ∪ {c}, S2 ∪ {c}) > Φ(S1, S2 ∪ {s1}) and Φ(S1 ∪ {c}, S2 ∪ {c}) > Φ(S1 ∪ {s2}, S2)
9.        Add {c} to both S1 and S2   // Add common seed c to both sets
10.    else if Φ(S1, S2 ∪ {s1}) > Φ(S1 ∪ {s2}, S2)
11.        Add s1 to S2               // Add seed s1 only to set S2
12.    else
13.        Add s2 to S1               // Add seed s2 only to set S1

14.    // Ensure the budget constraint is not violated
15.    if |S1| + |S2| > k then
16.        Undo the last addition      // Undo the last addition if the budget is exceeded
```

这个算法是一个**贪心算法**，用于在预算 $k$的限制下，为两个集合 $S_1$和 $S_2$选择种子节点，目的是**最大化信息传播的平衡性** $\Phi&。算法通过每次贪心地选择最优的种子节点，来逐步扩展这两个集合。下面是每个步骤的详细解释：

### 1. 初始化
- 第1行和第2行分别初始化两个空集合 $S_1$和 $S_2$，它们将分别保存为两个不同信息源选择的种子节点。

### 2. 贪心选择（主循环）
- 第3行开始进入循环，直到 $|S_1| + |S_2| \leq k$为止，确保总的种子节点数不超过预算 $k$。

#### 2.1 查找最优节点
- 第4行到第6行，算法分别寻找三种可能的选择：
  1. **共同种子**：找到一个节点 $c$，将它同时添加到 $S_1$和 $S_2$中，最大化平衡性 $\Phi$。
  2. **只添加到 $S_2$**：从集合 $I_1$中找到一个种子 $s_1$，仅将其添加到 $S_2$中，最大化平衡性 $\Phi$。
  3. **只添加到 $S_1$**：从集合 $I_2$中找到一个种子 $s_2$，仅将其添加到 $S_1$中，最大化平衡性 $\Phi$。

#### 2.2 比较并选择最优选项
- 第7行到第13行，算法比较三种选择：
  - 如果共同种子 $c$同时添加到 $S_1$和 $S_2$后的平衡性 $\Phi$最大，则执行第9行，选择 $c$作为共同种子，添加到两个集合中。
  - 否则，比较在 $S_2$中添加 $s_1$和在 $S_1$中添加 $s_2$的效果，选择平衡性较好的那个。
    - 如果添加 $s_1$到 $S_2$更好，则执行第11行，添加 $s_1$到 $S_2$。
    - 如果添加 $s_2$到 $S_1$更好，则执行第13行，添加 $s_2$到 $S_1$。

### 3. 预算约束检查
- 第14行到第16行，算法检查当前两个集合的大小之和是否超过了预算 $k$。
  - 如果超出预算，则撤销最后一次添加的节点，保证节点总数不超过预算。

### 总结
这个算法通过每次**贪心地**选择最优节点，逐步将节点添加到 $S_1$和 $S_2$中，最大化信息传播的平衡性，同时确保不超出预算。