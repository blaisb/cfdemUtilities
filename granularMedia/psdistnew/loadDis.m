global filename;

try
    info= DLMREAD(filename,' ',[0 0 0 4]);
    rho=info(3);
    nbtot=info(2);
    data=DLMREAD(filename,' ',1,0);
    nbps=size(data,1)-1;
    shape=data(:,1);
    nbpar=data(:,2);
    a=data(:,3);
    b=data(:,4);
    c=data(:,5);
    
    if a(1,1)==b(1,1)
        if b(1,1)==c(1,1)
            Vshape=1;
        else
            Vshape=2;
        end
    elseif a(1,1)==c(1,1)&a(1,1)~=b(1,1)
        Vshape=3;
    end
    
    
    
    figure(2);
    area=str2num(get(findobj(gcf,'Tag','EditText4'),'String'));
    set(findobj(gcf,'Tag','EditText1'),'String',num2str(nbps));
    set(findobj(gcf,'Tag','PopupMenu2'),'Value',Vshape);
    Vparam=get(findobj(gcf,'Tag','PopupMenu3'),'Value');
    Vvis=get(findobj(gcf,'Tag','PopupMenu3'),'Visible');
    
    set(findobj(gcf,'Tag','checkbox2'),'Value',info(4));
    if info(4)==0
        set(findobj(gcf,'Tag','StaticText59'),'Visible','off');
        set(findobj(gcf,'Tag','EditText142'),'Visible','off');
        set(findobj(gcf,'Tag','EditText142'),'String','0');
    else
        set(findobj(gcf,'Tag','StaticText59'),'Visible','on');
        set(findobj(gcf,'Tag','EditText142'),'Visible','on');
        set(findobj(gcf,'Tag','EditText142'),'String',num2str(info(5)));
    end   
    
    if (strcmp(Vvis,'on')~=1)&(Vshape==2|Vshape==3)
        set(findobj(gcf,'Tag','PopupMenu3'),'Visible','on');
        set(findobj(gcf,'Tag','StaticText57'),'Visible','on');
        set(findobj(gcf,'Tag','PopupMenu3'),'Value',1);
    else
        Vparam=get(findobj(gcf,'Tag','PopupMenu3'),'Value');
    end
    
    set(findobj(gcf,'Tag','checkbox1'),'Value',0);
    setupboxes
    for i = 1:str2num(nbps)-1,
        Veq=4/3*pi*a(i,1)*b(i,1)*c(i,1);
        diam=2*(a(i,1)*b(i,1)*c(i,1))^(1/3)*1000000;%(Veq*3/(4*pi))^(1/3)*2*1000000;
        VBox1 = strcat('EditText', num2str(i+4));
        set(findobj(gcf,'Tag',VBox1),'String',num2str(nbpar(i,1)));
        VBox2 = strcat('EditText', num2str(i+49));
        set(findobj(gcf,'Tag',VBox2),'String',num2str(diam));
        VBox3 = strcat('EditText', num2str(i+94));
        if Vshape==1
            set(findobj(gcf,'Tag',VBox3),'String',num2str(1));
        elseif Vshape==2|Vshape==3
            if Vparam==1
                set(findobj(gcf,'Tag',VBox3),'String',num2str(a(i)/c(i)));
            elseif Vparam==2
                set(findobj(gcf,'Tag',VBox3),'String',num2str(c(i)*1e006*2));
            end
        end
        %         if or(i== 2, i==str2num(nbps-1)),
        %                 set(findobj(gcf,'Tag',VBox2),'BackgroundColor',[0 1 0]);
        %                 set(findobj(gcf,'Tag',VBox2),'Enable','off');
        %         else,
        %             if Vcol(i) == 1,
        %                 set(findobj(gcf,'Tag',VBox2),'BackgroundColor',[0 1 0]);
        %                 set(findobj(gcf,'Tag',VBox2),'Enable','off');
        %             else,
        %                 VBox1 = strcat('EditText', num2str(i+5));
        %                 set(findobj(gcf,'Tag',VBox1),'BackgroundColor',[0 1 0]);
        %                 set(findobj(gcf,'Tag',VBox1),'Enable','off');
        %             end,
        %         end,
    end,
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
catch
    display(lasterr)
    errorstr=sprintf('Unable to load discretization. \n',lasterr)
    errordlg(errorstr,'Loading error','warning')
end
