function out=ssarea(k,n,deb,fin);

tol=1e-10;

%deb=7e-16
%fin=inf

% nb=10000;
% 
% x=log(deb):abs(log(fin)-log(deb))/nb:log(fin);
% x=exp(x);

% d2=quadgk(@(d)weibulld2(d,k,n),deb,fin,'Waypoints',x)
% d3=quadgk(@(d)weibulld3(d,k,n),deb,fin,'Waypoints',x)
d2=quadgk(@(d)weibulld2(d,k,n),deb,fin,'MaxIntervalCount',2000000)
d3=quadgk(@(d)weibulld3(d,k,n),deb,fin,'MaxIntervalCount',2000000)
% d2=quadl(@(d)weibulld2(d,k,n),deb,fin)
% d3=quadl(@(d)weibulld3(d,k,n),deb,fin)
So=6*d2/d3/2710/1000