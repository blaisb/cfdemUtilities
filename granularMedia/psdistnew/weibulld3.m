function y = weibulld3(d,k,n)

d33=d;

y=((n/k)*d.^(n-1)*(1/k)^(n-1).*exp(-(d.^(n)*(1/k)^n)));