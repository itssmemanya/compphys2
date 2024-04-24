#include <stdio.h>
#include <math.h>
// y.=y-t^2+1
float f(float t, float y) {return y-pow(t,2)+1;}
 //y = (t + 1)^2 − 0.5e^t
float func(float t) {return (pow((t+1),2)-0.5*exp(t));}
float error_bound(float h, float x, float a) 
{
    float M = 2;  
    float L = 1;  // Lipschitz constant
    return (h*M/(2*L)) * (exp(M*(x-a)/L)-1);
}
void euler_method(float a, float b, float y0, float h ) 
{
    float x = a,y = y0;
    float yf = func(x);
    float err = fabs(yf-y);
    float errb=error_bound(h,x,a);
    printf("t = %.2f, y = %.2f, y(t) = %.2f, error = %.2f, bound error = %.2f\n", x, y, yf,err,errb);
    while (x < b) 
    {
        y += h * f(x, y);
        x += h;
        yf = func(x);
        err = yf-y;
        errb=error_bound(h,x,a);
        printf("t = %.2f, y = %.2f, y(t) = %.2f, error = %.2f, bound error = %.2f\n", x, y, yf,err,errb);
    }
}

int main() 
{
    float a=0, b=2, y0=0.5, h=0.2;
    euler_method(a,b,y0,h);
    return 0;
}
