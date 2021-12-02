#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main() {
    // your code goes here
    freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout);
    string s;
    int x=0,y=0,n=0,m=0;
    while(getline(cin,s)){
        for(auto y:s){
            if(isdigit(y)){
                n=n*10+(y-'0');
            }
        }
        if(s[0]=='f'){
            x+=n;
            y+=m*n;
        }
        if(s[0]=='d')m+=n;
        if(s[0]=='u')m-=n;
        n=0;
    }
    cout<<(abs(x)*abs(y));
    return 0;
}
