class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a','e', 'i','o','u','A','E', 'I','O','U'}
        arr = [l for l in s]
        start = 0
        end = len(s) -1 
        while start < end: 
            if arr[start] in vowels and arr[end] in vowels:
                arr[start] , arr[end] = arr[end],arr[start] 
                start+=1 
                end -=1 
            elif arr[start] in vowels and arr[end] not in vowels:
                end -= 1
            elif arr[end] in vowels and arr[start] not in vowels:
                start += 1
            else: 
                start+=1
                end-=1

        return "".join(arr)




        