class Solution {
public:
    bool isPalindrome(string s) {
       for (int i = 0; i < s.length(); i++){
            char ch= s[i];

            if (ch <= 'Z' && ch >= 'A'){
            ch = ch - ('A' - 'a');
            s[i] = ch;
            }
        }

        int a = 0;
        int e = s.length()-1;

        while(a<=e){
            if (isalnum(s[a]) == 0){
            ++a;
            }

            else if (isalnum(s[e]) == 0){
            --e;
            }

            else if(s[a] == s[e]){
                ++a;
                --e;
            }

            else{
                return false;
            }
        }
        return true;
    }
};
