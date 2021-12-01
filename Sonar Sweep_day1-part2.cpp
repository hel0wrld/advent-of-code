#include <iostream>
using namespace std;

int main() {
	int a[200000000];
	int x=0,k=0,count=0;
	while(scanf("%d",&x)!=EOF){
		a[k]=x;
		k++;
	}
	for(int i=0;i<k-3;i++){
		if(a[i+1]+a[i+2]+a[i+3]>a[i]+a[i+1]+a[i+2])count++;
	}
	cout<<count;
}
