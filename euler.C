#include<stdio.h>
#include<stdlib.h>
#include<math.h>



void plot() {

	/* calling gnuplot using 
	 * a pipe from the program 
	 * to the terminal 
	 */
	
	FILE *pipe = popen("gnuplot -persist \n","w");
	fprintf(pipe,"plot 'euler-soln.dat'  \n");
	fprintf(pipe,"exit\n");
	pclose(pipe);





}

int  main()  {


	FILE *file;
	int i,j, Npoints, n;
	float *x, *y, h, up_lmt = 2.0, low_lmt =-2.0, S;
	Npoints = 50;


	

	x = (float *) malloc((Npoints+2)*sizeof(float)); //memory allocation for arrays
	y =  (float *) malloc((Npoints+2)*sizeof(float));


	n = Npoints;
	h = (up_lmt - low_lmt)/Npoints;

	for (i = 0; i <= Npoints; i++) {
			
			x[i] = low_lmt + i*h;

			}


	y[0] = 1;
	file = fopen("euler-soln.dat", "w");
	fprintf(file, "%f %f\n", x[0], y[0]);


	for (i  = 0; i <= Npoints; i++){
			
			y[i + 1] = y[i] - h*2*y[i];

			fprintf(file, "%f %f\n", x[i+1], y[i+1]);

			}


	fclose(file);

   plot();
	}
	
