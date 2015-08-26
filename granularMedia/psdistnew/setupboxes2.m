nbps=get(findobj(gcf,'Tag','EditText1'),'String');

for i = 1:str2num(nbps),
    VBox1 = strcat('EditText', num2str(i+4));
    set(findobj(gcf,'Tag',VBox1),'Enable','on');
    set(findobj(gcf,'Tag',VBox1),'String','');
    VBox2 = strcat('EditText', num2str(i+49));
    set(findobj(gcf,'Tag',VBox2),'Enable','on');
    set(findobj(gcf,'Tag',VBox2),'String','');
end

Vshape=get(findobj(gcf,'Tag','PopupMenu2'),'Value');

if Vshape==1
    Vparam=1;
elseif Vshape==2|Vshape==3
    Vparam=get(findobj(gcf,'Tag','PopupMenu3'),'Value');
end

if Vparam==1
    header=strvcat('Aspect','ratio');
    if Vshape==1
        param=1;
    elseif Vshape==2
        param=10;
    elseif Vshape==3
        param=4;
    end
elseif Vparam==2
    header=strvcat('Thickness','(µm)');
    param=0.1;
end

set(findobj(gcf,'Tag','StaticText56'),'String',header);

if and((str2num(nbps) <= 45),(str2num(nbps) >= 3)),
    for i = 1:str2num(nbps),
        VBox = strcat('StaticText', num2str(i+5));
        set(findobj(gcf,'Tag',VBox),'String',i);
    end
    
    for i=5:4+str2num(nbps),
        VBox = strcat('EditText', num2str(i));
        set(findobj(gcf,'Tag',VBox),'Visible','on');
        set(findobj(gcf,'Tag',VBox),'String','');
    end
    
    for i=(5+str2num(nbps)):49,
        VBox = strcat('EditText', num2str(i));
        set(findobj(gcf,'Tag',VBox),'Visible','off');
    end
    
    for i=50:49+str2num(nbps),
        VBox = strcat('EditText', num2str(i));
        set(findobj(gcf,'Tag',VBox),'Visible','on');
        set(findobj(gcf,'Tag',VBox),'String','');
    end
    
    for i=(50+str2num(nbps)):94,
        VBox = strcat('EditText', num2str(i));
        set(findobj(gcf,'Tag',VBox),'Visible','off');
    end
    
    for i=95:94+str2num(nbps),
        VBox = strcat('EditText', num2str(i));
        set(findobj(gcf,'Tag',VBox),'Visible','on');
        set(findobj(gcf,'Tag',VBox),'String',param);
    end
    
    for i=(95+str2num(nbps)):139,
        VBox = strcat('EditText', num2str(i));
        set(findobj(gcf,'Tag',VBox),'Visible','off');
    end
    
    for i=6:5+str2num(nbps),
        VBox = strcat('StaticText', num2str(i));
        set(findobj(gcf,'Tag',VBox),'Visible','on');
    end
    
    for i=(6+str2num(nbps)):50,
        VBox = strcat('StaticText', num2str(i));
        set(findobj(gcf,'Tag',VBox),'Visible','off');
    end
    
    set(findobj(gcf,'Tag','EditText50'),'BackgroundColor',[1 0 0]);
    set(findobj(gcf,'Tag','EditText5'),'BackgroundColor',[0 1 0]);
    set(findobj(gcf,'Tag','EditText5'),'Enable','off');
    set(findobj(gcf,'Tag','EditText6'),'BackgroundColor',[0 1 0]);
    set(findobj(gcf,'Tag','EditText6'),'Enable','off');
    if nbps == '3',
        dc = 0;
    else
        dc = 0.44/(str2num(nbps)-3);
    end
    for i = 7:(str2num(nbps)+3),
        VBox = strcat('EditText',num2str(i));
        set(findobj(gcf,'Tag',VBox),'BackgroundColor',[0 1 0]);
        set(findobj(gcf,'Tag',VBox),'Enable','off');
    end
    
    for i = 51:(str2num(nbps)+48),
        VBox = strcat('EditText',num2str(i));
        set(findobj(gcf,'Tag',VBox),'BackgroundColor',[0 1 0]);
        set(findobj(gcf,'Tag',VBox),'Enable','off');
    end
    
   for i = 95:(str2num(nbps)+94),
      VBox = strcat('EditText',num2str(i));
      set(findobj(gcf,'Tag',VBox),'BackgroundColor',[1 (1-(i-95)*dc) 0.5]);
      set(findobj(gcf,'Tag',VBox),'Enable','on');
   end
    
    VBox = strcat('EditText', num2str(str2num(nbps)+4));
    set(findobj(gcf,'Tag',VBox),'BackgroundColor',[1 0 0]);
    set(findobj(gcf,'Tag',VBox),'String','1');
    
    VBox = strcat('EditText', num2str(str2num(nbps)+49));
    set(findobj(gcf,'Tag',VBox),'BackgroundColor',[1 0 0]);
    
else
    errordlg('The number of particle size must be between 3 and 45!', 'Number of Particle Size');
end
