function loadaspect()
global aspectfile
try
    Vshape=get(findobj(gcf,'Tag','PopupMenu2'),'Value');
    %Vshape=1 -->sphere
    %Vshape=2 -->plate
    %Vshape=3 -->acicular
    %data=DLMREAD(aspectfile,' ',0,0);
    data=load(aspectfile);
    Nbins=size(data,1);
    a(:,1)=data(:,1);
    phi(:,1)=data(:,2);
    for i=1:Nbins
        if Vshape==1
            esd(i,1)=a(i,1);
        elseif Vshape==2
            esd(i,1)=((a(i,1))/phi(i,1)^(1/3));
        else %if Vshape==3
            esd(i,1)=a(i,1)/phi(i,1)^(2/3);
        end
    end
    
    figure(2);
    Nsizes=str2num(get(findobj(gcf,'Tag','EditText1'),'String'));

    for i = 1:Nsizes,
        VBox3 = strcat('EditText', num2str(i+49));
        siz=str2num(get(findobj(gcf,'Tag',VBox3),'String'));
        if siz>max(esd(:,1))
            pos=find(esd(:,1)==max(esd(:,1)));
            aspect=phi(pos);
        elseif siz<min(esd(:,1))
            pos=find(esd(:,1)==min(esd(:,1)));
            aspect=phi(pos);
        else
            aspect=spline(esd(:,1),phi,siz);
        end
        VBox2 = strcat('EditText', num2str(i+94));
        set(findobj(gcf,'Tag',VBox2),'String',num2str(aspect));
    end


catch
    display(lasterr)
    errorstr=sprintf('Unable to load discretization. \n',lasterr)
    errordlg(errorstr,'Loading error','warning')
end
