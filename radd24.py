def rAddtwentyfour(nums):

    if nums == 24:
        print("Is 24")
        return nums

    else:
        print(nums, "does not equal 24")
        print(str(24 - nums), "iterations until 24")
        return rAddtwentyfour(nums + 1)



def main():

    rAddtwentyfour(5)


main()
        
