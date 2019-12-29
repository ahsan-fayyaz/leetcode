# The Tribonacci sequence Tn is defined as follows:

# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

# Given n, return the value of Tn.
def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if((n == 0) or (n==1) or (n==2)):
            return n

        else:
            t0 = 0
            t1 = 1
            t2 = 1

            for i in range(1,n):
                next = t0 + t1 + t2
                t0 = t1
                t1 = t2
                t2 = next

            return t1



#Passed
#Runtime: 28ms
