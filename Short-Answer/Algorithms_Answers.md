#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) - single loop


b) O(n^2) - nested loops


c) O(n) - runs once

## Exercise II

- n-story building
- infinite eggs
- floor >= f = egg broken
- floor < f = egg not broken
- minimize broken eggs

1. find the middle floor: stories // 2 (call this "floor")
2. drop an egg
   1. if broken
      1. move down 1 floor
      2. drop another egg
      3. repeats until egg does not break
      4. add 1 to "floor"
   2. if not broken
      1. move up 1 floor
      2. drop another egg
      3. repeats until egg does break
      4. subtract 1 from floor

I think this is O(n) - there isn't a nested loop.