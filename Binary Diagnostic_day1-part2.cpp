#include <iostream>
#include <vector>
#include <string>
using namespace std;
vector<string> oxygen(vector<string> a, int k)
{
    if(a.size()==1)return a;
    else
    {
        int c0=0,c1=0;
        vector<string> index0,index1;
        for(int j=0;j<a.size();j++){
            if(a[j][k]=='0')c0++,index0.push_back(a[j]);
            else c1++,index1.push_back(a[j]);
        }
        if(c1>=c0){
            index0.clear();
            return oxygen(index1,k+1);
        }
        else{
            index1.clear();
            return oxygen(index0,k+1);
        }
    }
}
vector<string> co2(vector<string> a, int k)
{
    if(a.size()==1)return a;
    else
    {
        int c0=0,c1=0;
        vector<string> index0,index1;
        for(int j=0;j<a.size();j++){
            if(a[j][k]=='0')c0++,index0.push_back(a[j]);
            else c1++,index1.push_back(a[j]);
        }
        if(c1>=c0){
            index1.clear();
            return co2(index0,k+1);
        }
        else{
            index0.clear();
            return co2(index1,k+1);
        }
    }
}
int main() {
    // your code goes here
    freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout);
    string s;
    vector<string> a;
    while(getline(cin,s)){
        a.push_back(s);
    }
    int o=stoi(oxygen(a,0)[0],nullptr,2);
    int c=stoi(co2(a,0)[0],nullptr,2);
    cout<<"o="<<o<<" c="<<c<<'\n';
    cout<<(o*c);
}
