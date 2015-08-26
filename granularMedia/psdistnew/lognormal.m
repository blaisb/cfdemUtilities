function out=lognormal(xmoy,stdv);

xmed=.1;
xmedold=0;
diff=((xmed-xmedold)/xmed*100);
dx=.1;

while abs(diff) > 0.00000001,
    xmed=xmedold+dx;
    alpha=2*log(xmoy/xmed);
    xmedold=xmed;
    xmed=sqrt(stdv^2/(exp(alpha)*(exp(alpha)-1)));
    diff=((xmedold-xmed)/xmedold*100);

    if (diff < 0 | imag(diff) ~= 0),
        dx=-abs(dx)/2;
    else
        dx=abs(dx);
    end
end

xmed=xmed;
stdvg=exp(sqrt(2*log(xmoy/xmed)));
out=[xmed stdvg];