global fig1;
global fig2;
global fich;

nbps=get(findobj(gcf,'Tag','EditText1'),'String');

Iok =0;
for i = 1:str2num(nbps),
    VBox = strcat('EditText', num2str(i+4));
    VEn=get(findobj(gcf,'Tag',VBox),'Enable');
    VStr=get(findobj(gcf,'Tag',VBox),'String');
    if and((isempty(VStr)==1),(strcmp(VEn,'on') == 1)),
        Iok=1;
    end
    VBox = strcat('EditText', num2str(i+49));
    VEn=get(findobj(gcf,'Tag',VBox),'Enable');
    VStr=get(findobj(gcf,'Tag',VBox),'String');
    if and((isempty(VStr)==1),(strcmp(VEn,'on') == 1)),
        Iok=1;
    end
end

if Iok == 1,
    errordlg('Data Missing! Please fill all colored boxes, except green ones.', 'Compute');
else
    figure(fig1);
    Vmod=get(findobj(gcf,'Tag','PopupMenu1'),'Value');
    k=get(findobj(gcf,'Tag','EditText1'),'Value');
    n=get(findobj(gcf,'Tag','EditText2'),'Value');
    rho=get(findobj(gcf,'Tag','EditText12'),'Value');
    if Vmod==5
        xg=k;
        sg=n;
        xbar=get(findobj(gcf,'Tag','EditText6'),'Value');
        sbar=get(findobj(gcf,'Tag','EditText7'),'Value');
    end
    
    figure(fig2);
    Vmodfit=get(findobj(gcf,'Tag','PopupMenu1'),'Value')
    if Vmodfit == 2,
        Vmod = 6;
    end
    %rho=str2num(get(findobj(gcf,'Tag','EditText2'),'String'));
    cw=str2num(get(findobj(gcf,'Tag','EditText3'),'String'));
    area=str2num(get(findobj(gcf,'Tag','EditText4'),'String'));
%     if isempty(rho) == 1,
%         set(findobj(gcf,'Tag','EditText2'),'String','2000');
%         rho=2000;
%     end
    if isempty(cw) == 1,
        set(findobj(gcf,'Tag','EditText3'),'String','10');
        cw=10;
    end
    if isempty(area) == 1,
        set(findobj(gcf,'Tag','EditText4'),'String','100');
        area=100;
    end
    Mt=area/(1000000)^2*cw/1000;
    VBox=strcat('EditText',num2str(str2num(nbps)+49));
    dmax=str2num(get(findobj(gcf,'Tag',VBox),'String'));
    VBox=strcat('EditText',num2str(str2num(nbps)+4));
    ndmax=str2num(get(findobj(gcf,'Tag',VBox),'String'));
    d1=str2num(get(findobj(gcf,'Tag','EditText50'),'String'));
    mmax=rho*4/3*pi*(dmax/(2*1000000))^3;
    if Vmod == 1,
        fdmax=(dmax^n/k^n);
        x=k*(fdmax-ndmax*mmax/Mt)^(1/n);
        y=(d1^n/k^n);
    elseif Vmod == 2,
        fdmax=(1-(1-dmax/k)^n);
        x=k*(1-(1-fdmax+ndmax*mmax/Mt)^(1/n));
        y=(1-(1-d1/k)^n);
    elseif Vmod == 3,
        fdmax=erf(log(dmax/k)/n);
        x=k*exp(n*erfinv(fdmax-ndmax*mmax/Mt));
        y=erf(log(d1/k)/n); 
    elseif Vmod == 4,
        fdmax=(1-exp(-(dmax^n/k^n)));
        x=(-(k^n)*log(1-fdmax+ndmax*mmax/Mt))^(1/n);
        y=(1-exp(-(d1^n/k^n)));
    elseif Vmod == 5
        fdmax=1/2*(1+erf(log(dmax/xg)/(sqrt(2)*log(sg))));
        x=xg*exp(sqrt(2)*log(sg)*erfinv(2*(fdmax-ndmax*mmax/Mt)-1));
        y=1/2*(1+erf(log(d1/xg)/(sqrt(2)*log(sg))));
    elseif Vmod == 6,
        taille=size(fich,1);
        if taille ~= 0,
            dd=fich(:,1);
            mp=fich(:,2);
            fdmax=spline(dd,[0;mp;0],dmax);
            x=interp1(mp,dd,fdmax-ndmax*mmax/Mt*100,'cubic');
            y=interp1(dd,mp,d1,'cubic')/100;
        end
    end
    VBox=strcat('EditText',num2str(str2num(nbps)+48));
    set(findobj(gcf,'Tag',VBox),'String',x);
    m1=rho*4/3*pi*(d1/(2*1000000))^3;
    np=num2str(round(Mt*y/m1));
    set(findobj(gcf,'Tag','EditText5'),'String',np);
    for i=(str2num(nbps)-3):-1:0
        VBox = strcat('EditText', num2str(i+50));
        VStr=get(findobj(gcf,'Tag',VBox),'String');
        VCol=get(findobj(gcf,'Tag',VBox),'BackgroundColor');
        if VCol== [0 1 0],
            VBox2=strcat('EditText',num2str(i+6));
            nD=str2num(get(findobj(gcf,'Tag',VBox2),'String'));
            VBox3 = strcat('EditText', num2str(i+51));
            D=str2num(get(findobj(gcf,'Tag',VBox3),'String'));
            m=rho*4/3*pi*(D/(2*1000000))^3;
            if Vmod == 1,
                fD=(D^n/k^n);
                x=k*(fD-nD*m/Mt)^(1/n);
            elseif Vmod == 2,
                fD=(1-(1-D/k)^n);
                x=k*(1-(1-fD+nD*m/Mt)^(1/n));
            elseif Vmod == 3,
                fD=erf(log(D/k)/n);
                x=k*exp(n*erfinv(fD-nD*m/Mt));
            elseif Vmod == 4,
                fD=(1-exp(-(D^n/k^n)));
                x=(-(k^n)*log(1-fD+nD*m/Mt))^(1/n);
            elseif Vmod == 5
                fD=1/2*(1+erf(log(D/xg)/(sqrt(2)*log(sg))));
                x=xg*exp(sqrt(2)*log(sg)*erfinv(2*(fD-nD*m/Mt)-1));
            elseif Vmod == 6,
                taille=size(fich,1);
                if taille ~= 0,
                    dd=fich(:,1);
                    mp=fich(:,2);
                    fD=interp1(dd,mp,D,'cubic')/100;
                    x=spline(mp,dd,(fD-nD*m/Mt)*100,'cubic');
                end
            end
            VBox4=strcat('EditText',num2str(i+50));
            set(findobj(gcf,'Tag',VBox4),'String',x);
        else
            d=str2num(VStr);
            VBox2 = strcat('EditText', num2str(i+51));
            D=str2num(get(findobj(gcf,'Tag',VBox2),'String'));
            Mt=area/(1000000)^2*cw/1000;
            m=rho*4/3*pi*(D/(2*1000000))^3;
            if Vmod == 1,
                fd=(d^n/k^n);
                fD=(D^n/k^n);
            elseif Vmod == 2,
                fd=(1-(1-d/k)^n);
                fD=(1-(1-D/k)^n);
            elseif Vmod == 3,
                fd=erf(log(d/k)/n);
                fD=erf(log(D/k)/n);
            elseif Vmod == 4,
                fd=(1-exp(-(d^n/k^n)));
                fD=(1-exp(-(D^n/k^n)));
            elseif Vmod == 5
                fd=1/2*(1+erf(log(d/xg)/(sqrt(2)*log(sg))));
                fD=1/2*(1+erf(log(D/xg)/(sqrt(2)*log(sg))));
            elseif Vmod == 6,
                taille=size(fich,1);
                if taille ~= 0,
                    dd=fich(:,1);
                    mp=fich(:,2);
                    fD=interp1(dd,mp,D,'cubic')/100;
                    fd=interp1(dd,mp,d,'cubic')/100;
                end
            end
            x=num2str(round((fD-fd)*Mt/m));
            VBox3=strcat('EditText',num2str(i+6));
            set(findobj(gcf,'Tag',VBox3),'String',x);
        end
    end
    mtot=0;
    clear nn dd mm;
    for i = 1:str2num(nbps),
        VBox = strcat('EditText', num2str(i+4));
        nn(i)=str2num(get(findobj(gcf,'Tag',VBox),'String'));
        VBox = strcat('EditText', num2str(i+49));
        dd(i)=str2num(get(findobj(gcf,'Tag',VBox),'String'));
        mm(i)=nn(i)*rho*4/3*pi*(dd(i)/(2*1000000))^3;
        mtot=mtot+mm(i);
    end
    set(findobj(gcf,'Tag','EditText140'),'String',num2str(sum(nn,2)));
    cwcal=mtot/area*(1000000)^2*1000;
    set(findobj(gcf,'Tag','EditText141'),'String',num2str(cwcal));
    
end

