package hw4;

import java.util.Arrays;

public class Driver {
	public static void main(String[] args) {
		System.out.println(climbStairs(6));
		System.out.println(FirstRepeated("ABBFSA"));
		
        int A[] = { -5, -2,  1, 3, 7, 9, 12, 17 }; 
        int n = 21; 
        int arr_size = A.length; 
		System.out.println(hasArrayTwoCandidates(A,arr_size,n));

	}
		// Problem 1
		// Climbing Stairs with Recurrsive Dynamic programming 
		// Time Complexity: O(n) Method
	  public static int climbStairs(int n) {
		/*
		  In programming we all know we index off of 0. This is why
		  we create an array of size n + 1. It is so we can just return
		  dp[n] at the end instead of fumbling with dp[n - 1].
		  If n = 4 we will get an array like this if we just did "new int[n];":
		  [0, 0, 0, 0]
		   0  1  2  3
		  If we instead do "new int[n + 1" we have:
		  [0, 0, 0, 0, 0]
		   0  1  2  3  4
		   And now we can be literal in how we access the nth subproblem
		*/
		int[] dp = new int[n + 1];
		
		// n = 0, the answer is 1. We can only take no steps
		dp[0] = 1;
		
		// n = 1, the answer is 1. We can only take 1 step
		dp[1] = 1;
		
		// n = 2, the answer is 1. We can only take 2 step
		dp[2] = 2;

		/*
		  The answer to the ith subproblem is the sum between the answer
		  to the subproblems of climbing i - 1 stairs and i - 2 stairs
		*/
		for (int i = 3; i <= n; i++) {
		  dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
		}
		
		/*
		  This is what we want and built to the while way. The answer for
		  the total unique ways to climb n steps when we can either take a
		  1 step or 2 step
		*/
		return dp[n];
	}
	  //Time Complexity: O(n)
	 public static int FirstRepeated(String str) {
		// An integer to store presence/absence 
        // of 26 characters using its 32 bits. 
        int checker = 0; 
       
        for (int i = 0; i < str.length(); ++i) 
        { 
            int val = (str.charAt(i)-'a'); 
            
            // If bit corresponding to current 
            // character is already set 
            if ((checker & (1 << val)) > 0) {
                System.out.println(str.charAt(i));
                return i; 
            }
            // set bit.wise in checker 
            checker |= (1 << val); 
        } 
        return -1; 
    }
	 
	 //Time Complexity: O(n)
	 public static boolean hasArrayTwoCandidates(int A[], int arr_size, int sum) { 
		 
		int l, r; 
		/* Sort the elements */
		Arrays.sort(A); 
		
		/* Now look for the two candidates  
		in the sorted array*/
		l = 0; 
		r = arr_size - 1; 
		while (l < r) { 
			if (A[l] + A[r] == sum) 
				return true; 		
			else if (A[l] + A[r] < sum) 			
				l++; 
			else // A[i] + A[j] > sum 	
				r--; 
		} 
		return false; 
	} 
	 
		
}
