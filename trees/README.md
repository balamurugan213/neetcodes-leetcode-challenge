# Things learned

- In the invert binary tree problems, the solution 2 is effective just by adding some extra conditions to check left and right child *(root.right==None and root.left==None)* - so it avoids the recursion for the leaf nodes.

- But we are checking the left and right child in each recursion it. So, it will be more time consuming in each recursive step which could end up in more runtime than without condition.

- Using a function inside a function is a good way to avoid using global variables.It will be helpful in storing value in recursion.
