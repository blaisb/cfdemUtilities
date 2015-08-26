function [So]=ssarea(dis);

tol=1e-10;

deb=1e-11
fin=5e-5
nb=50;
kdeb=.01e-6;
kfin=10e-6;
ndeb=1.01;
nfin=10;

% nb=10000;
% 
 kk=log(kdeb):abs(log(kfin)-log(kdeb))/nb:log(kfin);
 kk=exp(kk)
 
 nn=log(ndeb):abs(log(nfin)-log(ndeb))/nb:log(nfin);
 nn=exp(nn)

% d2=quadgk(@(d)weibulld2(d,k,n),deb,fin,'Waypoints',x)
% d3=quadgk(@(d)weibulld3(d,k,n),deb,fin,'Waypoints',x)
for i=1:nb+1,
    for j=1:nb+1,
        k=kk(i);
        n=nn(j);
        switch dis;
            case 1
                d2=quadgk(@(d)weibulld2(d,k,n),deb,fin,'MaxIntervalCount',2000000);
                d3=quadgk(@(d)weibulld3(d,k,n),deb,fin,'MaxIntervalCount',2000000);
            case 2
                d2=quadgk(@(d)lognormald2(d,k,n),deb,fin,'MaxIntervalCount',2000000);
                d3=quadgk(@(d)lognormald3(d,k,n),deb,fin,'MaxIntervalCount',2000000);
        end
        % d2=quadl(@(d)weibulld2(d,k,n),deb,fin)
        % d3=quadl(@(d)weibulld3(d,k,n),deb,fin)
        So(j,i)=6*d2/d3/2710/1000;
    end
end
% size(So)
% length(nn)
% length(kk)
surf(kk,nn,So)
set(gca,'XScale','log','YScale','log','ZScale','linear')
shading interp
axis tight
axis square
xlabel('k')
ylabel('n')
zlabel('So')