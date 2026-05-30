class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length())
            return false;

        unordered_map<char,int> myAnagram;
        for (auto it : s)
            myAnagram[it]++;
        for (auto it : t){
            //Below if it was present
            //if(myAnagram.find(it) == myAnagram.end() || myAnagram[it] == 0  )
            // is not present 
            if(myAnagram.find(it) == myAnagram.end() || myAnagram[it] == 0  )
                return false ;
            myAnagram[it]--;
            
        }
        return true;
    }
};
