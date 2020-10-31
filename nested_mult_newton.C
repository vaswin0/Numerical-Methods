#include<stdio.h>

/* Nested multiplication
 * for newton form of a polynomial*/


double nested_mult(float coeff[], int degree, float  z ,float cent[]){
		 
		 double b = coeff[degree];

		 for(int i = degree-1 ; i >= 0; --i){
		 		
           printf("%f \n",b);
			  b += coeff[i] + (z - cent[i+1])*b;


			  }

		return b ;// + coeff[0];
		

	}



int main() {

 	int degree = 2 ;

	float coeff [degree + 1] = {1.57078,0.0006,0.00012};

	float cent[] = {0,1,1,4};

	printf("%f",nested_mult(coeff,degree,0,cent));

	}

	



