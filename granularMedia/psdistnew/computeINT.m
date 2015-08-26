global fig1;
global fig2;
global fich;

nbps=get(findobj(gcf,'Tag','EditText1'),'String');

%Verify if all the required data has been entered
Iok =0;
for i = 1:str2num(nbps),
    VBox = strcat('EditText', num2str(i+94));
    VEn=get(findobj(gcf,'Tag',VBox),'Enable');
    VStr=get(findobj(gcf,'Tag',VBox),'String');
    if and((isempty(VStr)==1),(strcmp(VEn,'on') == 1)),
        Iok=1;
    end
end
VBox1 = strcat('EditText', num2str(str2num(nbps)+49));
VBox2 = strcat('EditText', num2str(str2num(nbps)+4));
VBox3 = strcat('EditText', num2str(50));
VStr1=get(findobj(gcf,'Tag',VBox1),'String');
VStr2=get(findobj(gcf,'Tag',VBox2),'String');
VStr3=get(findobj(gcf,'Tag',VBox3),'String');
if (isempty(VStr1)==1)|(isempty(VStr2)==1)|(isempty(VStr3)==1)
    Iok=1;
end

if Iok == 1,
    errordlg('Data Missing! Please fill all colored boxes, except green ones.', 'Compute');
    
    %If all data is there, compute the next diameter for given max diamter and nb of particles
else
    %Get model
    figure(1);
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
    figure(2);
    
    %Get model or data fit choice
    Vmodfit=get(findobj(gcf,'Tag','PopupMenu1'),'Value');
    if Vmodfit == 2,
        Vmod = 6;
    end
    
    %get physical data (density, coatweight, area)
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
    
    %Calculate total mass 
    Mt=area/(1000000)^2*cw/1000;
    VBox=strcat('EditText',num2str(str2num(nbps)+49));
    
    %get max diameter and nb of particles w/ d max
    dmax=str2num(get(findobj(gcf,'Tag',VBox),'String'));
    VBox=strcat('EditText',num2str(str2num(nbps)+4));
    ndmax=str2num(get(findobj(gcf,'Tag',VBox),'String'));
    mmax=rho*4/3*pi*(dmax/(2*1000000))^3;
    
    %get min diameter and nb of particles w/ d min
    d1=str2num(get(findobj(gcf,'Tag','EditText50'),'String'));
    ndmin=str2num(get(findobj(gcf,'Tag','EditText5'),'String'));
    
    
    %Calculate next diameter 
    
    if Vmod == 1,
        fdmax=(dmax^n/k^n);
        X=k*(fdmax-ndmax*mmax/Mt)^(1/n);
        Y=(d1^n/k^n);
    elseif Vmod == 2,
        fdmax=(1-(1-dmax/k)^n);
        X=k*(1-(1-fdmax+ndmax*mmax/Mt)^(1/n));
        Y=(1-(1-d1/k)^n);
    elseif Vmod == 3,
        fdmax=erf(log(dmax/k)/n);
        X=k*exp(n*erfinv(fdmax-ndmax*mmax/Mt));
        Y=erf(log(d1/k)/n); 
    elseif Vmod == 4,
        fdmax=(1-exp(-(dmax^n/k^n)));
        X=(-(k^n)*log(1-fdmax+ndmax*mmax/Mt))^(1/n);
        Y=(1-exp(-(d1^n/k^n)));
    elseif Vmod == 5,
        fdmax=1/2*(1+erf(log(dmax/xg)/(sqrt(2)*log(sg))));
        X=xg*exp(sqrt(2)*log(sg)*erfinv(2*(fdmax-ndmax*mmax/Mt)-1))
        Y=1/2*(1+erf(log(d1/xg)/(sqrt(2)*log(sg))));
    elseif Vmod == 6,
        taille=size(fich,1);
        if taille ~= 0,
            global fich;
            dd=fich(:,1);
            mp=fich(:,2);
            fdmax=spline(dd,mp,dmax);
            X=interp1(mp,dd,fdmax-ndmax*mmax/Mt*100,'cubic');
            Y=interp1(dd,mp,d1,'cubic')/100;
        end
    end
    
    %Enter diameter in proper box
    VBox=strcat('EditText',num2str(str2num(nbps)+48));
    set(findobj(gcf,'Tag',VBox),'String',X);
    m1=rho*4/3*pi*(d1/(2*1000000))^3;
    np=num2str(round(Mt*Y/m1));
    set(findobj(gcf,'Tag','EditText5'),'String',np);
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%
    
    p1=Y;
    down=1;
    ok=0;
    
    
    
    while ok==0
%         fprintf(1,'\n');
%         fprintf(1,'\n');
%         fprintf(1,'*****************************WHILE LOOP********************************\n')
%         fprintf(1,'\n');
        
        %Find last diameter to take into account in interval splitting
        VBoxlast=strcat('EditText',num2str(str2num(nbps)-down+49))
        dlast=str2num(get(findobj(fig2,'Tag',VBoxlast),'String'))
        
        %Calculate mass percentage associated with dlast
        if Vmod == 1,
            plast=(dlast^n/k^n);        
        elseif Vmod == 2,
            plast=(1-(1-dlast/k)^n);    
        elseif Vmod == 3,
            plast=erf(log(dlast/k)/n);     
        elseif Vmod == 4,
            plast=(1-exp(-(dlast^n/k^n)));
        elseif Vmod == 5
            plast=1/2*(1+erf(log(dlast/xg)/(sqrt(2)*log(sg))));
        elseif Vmod == 6,
            taille=size(fich,1);
            if taille ~= 0,
                global fich;
                dd=fich(:,1);
                mp=fich(:,2);
                plast=interp1(dd,mp,dlast,'cubic')/100;              
            end
        end
        for i=1:str2num(nbps)-down-2
%             fprintf(1,'************************LOOP # %d ******************************\n',i)
            int=(plast-p1)/(str2num(nbps)-down-i);
            p2=p1+int;
            
            %Find diameter associated with percentage value p2
            if Vmod == 1,
                d2=k*(p2)^(1/n);
            elseif Vmod == 2,
                d2=k*(1-(1-p2)^(1/n));
            elseif Vmod == 3,
                d2=k*exp(n*erfinv(p2));
            elseif Vmod == 4,
                d2=(-(k^n)*log(1-p2))^(1/n);
            elseif Vmod == 5,
                d2=xg*exp(sqrt(2)*log(sg)*erfinv(2*(p2)-1));
            elseif Vmod == 6,
                taille=size(fich,1);
                if taille ~= 0,
                    global fich;
                    dd=fich(:,1);
                    mp=fich(:,2);
                    d2=interp1(mp,dd,p2*100,'cubic');
                end
            end
            
            %Verifying constraint (d2<=1.75*d1)
            if d2>=1.75*d1
                fprintf(1,'Constraint not satisfied.  Diameter will be recalculated.\n');
                d2=1.75*d1;
                %Calculate the new cumulative percentage of mass occupied by new d2
                if Vmod == 1,
                    p2=(d2^n/k^n);        
                elseif Vmod == 2,
                    p2=(1-(1-d2/k)^n);    
                elseif Vmod == 3,
                    p2=erf(log(d2/k)/n);     
                elseif Vmod == 4,
                    p2=(1-exp(-(d2^n/k^n)));
                elseif Vmod == 5
                    p2=1/2*(1+erf(log(d2/xg)/(sqrt(2)*log(sg))));
                elseif Vmod == 6,
                    taille=size(fich,1);
                    if taille ~= 0,
                        global fich;
                        dd=fich(:,1);
                        mp=fich(:,2);
                        p2=interp1(dd,mp,d2,'cubic')/100;               
                    end
                end
            end
            
            %Calculate number of particles:
            m=4/3*pi*(d2/(2*1000000))^3*rho;
            nb=round((p2-p1)*Mt/m);
            
            %Write data in boxes
            VBox1=strcat('EditText',num2str(i+5));
            VBox2=strcat('EditText',num2str(i+50));
            set(findobj(gcf,'Tag',VBox1),'String',nb);
            set(findobj(gcf,'Tag',VBox2),'String',d2);
            
            %Assign new variables:
            p1=p2;
            d1=d2;
        end
        %Calculate nb of particles associated with last interval
            if Vmod == 1,
                plast=(dlast^n/k^n);        
            elseif Vmod == 2,
                plast=(1-(1-dlast/k)^n);    
            elseif Vmod == 3,
                plast=erf(log(dlast/k)/n);     
            elseif Vmod == 4,
                plast=(1-exp(-(dlast^n/k^n)));
            elseif Vmod == 5,
                plast=1/2*(1+erf(log(dlast/xg)/(sqrt(2)*log(sg))));
            elseif Vmod == 6,
                taille=size(fich,1);
                if taille ~= 0,
                    global fich;
                    dd=fich(:,1);
                    mp=fich(:,2);
                    plast=interp1(dd,mp,dlast,'cubic')/100;               
                end
            end
            m=4/3*pi*(dlast/2/1000000)^3*rho;
            nb=round((plast-p2)*Mt/m);
            VBox1=strcat('EditText',num2str(i+6));
            set(findobj(gcf,'Tag',VBox1),'String',nb);
            
            if dlast>(1.75*d2)
                errordlg('No enough intervals to satisfy discretization constraints.', 'Warning');
                uiwait
            end
        
        
        if nb<=0
            down=down+1;
            nb=1;
            %Calculate next (last) diameter 
            if Vmod == 1,
                dlast=k*(plast-nb*m/Mt)^(1/n);
            elseif Vmod == 2,
                dlast=k*(1-(1-plast+nb*m/Mt)^(1/n));
            elseif Vmod == 3,
                dlast=k*exp(n*erfinv(plast-nb*m/Mt));
            elseif Vmod == 4,
                dlast=(-(k^n)*log(1-plast+nb*m/Mt))^(1/n);
            elseif Vmod == 5
                dlast=xg*exp(sqrt(2)*log(sg)*erfinv(2*(plast-nb*m/Mt)-1));
            elseif Vmod == 6,
                taille=size(fich,1);
                if taille ~= 0,
                    global fich;
                    dd=fich(:,1);
                    mp=fich(:,2);
                    dlast=interp1(mp,dd,plast-nb*m/Mt*100,'cubic');
                end
            end
            VBox1=strcat('EditBox',num2str(str2num(nbps)-down+51));
            set(findobj(gcf,'Tag',VBox1),'String',dlast);
            VBox2=strcat('EditText',num2str(i+6));
            set(findobj(gcf,'Tag',VBox2),'String',nb);
        else
            ok=1;
        end
    end
        mtot=0;
    clear nn dd mm;
    %calculate total number of particles
    figure(fig2);
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
dd'
end
    

