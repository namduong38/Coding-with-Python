#Given A =[13,7,2,8,3] your function should return 3. #Given A =[13,7,2,8,3] your function should return 1. The AND of eachpair from the array is equal to 0.
#Given A = [16,16] your function should return 2. The AND of both number is 16.
#Write an efficient algorithm for the following assumptions:
#N is an odd integer within the range [1..1,000,000];
#each element of array A is an integer within the range [1..1,000,000,000];

def solution(A):
    # write your code in Python 3.6
    if len(A) == 1:
        return 0
    if len(A) == 2:
        return A[0] & A[1]
    if len(A) == 3:
        return A[0] & A[1] & A[2]
    if len(A) == 4:
        return A[0] & A[1] & A[2] & A[3]
    if len(A) == 5:
        return A[0] & A[1] & A[2] & A[3] & A[4]
    if len(A) == 6:
        return A[0] & A[1] & A[2] & A[3] & A[4] & A[5]
    if len(A) == 7:
        return A[0] & A[1] & A[2] & A[3] & A[4] & A[5] & A[6]
    if len(A) == 8:
        return A[0] & A[1] & A[2] & A[3] & A[4] & A[5] & A[6] & A[7]
    if len(A) == 9:
        return A[0] & A[1] & A[2] & A[3] & A[4] & A[5] & A[6] & A[7] & A[8]
    if len(A) == 10:
        return A[0] & A[1] & A[2] & A[3] & A[4] & A[5] & A[6] & A[7] & A[8] & A[9]



print(solution([13,7,2,8,3]))
