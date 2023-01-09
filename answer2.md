### Ideas:
- We want to optimize get() to constant.
  - We need to use hashmap to fulfil this requirement
- About the score function:
  - It is an inverse exponential function
  - It will be hard to find the min(score) in < O(n) time, since in t=1 if score(a) > score(b), in t=5, score(a) not a must larger than score(b)
  - Although we could predict when the score level will be crossed, it takes O(n) to do so which could not speed up
  - A easiser way is to calculate the score when it is full
    - So the calculation will be O(n)

### Implementation
- Here we could use two hashmaps to put all the data
- In the first hashing, we hash the key into the key into the index of the second hashmaps
- In the second hashing, we store the value.
The implementation of get will be as follow:
- "key1" -hash-> "5, key1" (first hash)
  - If firstHash[1] == "key1", firstHash[0] -hash-> "value" (second hash), return -1
  - else return -1

The implementation of put will be as follow:
- "key1" -hash-> firstHash[index]
- If not hash crash
  - We could use a queue to store the empty space in hashmap two.
    - return index of hashMap two and store that {index, key1} in firshHash
  - If queue.empty()
    - We loop once the whole secondHash and find the min score (which takes n time complexity)
- else
  - would could use double hashing or linked list to store the value
  - Depend on the method it chose it might increase time complexity to O(log n) or even O(n)
  - But we might probably use the builtin hashmap in the language rather then implement this, since it might out of the scope of this question

### analysis
- Time complexity of get: O(1) only need two hashing
- Time complexity of put: O(n) finding min and pop
