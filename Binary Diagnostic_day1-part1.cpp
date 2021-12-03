#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    // your code goes here
    freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout);
    string s,g,e;
    vector<string> a;
    while(getline(cin,s)){
        a.push_back(s);
    }
    for(int i=0;i<a[0].size();i++){
        int c0=0,c1=0;
        for(int j=0;j<a.size();j++){
            if(a[j][i]=='0')c0++;
            else c1++;
        }
        cout<<"c1="<<c1<<" c0="<<c0<<'\n';
        if(c1>c0){
            g+='1';e+='0';
        }
        else{
            g+='0';e+='1';
        }
    }
    cout<<"g="<<g<<" e="<<e<<'\n';
    cout<<(stoi(g,nullptr,2)*stoi(e,nullptr,2));
    return 0;
}
