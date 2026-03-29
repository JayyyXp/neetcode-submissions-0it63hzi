class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #numUnique =len(set(task))
        taskToNum = {}
        for task in tasks:
            if task in taskToNum:
                taskToNum[task] += 1
            else:
                taskToNum[task] = 1
        
        max_key = max(taskToNum, key=taskToNum.get)
        print("max_key", max_key)
        print("max_key_val", taskToNum[max_key])
        # Initialize an empty dictionary to store value counts
        value_counts = {}

        # Iterate through the dictionary values and count occurrences
        for value in taskToNum.values():
            if value in value_counts:
                value_counts[value] += 1
            else:
                value_counts[value] = 1
        nbrMaxKeys = value_counts[taskToNum[max_key]]
        print("number of max keys", nbrMaxKeys)
        #if nbrMaxKeys == 1:
        #    return (taskToNum[max_key] * n)
        #else:
            #ans = 0
            #for i in range(taskToNum[max_key] ):
            #    ans += 1 + n
            #return ans -1
        return max(len(tasks),(taskToNum[max_key] - 1) * (n + 1) + nbrMaxKeys)
            # AB__AB__AB__AB 