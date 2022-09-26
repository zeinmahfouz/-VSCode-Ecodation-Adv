


# region rekursif_konsepti


def faktoriyel(n):
    # base alan
    if n==0:
        return 1
    else:
        return n * faktoriyel(n-1)
        #rekursif alan


print(faktoriyel(5))
# endregion