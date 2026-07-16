Problem 1071 - Greatest Common Divisor of Strings.

Topic: Strings.

Approach: loop through sum of both the given strings in two ways (1+2 and 2+1).
          If the two ways of sum are not equal then the given strings have nothing in common, so no GCD.
          But, if the are equal then the GCD is found for the length of the given strings and that many letters of any of the string is returned as the result.
