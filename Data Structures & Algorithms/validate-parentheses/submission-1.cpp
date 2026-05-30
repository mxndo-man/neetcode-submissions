class Solution {
public:
    bool isValid(string s) {
        //i can see the stack solution
        stack<char> myStack;
       //if(s.() == 0 || s.length() == 1) return false; 
        for (auto it : s){
            if (it == '(' || it == '{' || it == '[')
                myStack.push(it);
            else{
                if(myStack.empty()) return false;
                char top = myStack.top();
                myStack.pop();
                if(it == ')' && top !='(') return false;
                if(it == '}' && top !='{') return false;
                if(it == ']' && top !='[') return false;
            }
        }
        return myStack.empty();
    }
};
