

def removeDup(A):
        if A is []:
            return 0

        newtail = 0
        B= []
        for i in range(1, len(A)):
            if A[i] != A[newtail]:
                newtail = newtail+ 1
                A[newtail] = A[i]

        return (newtail + 1, A)

print removeDup([1,2,2,3,3])
