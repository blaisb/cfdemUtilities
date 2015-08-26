global fig1;
global fig2;
global fich;

figure(fig1);
Vmod=get(findobj(gcf,'Tag','PopupMenu1'),'Value');
k=get(findobj(gcf,'Tag','EditText1'),'Value');
n=get(findobj(gcf,'Tag','EditText2'),'Value');
figure(fig2);
Vmodfit=get(findobj(gcf,'Tag','PopupMenu1'),'Value');
if Vmodfit == 2,
   Vmod = 6;
end
if Vmod==5
    xg=k;
    sg=n;
    xbar=get(findobj(gcf,'Tag','EditText6'),'Value');
    sbar=get(findobj(gcf,'Tag','EditText7'),'Value');
end
VBox=strcat('EditText',num2str(str2num(nbobj)-45));
ndmax=str2num(get(findobj(gcf,'Tag',VBox),'String'));
if isempty(ndmax) == 1,
  ndmax=1;
  set(findobj(gcf,'Tag',VBox),'String','1');
end
dmax=str2num(get(gco,'String'));
rho=str2num(get(findobj(gcf,'Tag','EditText2'),'String'));
cw=str2num(get(findobj(gcf,'Tag','EditText3'),'String'));
area=str2num(get(findobj(gcf,'Tag','EditText4'),'String'));
if isempty(rho) == 1,
  set(findobj(gcf,'Tag','EditText2'),'String','2000');
  rho=2000;
end
if isempty(cw) == 1,
  set(findobj(gcf,'Tag','EditText3'),'String','10');
  cw=10;
end
if isempty(area) == 1,
  set(findobj(gcf,'Tag','EditText4'),'String','100');
  area=100;
end

Mt=area/(1000000)^2*cw/1000;
m=rho*4/3*pi*(dmax/(2*1000000))^3;
if Vmod == 1,
   fdmax=(dmax^n/k^n);
   X=k*(fdmax-ndmax*m/Mt)^(1/n);
elseif Vmod == 2,
   fdmax=(1-(1-dmax/k)^n);
   X=k*(1-(1-fdmax+ndmax*m/Mt)^(1/n));
elseif Vmod == 3,
   fdmax=erf(log(dmax/k)/n);
   X=k*exp(n*erfinv(fdmax-ndmax*m/Mt));
elseif Vmod == 4,
   fdmax=(1-exp(-(dmax^n/k^n)));
   X=(-(k^n)*log(1-fdmax+ndmax*m/Mt))^(1/n);
elseif Vmod == 5
    fdmax=1/2*(1+erf(log(dmax/xg)/(sqrt(2)*log(sg))));
    X=xg*exp(sqrt(2)*log(sg)*erfinv(2*(fdmax-ndmax*m/Mt)-1));
elseif Vmod == 6,
    global fich;
   taille=size(fich,1);
   if taille ~= 0,
      dd=fich(:,1);
      mp=fich(:,2);
      fdmax=interp1(dd, mp,dmax,'cubic')/100;
      X=interp1(mp, dd,(fdmax-ndmax*m/Mt)*100,'cubic');
   end
   
end
VBox=strcat('EditText',num2str(str2num(nbobj)-1));
set(findobj(gcf,'Tag',VBox),'String',X);