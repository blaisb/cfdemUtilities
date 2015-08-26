global fich;
v=1;
idrive=0;
while v==1,
    if idrive == 0,
        clear str;
        d = dir;
        str = {d.name};
        if char(str(:,1)) == '.',
            j=0;
        else
            j=2;
            str(1)={'.'};
            str(2)={'...'};
        end
    else
        idrive =0;
    end
    [s,v] = listdlg('PromptString','Select a data file:',...
        'Name','Load',...
        'SelectionMode','single',...
        'ListString',str);
    file=char(str(:,s));
    if v == 0,
    else
        switch file
            case '...',
                drive ={'a:','b:','c:','d:','e:','f:','g:','h:','i:','j:','k:','l:','m:','n:','o:','p:','q:','r:','s:'};
                rep=pwd;
                l=0;
                clear str;
                for i=1:1:size(drive,2),
                    try
                        cd(char(drive(:,i)));
                        l=l+1;
                        str(l)=drive(i);
                        idrive=1;
                    catch
                        sprintf('%s%d',lasterr,'1');
                    end
                end
                cd(rep);
            case '..',
                cd('..');
            case '.',
                % rien
            otherwise,
                try
                    cd(file);
                catch
                    sprintf('%s%d',lasterr,'2')
                    try
                        global fich;
                        global fig1;
                        global axehdl;
                        fich=load(file);
                        x=sort(fich(:,1));
                        y=sort(fich(:,2));
                        hold on;
                        figure(fig1);
                        axes(axehdl);
                        plot(x,y,'r+')
                        k=get(findobj(gcf,'Tag','EditText1'),'Value');
                        n=get(findobj(gcf,'Tag','EditText2'),'Value');
                        Value=get(findobj(gcf,'Tag','PopupMenu1'),'Value');
                        deb=get(findobj(gcf,'Tag','EditText3'),'Value');
                        fin=get(findobj(gcf,'Tag','EditText4'),'Value');
                        inter=get(findobj(gcf,'Tag','EditText5'),'Value');
                        Vlog=get(findobj(gcf,'Tag','Checkbox1'),'Value');
                        Vgrid=get(findobj(gcf,'Tag','Checkbox2'),'Value');
                        if Vlog ==1,
                            semilogx(x,y,'Parent',axehdl);
                        else,
                            plot(x,y,'Parent',axehdl);
                        end,
                        if Value == 1,
                            y2=(x.^n/k^n)*100;
                        elseif Value == 2,
                            y2=(1-(1-x/k).^n)*100;
                        elseif Value == 3,
                            y2=erf(log(x./k)/n)*100;
                        elseif Value == 4,
                            y2=(1-exp(-(x.^n/k^n)))*100;
                        elseif Value == 5,
                            y2=1/2*(1+erf(log(x/k)/(sqrt(2)*log(n))))*100;
                        end
                        erreur=(y-y2).^2;
                        somerr=sum(erreur);
                        set(findobj(gcf,'Tag','EditText6'),'String',somerr);
                        Vspline=get(findobj(gcf,'Tag','Checkbox3'),'Value')
                        if Vspline==1,
                            xx=deb:inter:fin;
                            yy=interp1(x,y,xx,'cubic');
                            plot(xx,yy,'r-')
                        end
                        if Vgrid ==1,
                            grid on;
                        else,

                            grid off;
                        end,
                    catch
                        sprintf('%s%d',lasterr,'3')
                        errordlg('Bad format. Can not load this file!', 'Loading Error');
                    end
                    v=0;
                end
        end
    end
end
