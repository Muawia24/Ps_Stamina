class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        prev_or_results = set()
        all_or_results = set()
        

        for num in arr:
            curr_or_results = {num}
            for prev in prev_or_results:
                curr_or_results.add(prev | num)
    
            all_or_results.update(curr_or_results)
            prev_or_results = curr_or_results
        
        return len(all_or_results)

        