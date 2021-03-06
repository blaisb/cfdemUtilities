clear all;
hold on;
deb=1e-15;
fin=inf

nb=100;
% k=0.671e-6;
% n=2.12;
% k=2.2e-6
% n=1.16
k=0.715e-6
n=1.06

ifin=1e-6;

ideb=log(deb):abs(log(ifin)-log(deb))/nb:log(ifin);
ideb=exp(ideb)
 
for i=1:nb+1,
%         d2=quadgk(@(d)lognormald2(d,k,n),ideb(i),fin,'MaxIntervalCount',20000);
%         d3=quadgk(@(d)lognormald3(d,k,n),ideb(i),fin,'MaxIntervalCount',20000);
    d2=quadgk(@(d)weibulld2(d,k,n),ideb(i),fin,'MaxIntervalCount',20000);
    d3=quadgk(@(d)weibulld3(d,k,n),ideb(i),fin,'MaxIntervalCount',20000);
    So(i)=6*d2/d3/2710/1000;
end

size(ideb)
size(So)

semilogx(ideb,So)
udeb=ideb' 
%ideb=((1-exp(-(ideb/k).^n))*100)'
ideb=(50*(1+erf(log(ideb/k)/(sqrt(2)*log(n)))))'
So=So'