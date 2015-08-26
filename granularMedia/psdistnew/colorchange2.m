nbps=get(findobj(gcf,'Tag','EditText1'),'String');
VTag=get(gcbo,'Tag');VStr=get(gcbo,'String');
if size(VTag,2) == 9,
    nbobj=VTag(9);
elseif  size(VTag,2) == 10,
    nbobj=strcat(VTag(9),VTag(10));
elseif  size(VTag,2) == 11,
    nbobj=strcat(VTag(9),VTag(10),VTag(11));
end,
Vmax=3+str2num(nbps);
if Vmax >= str2num(nbobj),
    if isempty(VStr)==1,
        VCol=get(gcbo,'BackgroundColor');
        VBox=strcat('EditText',num2str(str2num(nbobj)+44));
        set(findobj(gcf,'Tag',VBox),'BackgroundColor',VCol);
        set(findobj(gcf,'Tag',VBox),'Enable','on');
    else,
        if VStr =='0',
            VCol=get(gcbo,'BackgroundColor');
            VBox=strcat('EditText',num2str(str2num(nbobj)+44));
            set(findobj(gcf,'Tag',VBox),'BackgroundColor',VCol);
            set(findobj(gcf,'Tag',VBox),'Enable','on');
            set(findobj(gcf,'Tag',VTag),'String','');
        else,
            VBox=strcat('EditText',num2str(str2num(nbobj)+44));
            set(findobj(gcf,'Tag',VBox),'BackgroundColor',[0 1 0]);
            set(findobj(gcf,'Tag',VBox),'Enable','off');
        end,
    end,
end,
if (str2num(nbobj)-4) == str2num(nbps),
    MovingEnd4,
end
