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
		int[] stairArr = new int[n + 1];
		// n = 0, the answer is 1. We can only take no steps
		stairArr[0] = 1;
		// n = 1, the answer is 1. We can only take 1 step
		stairArr[1] = 1;
		// This represents only taking 2 steps
		stairArr[2] = 2;
		
		// 3 gets set on the first run and is now saved and this is repeated aka Memoization 
		for (int i = 3; i <= n; i++) {
		  stairArr[i] = stairArr[i - 1] + stairArr[i - 2] + stairArr[i - 3];
		}
		
		return stairArr[n];
	}
		// Time Complexity: O(n)
		// var |= value is short for var = var | value
		// The signed left shift operator "<<" shifts a bit pattern to the left
		// The signed right shift operator ">>" shifts a bit pattern to the right.
		// The unsigned right shift operator ">>>" shifts a zero into the leftmost position
	 public static int FindRepeated(String str) {
		// checker will contain 32 bits that will represent each lowercase letter in the alphabet
		// The lowest bit will represent a and the 26th is z
		// An integer to store presence/absence 
        // of 26 characters using its 32 bits. 
        int checker = 0; 
        // The first round in the for loop checker is equal to 32 0s and if we get b as the first letter 
      	// we will compare if both variables have 1 in the same positions
        for (int i = 0; i < str.length(); ++i) 
        { 
			// When you type 'a' you will get the char a wich is represented by the int 97. 
			// So lets say you take 'c' - 'a' you will get 99 - 97 = 2
			// wich is 0010 in binary
            int val = (str.charAt(i)-'a'); 
            // if (0 & 1 ) > 1 same as if (0000 & 0001 ) > 1 that will return 0000 wich is not > 1
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
	 
	 // Time Complexity: O(n)
	 public static boolean hasArrayTwoCandidates(int A[], int arr_size, int sum) { 
		 
		int l, r; 
		/* Sort the elements */
		Arrays.sort(A); 
		
		/* Now look for the two candidates  
		in the sorted array*/
		// left part of the index
		l = 0; 
		// last index in the array
		r = arr_size - 1; 

		//while the index to the left is less then the right index, meaning they havent intersected yet
		while (l < r) { 
			// if value of l + value of r equals the sum we are looking for
			if (A[l] + A[r] == sum) 
				return true; 		
			// else if its less then the some, increment l, this will make sure we add value
			// next time we check since its sorted
			else if (A[l] + A[r] < sum) 			
				l++; 
			// else it means that the sum we got was to high and we need to move r more to the left
			// this makes r a lesser value because the array is sorted.
			else // A[i] + A[j] > sum 	
				r--; 
		} 
		return false; 
	} 
	 
		
}
