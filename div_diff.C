#include<stdio.h>
#include<math.h>
const int num_points = 3;

const double fx[num_points] = {1.5709,1.5727,1.5751};
const double x[num_points] = {1,4,6};
double dd, ddd;
double div_diff(int m,int n){
	  

	  

	  if ( abs(m-n) == 1 ) {

	  		
	  		 dd =   ( (fx[m] - fx[n])/(x[m] -x[n]) );

			printf("m=%d\tn=%d\t%f\n",m,n, dd);

			return dd;

			}
	 else {
	 
		double term1 = div_diff(m+1,n);
		double term2 = div_diff(m, n-1);

		ddd =  (term1 - term2)/ (x[n] - x[m]);

		printf("m = %d\t n = %d\t %f\n",m, n,ddd);

		return ddd;

	 }


	 }


int main() {



	 double pol = 0;
    double prod ;
    double z = 3.5;
	int i,j;

	for(i=1;i<num_points;i++) {
      
		prod = 1;
		for(j=0;j<i;j++) {
		   
			prod = prod * (z-x[j]);
		
		}

		pol += prod*div_diff(0,i);
	  
	
	
	}
printf("%f",pol+fx[0]);








	 }
