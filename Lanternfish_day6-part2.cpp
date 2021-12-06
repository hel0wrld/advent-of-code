#include<bits/stdc++.h>
#define f(i,n)          for(int i=0;i<n;i++)
#define lli             long long int
#define pb              push_back
using namespace std;
vector<lli> shift(vector<lli> a)    //shifts the elements 1 unit left
{
    vector<lli> b(9,0);
    for(lli i=1;i<9;i++){
        b[i-1]=a[i];
    }
    b[8]=a[0];
    return b;
}
int main()
{
    //IO from txt
    freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout);
    ////////\\\\\\\\\////////\\\\\\\\\////////\\\\\\\\\//
    int N=1;
    //cin>>N;
    while(N--)
    {
        string s;cin>>s;
        vector<lli> a(9,0);     //stores number of occurrences of 0,1,2...7,8 instead of the array itself
        for(auto x:s){
            if(isdigit(x))a[(x-'0')]++;
        }
        int days=256;
        while(days>0){
            lli num_6=a[0];
            a=shift(a);
            a[6]+=num_6;
            days--;
        }
        lli sum=0;
        for(lli i=0;i<9;i++)sum+=a[i];
        cout<<sum;
    }
}
