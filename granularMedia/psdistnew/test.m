function varargout = test(varargin)
% TEST Application M-file for test.fig
%    FIG = TEST launch test GUI.
%    TEST('callback_name', ...) invoke the named callback.

% Last Modified by GUIDE v2.5 12-Jan-2015 14:29:51

if nargin == 0  % LAUNCH GUI

    fig = openfig(mfilename,'new');
    global fig2;
    global fig1;
    global fich;
    global fig3;
    fig2=gcf;

    % Generate a structure of handles to pass to callbacks, and store it.
    handles = guihandles(fig);
    guidata(fig, handles);

    if nargout > 0
        varargout{1} = fig;
    end

elseif ischar(varargin{1}) % INVOKE NAMED SUBFUNCTION OR CALLBACK

    try
        if (nargout)
            [varargout{1:nargout}] = feval(varargin{:}); % FEVAL switchyard
        else
            feval(varargin{:}); % FEVAL switchyard
        end
    catch
        disp(lasterr);
    end

end


%| ABOUT CALLBACKS:
%| GUIDE automatically appends subfunction prototypes to this file, and
%| sets objects' callback properties to call them through the FEVAL
%| switchyard above. This comment describes that mechanism.
%|
%| Each callback subfunction declaration has the following form:
%| <SUBFUNCTION_NAME>(H, EVENTDATA, HANDLES, VARARGIN)
%|
%| The subfunction name is composed using the object's Tag and the
%| callback type separated by '_', e.g. 'slider2_Callback',
%| 'figure1_CloseRequestFcn', 'axis1_ButtondownFcn'.
%|
%| H is the callback object's handle (obtained using GCBO).
%|
%| EVENTDATA is empty, but reserved for future use.
%|
%| HANDLES is a structure containing handles of components in GUI using
%| tags as fieldnames, e.g. handles.figure1, handles.slider2. This
%| structure is created at GUI startup using GUIHANDLES and stored in
%| the figure's application data using GUIDATA. A copy of the structure
%| is passed to each callback.  You can store additional information in
%| this structure at GUI startup, and you can change the structure
%| during callbacks.  Call guidata(h, handles) after changing your
%| copy to replace the stored original so that subsequent callbacks see
%| the updates. Type "help guihandles" and "help guidata" for more
%| information.
%|
%| VARARGIN contains any extra arguments you have passed to the
%| callback. Specify the extra arguments by editing the callback
%| property in the inspector. By default, GUIDE sets the property to:
%| <MFILENAME>('<SUBFUNCTION_NAME>', gcbo, [], guidata(gcbo))
%| Add any extra arguments after the last argument, before the final
%| closing parenthesis.



% --------------------------------------------------------------------






% --------------------------------------------------------------------
function varargout = Pushbutton1_Callback(h, eventdata, handles, varargin)
auto=get(findobj(gcf,'Tag','checkbox1'),'Value');
if auto==1
    setupboxes2
else
    setupboxes
end



% --------------------------------------------------------------------
function varargout = EditText50_Callback(h, eventdata, handles, varargin)
global fig2;
global fig1;
global fich;
%global fig3;
% callback for first cell of diameter column
figure(fig1);
Vmod=get(findobj(gcf,'Tag','PopupMenu1'),'Value');
k=get(findobj(gcf,'Tag','EditText1'),'Value');
n=get(findobj(gcf,'Tag','EditText2'),'Value');
rho=str2num(get(findobj(gcf,'Tag','EditText12'),'String'));

if Vmod==5
    xg=k;
    sg=n;
    xbar=get(findobj(gcf,'Tag','EditText6'),'Value');
    sbar=get(findobj(gcf,'Tag','EditText7'),'Value');
end

figure(fig2);
x=str2num(get(gco,'String'));

cw=str2num(get(findobj(gcf,'Tag','EditText3'),'String'));
area=str2num(get(findobj(gcf,'Tag','EditText4'),'String'));

Vmodfit=get(findobj(gcf,'Tag','PopupMenu1'),'Value');
if Vmodfit == 2,
    Vmod = 6;
end

if isempty(cw) == 1,
    set(findobj(gcf,'Tag','EditText3'),'String','10');
    cw=10;
end,

if isempty(area) == 1,
    set(findobj(gcf,'Tag','EditText4'),'String','100');
    area=100;
end,

if Vmod == 1,
    y=(x^n/k^n);
elseif Vmod == 2,
    y=(1-(1-x/k)^n);
elseif Vmod == 3,
    y=erf(log(x/k)/n);
elseif Vmod == 4,
    y=(1-exp(-(x^n/k^n)));
elseif Vmod == 5
    y=1/2*(1+erf(log(x/xg)/(sqrt(2)*log(sg))));

    %%%added on 16/01/2003
elseif Vmod == 6,
    taille=size(fich,1);
    if taille ~= 0,
        dd=fich(:,1);
        mp=fich(:,2);
        y=interp1(dd,mp,x,'cubic')/100;
    end
    %%end of added part
end,


Mt=area/(1000000)^2*cw/1000;
m=rho*4/3*pi*(x/(2*1000000))^3;
np=num2str(round(Mt*y/m));
set(findobj(gcf,'Tag','EditText5'),'String',np);




% --------------------------------------------------------------------
function varargout = EditText94_Callback(h, eventdata, handles, varargin)

%callback for last cell of diameter column

figure(1);
Vmod=get(findobj(gcf,'Tag','PopupMenu1'),'Value');
k=get(findobj(gcf,'Tag','EditText1'),'Value');
n=get(findobj(gcf,'Tag','EditText2'),'Value');
rho=str2num(get(findobj(gcf,'Tag','EditText12'),'String'));
if isempty(rho)
    rho=get(findobj(gcf,'Tag','EditText12'),'Value');
end
if Vmod==5
    xg=k;
    sg=n;
    xbar=get(findobj(gcf,'Tag','EditText6'),'Value');
    sbar=get(findobj(gcf,'Tag','EditText7'),'Value');
end

figure(2);
VTag=get(gcbo,'Tag');
VStr=get(gcbo,'String');

if size(VTag,2) == 9,
    nbobj=VTag(9);
elseif  size(VTag,2) == 10,
    nbobj=strcat(VTag(9),VTag(10));
elseif  size(VTag,2) == 11,
    nbobj=strcat(VTag(9),VTag(10),VTag(11));
end,

VBox=strcat('EditText',num2str(str2num(nbobj)-45));
ndmax=str2num(get(findobj(gcf,'Tag',VBox),'String'));

if isempty(ndmax) == 1,ndmax=1;
    set(findobj(gcf,'Tag',VBox),'String','1');
end,

dmax=str2num(get(gco,'String'));
cw=str2num(get(findobj(gcf,'Tag','EditText3'),'String'));
area=str2num(get(findobj(gcf,'Tag','EditText4'),'String'));

if isempty(cw) == 1,set(findobj(gcf,'Tag','EditText3'),'String','10');
    cw=10;
end,

if isempty(area) == 1,set(findobj(gcf,'Tag','EditText4'),'String','100');
    area=100;
end,

Mt=area/(1000000)^2*cw/1000;
m=rho*4/3*pi*(dmax/(2*1000000))^3;

Vmodfit=get(findobj(gcf,'Tag','PopupMenu1'),'Value');
if Vmodfit == 2,
    Vmod = 6;
end

if Vmod == 1,
    fdmax=(dmax^n/k^n);
    x=k*(fdmax-ndmax*m/Mt)^(1/n);

elseif Vmod == 2,
    fdmax=(1-(1-dmax/k)^n);
    x=k*(1-(1-fdmax+ndmax*m/Mt)^(1/n));

elseif Vmod == 3,
    fdmax=erf(log(dmax/k)/n);
    x=k*exp(n*erfinv(fdmax-ndmax*m/Mt));

elseif Vmod == 4,
    fdmax=(1-exp(-(dmax^n/k^n)));
    x=(-(k^n)*log(1-fdmax+ndmax*m/Mt))^(1/n);
    %%%added on 16/01/2003

elseif Vmod == 5
    fdmax=1/2*(1+erf(log(dmax/xg)/(sqrt(2)*log(sg))));
    x=xg*exp(sqrt(2)*log(sg)*erfinv(2*(fdmax-ndmax*mmax/Mt)-1));

elseif Vmod ==6,
    global fich;
    taille=size(fich,1);
    if taille ~= 0,
        dd=fich(:,1);
        mp=fich(:,2);
        fdmax=interp1(dd,mp,dmax,'cubic')/100;
        x=interp1(mp,dd,(fdmax-ndmax*m/Mt)*100,'cubic');
    end
    %%end of added part
end,

VBox=strcat('EditText',num2str(str2num(nbobj)-1));
set(findobj(gcf,'Tag',VBox),'String',x);



% --------------------------------------------------------------------
function varargout = EditText49_Callback(h, eventdata, handles, varargin)

%callback for last cell of nb particles column

figure(1);
Vmod=get(findobj(gcf,'Tag','PopupMenu1'),'Value');
k=get(findobj(gcf,'Tag','EditText1'),'Value');
n=get(findobj(gcf,'Tag','EditText2'),'Value');
rho=str2num(get(findobj(gcf,'Tag','EditText12'),'String'));
if isempty(rho)
    rho=get(findobj(gcf,'Tag','EditText12'),'Value');
end
if Vmod==5
    xg=k;
    sg=n;
    xbar=get(findobj(gcf,'Tag','EditText6'),'Value');
    sbar=get(findobj(gcf,'Tag','EditText7'),'Value');
end
figure(2);
VTag=get(gcbo,'Tag');
Vmodfit=get(findobj(gcf,'Tag','PopupMenu1'),'Value');
if Vmodfit == 2,
    Vmod = 6;
end

if size(VTag,2) == 9,
    nbobj=VTag(9);
elseif  size(VTag,2) == 10,
    nbobj=strcat(VTag(9),VTag(10));
elseif  size(VTag,2) == 11,
    nbobj=strcat(VTag(9),VTag(10),VTag(11));
end,

VBox=strcat('EditText',num2str(str2num(nbobj)+45));
dmax=str2num(get(findobj(gcf,'Tag',VBox),'String'));
ndmax=round(str2num(get(gco,'String')));
set(gco,'String',num2str(ndmax));

if isempty(dmax) == 0,

    cw=str2num(get(findobj(gcf,'Tag','EditText3'),'String'));
    area=str2num(get(findobj(gcf,'Tag','EditText4'),'String'));

    if isempty(cw) == 1,set(findobj(gcf,'Tag','EditText3'),'String','10');
        cw=10;
    end,

    if isempty(area) == 1,set(findobj(gcf,'Tag','EditText4'),'String','100');
        area=100;
    end,

    Mt=area/(1000000)^2*cw/1000;
    m=rho*4/3*pi*(dmax/(2*1000000))^3;

    if Vmod == 1,fdmax=(dmax^n/k^n);
        x=k*(fdmax-ndmax*m/Mt)^(1/n);
    elseif Vmod == 2,fdmax=(1-(1-dmax/k)^n);
        x=k*(1-(1-fdmax+ndmax*m/Mt)^(1/n));
    elseif Vmod == 3,fdmax=erf(log(dmax/k)/n);
        x=k*exp(n*erfinv(fdmax-ndmax*m/Mt));
    elseif Vmod == 4,fdmax=(1-exp(-(dmax^n/k^n)));
        x=(-(k^n)*log(1-fdmax+ndmax*m/Mt))^(1/n);
        %%%added on 16/01/2003
    elseif Vmod == 5
        fdmax=1/2*(1+erf(log(dmax/xg)/(sqrt(2)*log(sg))));
        X=xg*exp(sqrt(2)*log(sg)*erfinv(2*(fdmax-ndmax*mmax/Mt)-1));
    elseif Vmod ==6,
        global fich;
        taille=size(fich,1);
        if taille ~= 0,
            dd=fich(:,1);
            mp=fich(:,2);
            fdmax=interp1(dd,mp,dmax,'cubic')/100;
            x=interp1(mp,dd,(fdmax-ndmax*m/Mt)*100,'cubic');
        end
        %%end of added part
    end,

    VBox=strcat('EditText',num2str(str2num(nbobj)+44));
    set(findobj(gcf,'Tag',VBox),'String',x);
end





% --------------------------------------------------------------------
function varargout = EditText51_Callback(h, eventdata, handles, varargin)
colorchange

% --------------------------------------------------------------------
function varargout = EditText52_Callback(h, eventdata, handles, varargin)
colorchange


% --------------------------------------------------------------------
function varargout = EditText53_Callback(h, eventdata, handles, varargin)
colorchange


% --------------------------------------------------------------------
function varargout = EditText54_Callback(h, eventdata, handles, varargin)
colorchange


% --------------------------------------------------------------------
function varargout = EditText55_Callback(h, eventdata, handles, varargin)
colorchange


% --------------------------------------------------------------------
function varargout = EditText56_Callback(h, eventdata, handles, varargin)
colorchange


% --------------------------------------------------------------------
function varargout = EditText57_Callback(h, eventdata, handles, varargin)
colorchange

% --------------------------------------------------------------------
function varargout = EditText60_Callback(h, eventdata, handles, varargin)
colorchange


% --------------------------------------------------------------------
function varargout = EditText58_Callback(h, eventdata, handles, varargin)
colorchange

% --------------------------------------------------------------------
function varargout = EditText59_Callback(h, eventdata, handles, varargin)
colorchange

% --------------------------------------------------------------------
function varargout = EditText61_Callback(h, eventdata, handles, varargin)
colorchange

% --------------------------------------------------------------------
function varargout = EditText62_Callback(h, eventdata, handles, varargin)
colorchange

% --------------------------------------------------------------------
function varargout = EditText63_Callback(h, eventdata, handles, varargin)
colorchange

% --------------------------------------------------------------------
function varargout = EditText64_Callback(h, eventdata, handles, varargin)
colorchange

% --------------------------------------------------------------------
function varargout = EditText65_Callback(h, eventdata, handles, varargin)
colorchange


% --------------------------------------------------------------------
function varargout = EditText66_Callback(h, eventdata, handles, varargin)
colorchange


% --------------------------------------------------------------------
function varargout = EditText67_Callback(h, eventdata, handles, varargin)
colorchange

% --------------------------------------------------------------------
function varargout = EditText70_Callback(h, eventdata, handles, varargin)
colorchange


% --------------------------------------------------------------------
function varargout = EditText68_Callback(h, eventdata, handles, varargin)
colorchange

% --------------------------------------------------------------------
function varargout = EditText69_Callback(h, eventdata, handles, varargin)
colorchange

% --------------------------------------------------------------------
function varargout = EditText71_Callback(h, eventdata, handles, varargin)
colorchange

% --------------------------------------------------------------------
function varargout = EditText72_Callback(h, eventdata, handles, varargin)
colorchange

% --------------------------------------------------------------------
function varargout = EditText73_Callback(h, eventdata, handles, varargin)
colorchange

% --------------------------------------------------------------------
function varargout = EditText74_Callback(h, eventdata, handles, varargin)
colorchange

% --------------------------------------------------------------------
function varargout = EditText75_Callback(h, eventdata, handles, varargin)
colorchange


% --------------------------------------------------------------------
function varargout = EditText76_Callback(h, eventdata, handles, varargin)
colorchange


% --------------------------------------------------------------------
function varargout = EditText77_Callback(h, eventdata, handles, varargin)
colorchange

% --------------------------------------------------------------------
function varargout = EditText80_Callback(h, eventdata, handles, varargin)
colorchange


% --------------------------------------------------------------------
function varargout = EditText78_Callback(h, eventdata, handles, varargin)
colorchange

% --------------------------------------------------------------------
function varargout = EditText79_Callback(h, eventdata, handles, varargin)
colorchange

% --------------------------------------------------------------------
function varargout = EditText81_Callback(h, eventdata, handles, varargin)
colorchange

% --------------------------------------------------------------------
function varargout = EditText82_Callback(h, eventdata, handles, varargin)
colorchange

% --------------------------------------------------------------------
function varargout = EditText83_Callback(h, eventdata, handles, varargin)
colorchange

% --------------------------------------------------------------------
function varargout = EditText84_Callback(h, eventdata, handles, varargin)
colorchange

% --------------------------------------------------------------------
function varargout = EditText85_Callback(h, eventdata, handles, varargin)
colorchange


% --------------------------------------------------------------------
function varargout = EditText86_Callback(h, eventdata, handles, varargin)
colorchange


% --------------------------------------------------------------------
function varargout = EditText87_Callback(h, eventdata, handles, varargin)
colorchange

% --------------------------------------------------------------------
function varargout = EditText90_Callback(h, eventdata, handles, varargin)
colorchange


% --------------------------------------------------------------------
function varargout = EditText88_Callback(h, eventdata, handles, varargin)
colorchange

% --------------------------------------------------------------------
function varargout = EditText89_Callback(h, eventdata, handles, varargin)
colorchange

% --------------------------------------------------------------------
function varargout = EditText91_Callback(h, eventdata, handles, varargin)
colorchange

% --------------------------------------------------------------------
function varargout = EditText92_Callback(h, eventdata, handles, varargin)
colorchange

% --------------------------------------------------------------------
function varargout = EditText93_Callback(h, eventdata, handles, varargin)
colorchange

% --------------------------------------------------------------------
% --------------------------------------------------------------------
% --------------------------------------------------------------------
function varargout = EditText7_Callback(h, eventdata, handles, varargin)
colorchange2

% --------------------------------------------------------------------
function varargout = EditText8_Callback(h, eventdata, handles, varargin)
colorchange2

% --------------------------------------------------------------------
function varargout = EditText9_Callback(h, eventdata, handles, varargin)
colorchange2

% --------------------------------------------------------------------
function varargout = EditText10_Callback(h, eventdata, handles, varargin)
colorchange2

% --------------------------------------------------------------------
function varargout = EditText11_Callback(h, eventdata, handles, varargin)
colorchange2

% --------------------------------------------------------------------
function varargout = EditText12_Callback(h, eventdata, handles, varargin)
colorchange2

% --------------------------------------------------------------------
function varargout = EditText13_Callback(h, eventdata, handles, varargin)
colorchange2

% --------------------------------------------------------------------
function varargout = EditText14_Callback(h, eventdata, handles, varargin)
colorchange2

% --------------------------------------------------------------------
function varargout = EditText15_Callback(h, eventdata, handles, varargin)
colorchange2

% --------------------------------------------------------------------
function varargout = EditText16_Callback(h, eventdata, handles, varargin)
colorchange2

% --------------------------------------------------------------------
function varargout = EditText17_Callback(h, eventdata, handles, varargin)
colorchange2

% --------------------------------------------------------------------
function varargout = EditText18_Callback(h, eventdata, handles, varargin)
colorchange2

% --------------------------------------------------------------------
function varargout = EditText19_Callback(h, eventdata, handles, varargin)
colorchange2

% --------------------------------------------------------------------
function varargout = EditText20_Callback(h, eventdata, handles, varargin)
colorchange2

% --------------------------------------------------------------------
function varargout = EditText21_Callback(h, eventdata, handles, varargin)
colorchange2

% --------------------------------------------------------------------
function varargout = EditText22_Callback(h, eventdata, handles, varargin)
colorchange2

% --------------------------------------------------------------------
function varargout = EditText23_Callback(h, eventdata, handles, varargin)
colorchange2

% --------------------------------------------------------------------
function varargout = EditText24_Callback(h, eventdata, handles, varargin)
colorchange2

% --------------------------------------------------------------------
function varargout = EditText25_Callback(h, eventdata, handles, varargin)
colorchange2

% --------------------------------------------------------------------
function varargout = EditText26_Callback(h, eventdata, handles, varargin)
colorchange2

% --------------------------------------------------------------------
function varargout = EditText27_Callback(h, eventdata, handles, varargin)
colorchange2

% --------------------------------------------------------------------
function varargout = EditText28_Callback(h, eventdata, handles, varargin)
colorchange2

% --------------------------------------------------------------------
function varargout = EditText29_Callback(h, eventdata, handles, varargin)
colorchange2

% --------------------------------------------------------------------
function varargout = EditText30_Callback(h, eventdata, handles, varargin)
colorchange2

% --------------------------------------------------------------------
function varargout = EditText31_Callback(h, eventdata, handles, varargin)
colorchange2

% --------------------------------------------------------------------
function varargout = EditText32_Callback(h, eventdata, handles, varargin)
colorchange2

% --------------------------------------------------------------------
function varargout = EditText33_Callback(h, eventdata, handles, varargin)
colorchange2

% --------------------------------------------------------------------
function varargout = EditText34_Callback(h, eventdata, handles, varargin)
colorchange2

% --------------------------------------------------------------------
function varargout = EditText35_Callback(h, eventdata, handles, varargin)
colorchange2

% --------------------------------------------------------------------
function varargout = EditText36_Callback(h, eventdata, handles, varargin)
colorchange2

% --------------------------------------------------------------------
function varargout = EditText37_Callback(h, eventdata, handles, varargin)
colorchange2

% --------------------------------------------------------------------
function varargout = EditText38_Callback(h, eventdata, handles, varargin)
colorchange2

% --------------------------------------------------------------------
function varargout = EditText39_Callback(h, eventdata, handles, varargin)
colorchange2

% --------------------------------------------------------------------
function varargout = EditText40_Callback(h, eventdata, handles, varargin)
colorchange2

% --------------------------------------------------------------------
function varargout = EditText41_Callback(h, eventdata, handles, varargin)
colorchange2

% --------------------------------------------------------------------
function varargout = EditText42_Callback(h, eventdata, handles, varargin)
colorchange2

% --------------------------------------------------------------------
function varargout = EditText43_Callback(h, eventdata, handles, varargin)
colorchange2

% --------------------------------------------------------------------
function varargout = EditText44_Callback(h, eventdata, handles, varargin)
colorchange2

% --------------------------------------------------------------------
function varargout = EditText45_Callback(h, eventdata, handles, varargin)
colorchange2

% --------------------------------------------------------------------
function varargout = EditText46_Callback(h, eventdata, handles, varargin)
colorchange2

% --------------------------------------------------------------------
function varargout = EditText47_Callback(h, eventdata, handles, varargin)
colorchange2

% --------------------------------------------------------------------
function varargout = EditText48_Callback(h, eventdata, handles, varargin)
colorchange2

% --------------------------------------------------------------------
function varargout = EditText1_Callback(h, eventdata, handles, varargin)

valeur=str2num(get(findobj(gcf,'Tag','EditText1'),'String'));
set(findobj(gcf,'Tag','EditText1'),'Value',valeur);
Value=get(findobj(gcf,'Tag','PopupMenu2'),'Value');


% --------------------------------------------------------------------
function varargout = PopupMenu2_Callback(h, eventdata, handles, varargin)

Vshape=get(findobj(gcf,'Tag','PopupMenu2'),'Value');
if Vshape==2 | Vshape==3
    set(findobj(gcf,'Tag','StaticText57'),'Visible','on');
    set(findobj(gcf,'Tag','PopupMenu3'),'Visible','on');
elseif Vshape==1
    set(findobj(gcf,'Tag','StaticText57'),'Visible','off');
    set(findobj(gcf,'Tag','PopupMenu3'),'Visible','off');
end

% --------------------------------------------------------------------
function varargout = Pushbutton2_Callback(h, eventdata, handles, varargin)
auto=get(findobj(gcf,'Tag','checkbox1'),'Value');
if auto==1
    computeINT
else
    computePSD
end

%Specific surface
figure(fig1)
rho=str2num(get(findobj(gcf,'Tag','EditText12'),'String'));
if isempty(rho)
    rho=get(findobj(gcf,'Tag','EditText12'),'Value');
end

figure(fig2)
S2=0;
S3=0;
shap=get(findobj(gcf,'Tag','PopupMenu2'),'Value');
para=get(findobj(gcf,'Tag','PopupMenu3'),'Value');

nbcase=str2num(get(findobj(gcf,'Tag','EditText1'),'String'));
for i = 1:nbcase
    nbr=strcat('EditText',num2str(i+4));
    dia=strcat('EditText',num2str(i+49));
    rat=strcat('EditText',num2str(i+94));
    nombre(i)=str2num(get(findobj(gcf,'Tag',nbr),'String'));
    diametre(i)=str2num(get(findobj(gcf,'Tag',dia),'String'))*10^-6;
    aspect(i)=str2num(get(findobj(gcf,'Tag',rat),'String'));
    if shap == 1
    S2=S2+6*(nombre(i)*(diametre(i))^2);
    S3=S3+(nombre(i)*(diametre(i))^3);
    elseif shap == 2
        if para == 1
            a=diametre(i)*(aspect(i)^(1/3))/2;
            b=a/aspect(i);
            e=sqrt((a^2)-(b^2))/a;
            S2=S2+nombre(i)*((2*pi*a^2)+(pi*b^2*log((1+e)/(1-e))/e));
            S3=S3+nombre(i)*4*pi*a*a*b/3;
        elseif para == 2
            a=(((diametre(i)/2)^3)/(aspect(i)/2))^(1/2);
            b=aspect(i);
            e=sqrt((a^2)-(b^2))/a;
            S2=S2+nombre(i)*((2*pi*a^2)+(pi*b^2*log((1+e)/(1-e))/e));
            S3=S3+nombre(i)*4*pi*a*a*b/3;
            end
    elseif shap == 3
        if para == 1
            b=(diametre(i)/2)*(1/(aspect(i)^(1/3)));
            a=b*aspect(i);
            e=sqrt((a^2)-(b^2))/a;
            S2=S2+nombre(i)*((2*pi*b^2)+(2*pi*a*b*asin(e)/e));
            S3=S3+nombre(i)*4*pi*a*b*b/3;
        elseif para == 2
            a=((diametre(i)/2)^3)/((aspect(i)/2)^2);
            b=aspect(i)/2;
            e=sqrt((a^2)-(b^2))/a;
            S2=S2+nombre(i)*((2*pi*b^2)+(2*pi*a*b*asin(e)/e));
            S3=S3+nombre(i)*4*pi*a*b*b/3;
        end        
    end
end
So1=S2/S3/(10^6);
set(findobj(gcf,'Tag','EditText200'),'String',num2str(So1));
So2=S2/S3/rho/1000;
set(findobj(gcf,'Tag','EditText201'),'String',num2str(So2));

%Diametre
Dss=6/So1; %(um)
set(findobj(gcf,'Tag','edit302'),'String',num2str(Dss));
Dmean1=sum(nombre.*diametre)*10^6/sum(nombre); %(um)
set(findobj(gcf,'Tag','edit299'),'String',num2str(Dmean1));
Dmean2=(sum(nombre.*(diametre.^4))/(sum(nombre.*(diametre.^3))))*10^6; %(um)
set(findobj(gcf,'Tag','edit301'),'String',num2str(Dmean2));
a=0;
Nmed=sum(nombre)/2;
for i=nbcase:-1:1
    if Nmed > a && Nmed <= nombre(i)+a
        Dmed=diametre(i)*10^6; %(um)
    end
    a=a+nombre(i);
end
set(findobj(gcf,'Tag','edit295'),'String',num2str(Dmed));
Dmed2=diametre(round(nbcase/2))*10^6;
set(findobj(gcf,'Tag','edit303'),'String',num2str(Dmed2));

%Skewness
n=sum(nombre);
diametre=diametre*10^6;
Dmean=sum(diametre.*nombre)/n; %(um)
Sknum=0;
Skden=0;
for i = 1:nbcase
    Sknum=Sknum + nombre(i)*(diametre(i)-Dmean)^3;
    Skden=Skden + nombre(i)*(diametre(i)-Dmean)^2;
end
Sk = (Sknum/n)/((Skden/n)^(3/2));
set(findobj(gcf,'Tag','EditText202'),'String',num2str(Sk));
    

% --------------------------------------------------------------------
function varargout = EditText200_Callback(h, eventdata, handles, varargin)

valeur=str2num(get(findobj(gcf,'Tag','EditText200'),'String'));
set(findobj(gcf,'Tag','EditText200'),'Value',valeur);
Value=get(findobj(gcf,'Tag','PopupMenu2'),'Value');

% --------------------------------------------------------------------
function varargout = EditText201_Callback(h, eventdata, handles, varargin)

valeur=str2num(get(findobj(gcf,'Tag','EditText201'),'String'));
set(findobj(gcf,'Tag','EditText201'),'Value',valeur);
Value=get(findobj(gcf,'Tag','PopupMenu2'),'Value');


% --------------------------------------------------------------------
function varargout = Pushbutton6_Callback(h, eventdata, handles, varargin)
global filename;

[temp1, temp2] = uigetfile( ...
    {
    '*.*',  'All Files (*.*)'}, ...
    'Pick a file');
if isequal(temp1,0)|isequal(temp2,0)
else
    filename=strcat(temp2,temp1);
    loadDis;
end

% --------------------------------------------------------------------
function varargout = pushbutton10_Callback(h, eventdata, handles, varargin)

Subgrid

% --------------------------------------------------------------------
function varargout = checkbox2_Callback(h, eventdata, handles, varargin)

Vcheck=get(findobj(gcf,'Tag','checkbox2'),'Value');
if Vcheck==0
    set(findobj(gcf,'Tag','StaticText59'),'Visible','off');
    set(findobj(gcf,'Tag','EditText142'),'Visible','off');
    set(findobj(gcf,'Tag','EditText142'),'String','0');
else
    set(findobj(gcf,'Tag','StaticText59'),'Visible','on');
    set(findobj(gcf,'Tag','EditText142'),'Visible','on');
    set(findobj(gcf,'Tag','EditText142'),'String','0');
end





% --------------------------------------------------------------------
function varargout = EditText142_Callback(h, eventdata, handles, varargin)



% --- Executes on button press in pushAspect.
function pushAspect_Callback(hObject, eventdata, handles)
% hObject    handle to pushAspect (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global aspectfile;

[temp1, temp2] = uigetfile( ...
    {
    '*.*',  'All Files (*.*)'}, ...
    'Pick a file');
if isequal(temp1,0)|isequal(temp2,0)
else
    aspectfile=strcat(temp2,temp1);
    loadaspect;
end

% function EditText200_Callback(hObject, eventdata, handles)
% % hObject    handle to EditText200 (see GCBO)
% % eventdata  reserved - to be defined in a future version of MATLAB
% % handles    structure with handles and user data (see GUIDATA)
% 
% % Hints: get(hObject,'String') returns contents of EditText200 as text
% %        str2double(get(hObject,'String')) returns contents of EditText200 as a double


% --- Executes during object creation, after setting all properties.
function EditText200_CreateFcn(hObject, eventdata, handles)
% hObject    handle to EditText200 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



% function EditText201_Callback(hObject, eventdata, handles)
% % hObject    handle to EditText201 (see GCBO)
% % eventdata  reserved - to be defined in a future version of MATLAB
% % handles    structure with handles and user data (see GUIDATA)
% 
% % Hints: get(hObject,'String') returns contents of EditText201 as text
% %        str2double(get(hObject,'String')) returns contents of EditText201 as a double


% --- Executes during object creation, after setting all properties.
function EditText201_CreateFcn(hObject, eventdata, handles)
% hObject    handle to EditText201 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% % --- Executes on button press in pushbutton10.
% function pushbutton10_Callback(hObject, eventdata, handles)
% % hObject    handle to pushbutton10 (see GCBO)
% % eventdata  reserved - to be defined in a future version of MATLAB
% % handles    structure with handles and user data (see GUIDATA)


% --- Executes during object creation, after setting all properties.
function Fig2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to Fig2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called



function EditText202_Callback(hObject, eventdata, handles)
% hObject    handle to EditText202 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of EditText202 as text
%        str2double(get(hObject,'String')) returns contents of EditText202 as a double


% --- Executes during object creation, after setting all properties.
function EditText202_CreateFcn(hObject, eventdata, handles)
% hObject    handle to EditText202 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function edit295_Callback(hObject, eventdata, handles)
% hObject    handle to edit295 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit295 as text
%        str2double(get(hObject,'String')) returns contents of edit295 as a double


% --- Executes during object creation, after setting all properties.
function edit295_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit295 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function edit299_Callback(hObject, eventdata, handles)
% hObject    handle to edit299 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit299 as text
%        str2double(get(hObject,'String')) returns contents of edit299 as a double


% --- Executes during object creation, after setting all properties.
function edit299_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit299 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function edit300_Callback(hObject, eventdata, handles)
% hObject    handle to edit300 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit300 as text
%        str2double(get(hObject,'String')) returns contents of edit300 as a double


% --- Executes during object creation, after setting all properties.
function edit300_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit300 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function edit301_Callback(hObject, eventdata, handles)
% hObject    handle to edit301 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit301 as text
%        str2double(get(hObject,'String')) returns contents of edit301 as a double


% --- Executes during object creation, after setting all properties.
function edit301_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit301 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function edit302_Callback(hObject, eventdata, handles)
% hObject    handle to edit302 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit302 as text
%        str2double(get(hObject,'String')) returns contents of edit302 as a double


% --- Executes during object creation, after setting all properties.
function edit302_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit302 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function edit303_Callback(hObject, eventdata, handles)
% hObject    handle to edit303 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit303 as text
%        str2double(get(hObject,'String')) returns contents of edit303 as a double


% --- Executes during object creation, after setting all properties.
function edit303_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit303 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in pushbutton4.
function pushbutton4_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

MaxPackFraction

function edit304_Callback(hObject, eventdata, handles)
% hObject    handle to edit304 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit304 as text
%        str2double(get(hObject,'String')) returns contents of edit304 as a double


% --- Executes during object creation, after setting all properties.
function edit304_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit304 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end
