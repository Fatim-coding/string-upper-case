# create a class
class pair_elements:

    def twosum(self, nums, target):
        # craete an empty dictionary
     Lookup = {}

     # Iterate through thetuple
     for i, num in enumerate(nums):
        if target - num in Lookup:
            return (Lookup[target - num], i )
        Lookup[num] = i

value = int(input("Enter sum for which you want to make this search : "))
print("index1=%d, index2=%d" % pair_elements().twosum(10,20,30,40,50,60,70),value)
