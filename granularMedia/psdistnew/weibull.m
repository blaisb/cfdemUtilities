function [So] = weibull(k,n,density)

meanw=k*gamma(1+1/n)

stdevw=sqrt(k^2*gamma(1+2/n)-meanw^2)

So=stdevw^3/(gamma(1+3/n)*k^3-3*meanw*stdevw^2-meanw^3)/stdevw^2