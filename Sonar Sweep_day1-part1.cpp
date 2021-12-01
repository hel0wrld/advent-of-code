#include <iostream>
using namespace std;

int main() {
	int a[200000000];
	int x=0,k=0,count=0;
	while(scanf("%d",&x)!=EOF){
		a[k]=x;
		k++;
	}
	for(int i=1;i<k;i++){
		if(a[i]>a[i-1])count++;
	}
	cout<<count;
}
