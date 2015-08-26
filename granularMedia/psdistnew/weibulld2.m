function y = weibulld2(d,k,n)


n=n;
k=k;
d22=d;

%distribution volumique divisee par pi/6*d^3

y=((n/k)*d.^(n-1)*(1/k)^(n-1).*exp(-(d.^(n)*(1/k)^n)))./d;