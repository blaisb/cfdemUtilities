function [c,ceq]=cwcon(dd)

global fig1 fig2 fich Vmod k n xg sg nbps rho cw area Mt cwcal dmin first nn0 dd0 percent;

for i = 1:str2num(nbps),
    fD=0.;
    m=rho*4/3*pi*(dd(i)/(2*1000000))^3;
    if Vmod == 1,
        fd=(dd(i)^n/k^n);
        if i ~= 1,
            fD=(dd(i-1)^n/k^n);
        end
    elseif Vmod == 2,
        fd=(1-(1-dd(i)/k)^n);
        if i ~= 1,
            fD=(1-(1-dd(i-1)/k)^n);
        end
    elseif Vmod == 3,
        fd=erf(log(dd(i)/k)/n);
        if i ~= 1,
            fD=erf(log(dd(i-1)/k)/n);
        end
    elseif Vmod == 4,
        fd=(1-exp(-(dd(i)^n/k^n)));
        if i ~= 1,                
            fD=(1-exp(-(dd(i-1)^n/k^n)));
        end
    elseif Vmod == 5
        fd=1/2*(1+erf(log(dd(i)/xg)/(sqrt(2)*log(sg))));
        if i ~= 1,
            fD=1/2*(1+erf(log(dd(i-1)/xg)/(sqrt(2)*log(sg))));
        end
        
    elseif Vmod == 6,
        taille=size(fich,1);
        if taille ~= 0,
            d=fich(:,1);
            mp=fich(:,2);
            fd=interp1(d,mp,dd(i),'cubic')/100;
            if i ~= 1,
                fD=interp1(d,mp,dd(i-1),'cubic')/100;    
            end
        end
    end
    nn(i)=(round((fd-fD)*Mt/m));
end

c=dd(1)-dmin;
%c=[c;-dd(1)]
const=1.25;
%percent=45;

if first == 1,
    nn0=nn;
    first=0;
end
  
for i = 2:str2num(nbps),
%    if nn0(i) <= 20,
%        c=[c;1-nn(i)];
%    else
        c=[c;dd(i)-dd(i-1)*const;1-nn(i)];        
%    end
%        c=[c;abs(dd(i)-dd0(i))/dd0(i)*100-percent;1-nn(i)];
%        if i==2,
%        abs(dd(i)-dd0(i))/dd0(i)*100-percent
%    end
%        c=[c;abs(dd(i)-dd0(i))/dd0(i)*100-percent];        
end

%ceq=dd(1)-dd0(1);
%ceq=[ceq;dd(str2num(nbps))-dd0(str2num(nbps))];
ceq=0;