function y = lognormald2(d,k,n)

%k=mu
%n=sigma

%distribution volumique divisee par pi/6*d^3

%y=((n/k)*d.^(n-1)*(1/k)^(n-1).*exp(-(d.^(n)*(1/k)^n)))./d;
y=1./(d*log(n)*sqrt(2*pi)).*exp(-((log(d/k)).^2/(2*(log(n))^2)))./d;