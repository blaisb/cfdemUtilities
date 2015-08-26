function F = psdfun(x,xdata)

n=x(2);
k=x(1);

Value=get(findobj(gcf,'Tag','PopupMenu1'),'Value');

if Value == 1,
    F=(xdata.^n/k^n)*100;
elseif Value == 2,
    F=(1-(1-xdata/k).^n)*100;
elseif Value == 3,
    F=erf(log(xdata./k)/n)*100;
elseif Value == 4,
    F=(1-exp(-(xdata.^n/k^n)))*100;
elseif Value == 5,
    F=1/2*(1+erf(log(xdata/k)/(sqrt(2)*log(n))))*100;
end,