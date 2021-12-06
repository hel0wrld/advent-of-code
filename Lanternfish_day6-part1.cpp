#include<bits/stdc++.h>
#define f(i,n)          for(int i=0;i<n;i++)
#define lli             long long int
#define pb              push_back
using namespace std;
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
        vector<int> a;
        for(auto x:s){
            if(isdigit(x))a.pb(x-'0');
        }
        f(i,a.size())cout<<a[i];
        int days=80;
        f(i,days){
            //cout<<"day="<<i<<' ';
            f(j,a.size()){
                a[j]--;
                if(a[j]==-1){
                    a[j]=6;
                    a.pb(9);
                }
                //cout<<a[j]<<',';
            }
            //cout<<'\n';
        }
        cout<<"length="<<a.size();
    }
}
