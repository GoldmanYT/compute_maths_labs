#include <iostream>
#include <cmath>

using namespace std;

double f0(double x)
{
    return x * x;
}

double f(double x)
{
    return cos(0.8 * x * x + 1) / (1.2 + sin(x + 0.5));
}

double rect_int(double (*func)(double), double a, double b, unsigned n)
{
    double h = (b - a) / n;
    double ans = 0;

    for (unsigned i = 0; i < n; i++)
    {
        double x1 = a + h * i;
        double x2 = a + h * (i + 1);
        double c = (x1 + x2) / 2;

        ans += h * func(c);
    }

    return ans;
}

double sympson_int(double (*func)(double), double a, double b, unsigned n)
{
    n += n % 2;
    double h = (b - a) / n;
    double *y = new double[n + 1];

    for (unsigned i = 0; i <= n; i++)
    {
        *(y + i) = func(a + h * i);
    }

    unsigned m = n / 2;
    double ans = (y[0] + y[2 * m] + 4 * y[1]) * h / 3;

    for (unsigned i = 2; i <= m; i++)
    {
        ans += (4 * y[2 * i - 1] + 2 * y[2 * i - 2]) * h / 3;
    }

    return ans;
}

int main()
{
    cout << rect_int(f, 0.4, 1.4, 20) << endl;
    cout << sympson_int(f, 0.4, 1.4, 20) << endl << endl;
    cout << rect_int(f0, 0, 1, 10) << endl;
    cout << sympson_int(f0, 0, 1, 10) << endl << endl;
    return 0;
}
