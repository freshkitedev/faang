# print below staircase for n = 3
#  #
#  ##
#  ###

def staircase(n):
    for r in range(1, n + 1):
        for c in range(1, r + 1):
            print("#", end="")
        print("")

staircase(5)