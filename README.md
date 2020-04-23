# Algorithms

**Hw1**

```
Fine the maximum product of two distinct numbers in a sequence of non-negative integers.
(Find the 1st and 2nd largest numbers in a list, multiple them and return them)
```

**Hw2**

```
Solve the following two problems:

1)  Develop an algorithm to find the floor of a square root of an integer number. Analyze the time complexity of the proposed algorithm.

2)  Develop an algorithm to find the longest decreasing subsequence of a sequence of numbers. The elements of the subsequence need not be adjacent in the sequence. For example, the sequence <1,7, 8, 5, 4,9> has longest decreasing subsequence <7, 5, 4>. Analyze the time complexity of the proposed algorithm.
```

**Hw3**

```
Problem 1) A little kitten can hop a staircase either 1, 2, or 3 jumps at a time. 50%
  1.1) Write an algorithm that computes how many possible ways the kitten can hop up the stairs of size n.
   1.2) compute the asymptotic notation of the suggested algorithm (Big O, Theta, Omega).

Problem 2) Find and show how to compute Big O for the following algorithm: 30%
public static int getLargest(int arr[], int sz){
 int iterate1 = 0;
 int iterate2 = 0;
 int largest = 0;
  while(iterate1 < sz - 1) {
 iterate2++;
 if(iterate2 == sz) {
 iterate1++;
 iterate2 = iterate1;
 continue;
 }
 int product = arr[iterate1] * arr[iterate2];
 if(product > largest)
 largest = product;

 }
  return largest;
}

Problem 3) You have 20 M&Ms bags. 19 bags have 1.0 gram pieces, but one has pieces of weight  1.1 grams. Given a scale that provides an exact measurement, how would you find the heavy bag? You can only use the scale once.  20% Please describe your solution using a MS Word document.
```

**Hw4**

```
Solve the following problems:

Problem 1) Write a DP recursive solution to the following : A little kitten can hop a staircase either 1, 2, or 3 jumps at a time. Write an algorithm that computes how many possible ways the kitten can hop up the stairs of size n. Analyze the time complexity of your proposed solution.                         30%

Problem 2) Implement an efficient algorithm to check the First repeated character in a string. Input example: str1="ABBFSA" and str2="FEARE".                   30%

Problem 3) We have an array of numbers such as [-5, -2,  1, 3, 7, 9, 12, 17]. We need to find in this array a pair of numbers that have a certain sum such as  21. Discuss the time complexity of your solution.            30%

Problem 4) Microsoft Booking is a popular software that can take two people's calendars and find the slots that are free between them during which both can have a meeting. Write a program that reports the available times and analyzes the proposed solution. Please note that O(n^2) is not an acceptable solution                                                       10% + 20% extra credit.

You may assume that the calenders are like: Calender1 = [ “10:00, 11:00”, “13:00,14:00”]  Calender2 = [ “09:00, 11:00”, “12:00,13:00”, "14:00,15:00"]
Daily bounds from 8 to 19

A meeting duration can be like 1:00
Return a list of availability in which the two can meet.
```

**Hw5**

```
Problem 1:

A delivery truck driver travels between different stops (stations). Assume the driver has to travel from StopA to StopB. There are N ( 0 < N <=10^10) stops between A and B.
StopA, StopB, and the stops in between are on the same straight line. At each stop, the driver can travel a max distance ( >=0) from that stop towards PointB.

Returns the minimum number of stops required to reach PointB. If it is not possible to reach PointB, return -1.



Study the following example:

Example 1:  [ PointA, Stop2, Stop3, Stop4, Stop5, Stop6, Stop7, PointB ]
            [4, 2, 5, 1, 2, 1, 2, 1]



 PointA is at index 0 and PointB at index n-1 (n=8 number of stops).


The output is 2.

This is because if the driver starts with a 4 which allows him to stop at stops 2, 3, 4, and 5.  If the driver stops at Stop3 (with max distance 5) then he can reach PointB.
So the driver needs to stop at StopA and Stop3 only.


Example 2: [2, 1, 2, 1, 0, 3]

The output is -1.
There is no possible way to reach PointB.


Example 3: [2, 3, 1, 1, 4]

The output is 2.
It starts at A, then stops at Stop2, and then reach PointB.


Example 4: [2, 3, 1, 1, 4,1,1,2,1]

The output is 3.
It starts at A, then stops at the second stop, then stops at the fifth stop, and then reaches PointB.


Example 5: [2, 3, 1]

The output is 1.
It starts at A and then reaches PointB.


Problem 2: (You must be prepared to present your solution - make sure to have a working mic and a webcam)


Given a string A containing characters including ’(‘ and ’)’.
Find the length of the longest valid (well-formed) parentheses substring.
```
