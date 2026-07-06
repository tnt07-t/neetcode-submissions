class Solution {
public:
    vector<int> partitionLabels(string s) {
        //know a character's first and last appearance
        //-> becomes a range. then for each char in that range, makes sure same
        //-> merge intervals. sort by start time

        vector<int> last(26); //26 chars

        for (int i = 0; i < s.size(); i++){
            last[s[i] - 'a'] = i;
        }

        //go through string
        int start = 0, end = 0;
        vector<int> res;

        for (int i = 0; i < s.size(); i++){
            end = max(last[s[i]-'a'], end);
            if (i == end){ //range ends @ index
                res.push_back(end-start+1);
                start = end + 1; //starts next index
            }
        }   
        return res;

    }
};
