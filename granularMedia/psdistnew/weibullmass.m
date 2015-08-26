function y = weibulld2(d,k,n)


n=n
k=k
d22=d;

y=((n/k)*d.^(n-1)*(1/k)^(n-1).*exp(-(d.^(n)*(1/k)^n)));