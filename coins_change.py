def findMin(V):
    deno = [1, 2, 5, 10, 20, 50,
            100, 500, 1000]
    n = len(deno)

    ans = []
    i = n - 1

    while i >= 0:

        while V >= deno[i]:
            V -= deno[i]
            ans.append(deno[i])

        i -= 1
    for i in range(len(ans)):
        print(ans[i], end=" ")


n = int(input("Enter your amount"))
print("Following is minimal number", "of change for", n, ": ", end="")
findMin(n)