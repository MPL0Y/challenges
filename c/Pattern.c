#include <stdio.h>
int main(){
	int a,b,c;
	printf("Enter Number of rows\n");
	scanf("%d",&b);
	for(c=1;c<=b;c++){
		for(a=1;a<=c;a++){
			printf("*");
		}
		printf("\n");
	}
}