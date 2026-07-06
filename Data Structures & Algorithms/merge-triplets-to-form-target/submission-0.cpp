class Solution {
public:
    bool mergeTriplets(vector<vector<int>>& triplets, vector<int>& target) {
        bool p1 = 0, p2 = 0, p3 = 0;
        
        for (vector<int>& triplet : triplets){
            //no merge if any elem in triplet > target 
            if (triplet[0] > target[0] || 
            triplet[1] > target[1] || 
            triplet[2] > target[2]) {
                continue;
            }

            if (triplet[0] == target[0]) p1 = true;
            if (triplet[1] == target[1]) p2 = true;
            if (triplet[2] == target[2]) p3 = true;
            
        }

        return p1 && p2 && p3;
    }
};
