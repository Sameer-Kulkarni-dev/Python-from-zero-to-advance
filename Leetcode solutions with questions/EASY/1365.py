# BRUTE FORCE METHOD

class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        final_answer=[]
        for left_finger in nums:
            count_smaller=0
            for right_finger in nums:
                if right_finger<left_finger:
                    count_smaller+=1
            final_answer.append(count_smaller)
        return final_answer


#DICTIONARY METHOD
class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        # STEP 1: Line them up
        # nums is [8, 1, 2, 2, 3]
        # sorted_nums becomes [1, 2, 2, 3, 8]
        sorted_nums = sorted(nums)
        
        # STEP 2: Create our blank notebook (a dictionary)
        notepad = {}
        
        # Walk down the line to fill the notebook
        for position, number in enumerate(sorted_nums):
            
            # Only write it down if we haven't seen this number yet!
            if number not in notepad:
                notepad[number] = position
                
        # STEP 3: Pass out the answers
        final_answers = []
        for number in nums:
            # Look up the answer in our notebook
            answer = notepad[number]
            # Add it to our final list
            final_answers.append(answer)
            
        return final_answers