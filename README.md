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
