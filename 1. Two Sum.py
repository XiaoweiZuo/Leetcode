class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # #main function
        # error = 0
        # for i in range(0,len(nums)):
        #     for j in range( i+1, len(nums) ):
        #         test_sum = nums[i] + nums[j]
        #         if test_sum == target:
        #             return [i, j]
        #         else:
        #             error = -1
        
        # if error == -1:
        #     print("No such two integers found.")
                    
    # function definition
        def bi_search(nums, difference, start_psn, end_psn):
            if start_psn <= end_psn:
                mid_psn = int((start_psn + end_psn)/2)
                if difference == nums[mid_psn]:
                    return mid_psn
                elif difference > nums[mid_psn]:
                    return bi_search(nums, difference, mid_psn + 1, end_psn)
                else:
                    return bi_search(nums, difference, start_psn, mid_psn - 1)
            else:
                return -1

    # main function
        old_array = nums

        # small to big #O(n)
        nums = sorted(nums) # this sorted() does not change the original array
                            # sort() will change the original array globally
        error = 0

        for i in range(0,len(nums)):
            #找中间值，然后跟目前需要的差值比较，找到差值后return差值的index
            difference_index = bi_search(nums,target-nums[i],0,len(nums)-1)
            print(difference_index)
            
            if difference_index == -1:
                error = -1
            else:
                if i != difference_index:
                    val_1 = nums[i]
                    val_2 = nums[difference_index]
                    index_1 = -1
                    index_2 = -1
                    if val_1 != val_2:
                        for j in range(0,len(old_array)):
                            if val_1 == old_array[j]:
                                index_1 = j
                                print(index_1)
                            if val_2 == old_array[j]:
                                index_2 = j
                                print(index_2)
                        # return [index_1, index_2]
                    else:
                        for j in range(0,len(old_array)):
                            if val_1 == old_array[j]:
                                index_1 = j
                                for k in range(j+1,len(old_array)):
                                    if val_2 == old_array[k]:
                                        index_2 = k
                                break
                        # return [index_1, index_2]
                    return [index_1, index_2]
                    
        if error == -1:
            print("No such two integers found.")
        




            











