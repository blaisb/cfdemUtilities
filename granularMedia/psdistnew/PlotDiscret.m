global axehdl fig1

nbps=get(findobj(gcf,'Tag','EditText1'),'String');

figure(1)
rho=get(findobj(gcf,'Tag','EditText12'),'Value');

figure(2)
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

mtot=0;
clear dd pm mm;
for i = 1:str2num(nbps),
   VBox = strcat('EditText', num2str(i+4));
   nn(i)=str2num(get(findobj(gcf,'Tag',VBox),'String'));
   VBox = strcat('EditText', num2str(i+49));
   dd(i)=str2num(get(findobj(gcf,'Tag',VBox),'String'));
   mm(i)=nn(i)*rho*4/3*pi*(dd(i)/(2*1000000))^3;
   mtot=mtot+mm(i);
end
pm=cumsum((mm./mtot*100),2)';
figure(fig1);
hold on;
set(gcf,'CurrentAxes',axehdl)
plot(dd,pm,'g*');
