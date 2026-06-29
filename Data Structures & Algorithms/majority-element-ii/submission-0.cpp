class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int threshold = nums.size() / 3;
        unordered_map<int, int> count;
        for (int n : nums){
            count[n]++;
        }

        vector<int> res;
        for (auto& [key,count] : count){ // for k,v in map.items()
            if (count > threshold){
                res.push_back(key); //like python list.append()
            }
        }

        return res;
    }
};