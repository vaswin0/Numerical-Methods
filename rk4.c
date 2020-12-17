#include<stdio.h>
#include<stdlib.h>
#include<math.h>

float func(float x, float y ) {

	return -2*y;


	}



void plot() {
	
	FILE *pipe = popen("gnuplot -persist \n","w");
	fprintf(pipe,"plot 'rungek4.dat'  \n");
	fprintf(pipe,"exit\n");
	pclose(pipe);





}

int  main()  {


	FILE *file;
	int i,j, Npoints, n;
	float *x, *y, h, k1, k2, k3, k4 , up_lmt = 2.0, low_lmt =0.0, S;
	Npoints = 50;


	char fname[20];

	x = (float *) malloc((Npoints+2)*sizeof(float));
	y =  (float *) malloc((Npoints+2)*sizeof(float));


	n = Npoints;
	h = (up_lmt - low_lmt)/Npoints;

	for (i = 0; i <= Npoints; i++) {
			
			x[i] = low_lmt + i*h;

			}


	y[0] = 1;
	file = fopen("rungek4.dat", "w");
	fprintf(file, "%f %f\n", x[0], y[0]);


	for (i  = 0; i <= Npoints; i++){

			k1 = h*func(x[i], y[i]);
			k2 = h*func(x[i] + 0.5*h, y[i] + 0.5*k1);
			k3 = h*func(x[i] + 0.5*h, y[i] + 0.5*k2);
			k4 = h*func(x[i] + h, y[i] + k3);
			
			y[i + 1] = y[i] + 0.1666*(k1 +2*k2 +2*k3 + k4) ;

			fprintf(file, "%f %f\n", x[i+1], y[i+1]);

			}


	fclose(file);

   plot();
	}
	
