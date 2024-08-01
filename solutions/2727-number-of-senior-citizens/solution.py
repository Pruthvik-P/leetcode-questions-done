class Solution:
    def countSeniors(self, details: List[str]) -> int:
        senior_citizen = 0
        for i in details:
            if int(i[11:13]) > 60:
                senior_citizen +=1
        return senior_citizen
        
