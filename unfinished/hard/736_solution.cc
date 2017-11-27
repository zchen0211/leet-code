/*
iIf the expression is a variable, we look up in the map and return the variable value. If the expression is a value, we simply return its value.

For the "let" case, we first get the variable name, and the following expression. Then we evaluate the expression, and use a map to assign the expression value to the variable. For example, consider "(let x (add 2 3) x)", the variable is "x", and we evaluate the expression "(add 2 3)", and assign x = 5. For the last "x", we recursively call the help function, and get its value 5.

For the "add" case, we evaluate the value of the first expression, and the second expression, and add them together. For example, consider "(add (add 2 3) (add 3 4))", the first expression is "(add 2 3)", and the second expression is "(add 3 4)". We get 5 after evaluating "(add 2 3)", and get 7 after evaluating "(add 3 4)", and we will return 12.

The "mult" case is similar to the "add" case.
*/

class Solution {
public:
    int evaluate(string expression) {
        unordered_map<string,int> myMap;
        return help(expression,myMap);
    }
    
    int help(string expression,unordered_map<string,int> myMap) {
        if ((expression[0] == '-') || (expression[0] >= '0' && expression[0] <= '9'))
            return stoi(expression);
        else if (expression[0] != '(')
            return myMap[expression];
        //to get rid of the first '(' and the last ')'
        string s = expression.substr(1,expression.size()-2);
        int start = 0;
        string word = parse(s,start);
        if (word == "let") {
            while (true) {
                string variable = parse(s,start);
                //if there is no more expression, simply evaluate the variable
                if (start > s.size())
                    return help(variable,myMap);
                string temp = parse(s,start);
                myMap[variable] = help(temp,myMap);                    
            }
        }
        else if (word == "add") 
            return help(parse(s,start),myMap) + help(parse(s,start),myMap);
        else if (word == "mult") 
            return help(parse(s,start),myMap) * help(parse(s,start),myMap);
    }
    
    //function to seperate each expression
    string parse(string &s,int &start) {
        int end = start+1, temp = start, count = 1;
        if (s[start] == '(') {
            while (count != 0) {
                if (s[end] == '(')
                    count++;
                else if (s[end] == ')')
                    count--;
                end++;
            }
        }
        else {
            while (end < s.size() && s[end] != ' ')
                end++;
        }
        start = end+1;
        return s.substr(temp,end-temp);
    }
};
