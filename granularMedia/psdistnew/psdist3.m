function varargout = psdist3(varargin)
% TEST Application M-file for test.fig
%    FIG = TEST launch test GUI.
%    TEST('callback_name', ...) invoke the named callback.

% Last Modified by GUIDE v2.5 12-Jan-2015 11:48:30

if nargin == 0  % LAUNCH GUI
    
    fig = openfig(mfilename,'new');
    global fig2;
    global fig1;
    global fich;
    global fig3;
    fig1=gcf;
    
    % Generate a structure of handles to pass to callbacks, and store it. 
    handles = guihandles(fig);
    guidata(fig, handles);
    
    if nargout > 0
        varargout{1} = fig;
    end
    h=get(0,'CurrentFigure');
    global h1 h2 h3 h4 h5 a b c d e axehdl
    banner1 = imread(['GGSdist.jpg']);
    banner2 = imread(['GMdist.jpg']);
    banner3 = imread(['LPdist.jpg']);
    banner4 = imread(['RRBdist.JPG']);
    banner5 = imread(['LogNormal2.jpg']);% Read the image file lognormal.jpg
    a=findobj(0,'Tag','Axes6');
    b=findobj(0,'Tag','Axes7');
    c=findobj(0,'Tag','Axes8');
    d=findobj(0,'Tag','Axes9');
    e=findobj(0,'Tag','Axes10');
    axehdl=findobj(0,'Tag','Axes5');
    axes(a);
    h1=imagesc(banner1);
    axes(b);
    h2=imagesc(banner2);
    axes(c);
    h3=imagesc(banner3);
    axes(d);
    h4=imagesc(banner4);
    axes(e);
    h5=imagesc(banner5);
    
    set(a, 'Visible', 'off', 'Units', 'pixels');
    set(b, 'Visible', 'off', 'Units', 'pixels');
    set(c, 'Visible', 'off', 'Units', 'pixels');
    set(d, 'Visible', 'off', 'Units', 'pixels');
    set(e, 'Visible', 'off', 'Units', 'pixels');
    
    set(h1,'Visible','off');
    set(h2,'Visible','off');
    set(h3,'Visible','on');
    set(h4,'Visible','off');
    set(h5,'Visible','off');
    
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



% --------------------------------------------------------------------
function varargout = edit1_Callback(h, eventdata, handles, varargin)




% --------------------------------------------------------------------
function varargout = edit2_Callback(h, eventdata, handles, varargin)




% --------------------------------------------------------------------
function varargout = PopupMenu1_Callback(h, eventdata, handles, varargin)

global h1 h2 h3 h4 h5 a b c d e





Value=get(gcbo,'Value');
if Value == 1,
    set(findobj(gcf,'Tag','StaticText1'),'String','k (in microns):');
    set(findobj(gcf,'Tag','StaticText2'),'String','m (-):');
    set(findobj(gcf,'Tag','StaticText9'),'Visible','off');
    set(findobj(gcf,'Tag','StaticText10'),'Visible','off');
    set(findobj(gcf,'Tag','EditText1'),'Visible','on','BackgroundColor',[1 1 1]);
    set(findobj(gcf,'Tag','EditText2'),'Visible','on','BackgroundColor',[1 1 1]);    
    set(findobj(gcf,'Tag','EditText6'),'Visible','off','BackgroundColor',[1 1 1]);
    set(findobj(gcf,'Tag','EditText7'),'Visible','off','BackgroundColor',[1 1 1]);
    axes(a);
    set(h1,'Visible','on');
    set(h2,'Visible','off');
    set(h3,'Visible','off');
    set(h4,'Visible','off');
    set(h5,'Visible','off');
    
elseif Value == 2,
    set(findobj(gcf,'Tag','StaticText1'),'String','k (in microns):');
    set(findobj(gcf,'Tag','StaticText2'),'String','r (-):');
    set(findobj(gcf,'Tag','StaticText9'),'Visible','off');
    set(findobj(gcf,'Tag','StaticText10'),'Visible','off');
    set(findobj(gcf,'Tag','EditText1'),'Visible','on','BackgroundColor',[1 1 1]);
    set(findobj(gcf,'Tag','EditText2'),'Visible','on','BackgroundColor',[1 1 1]);
    set(findobj(gcf,'Tag','EditText6'),'Visible','off','BackgroundColor',[1 1 1]);
    set(findobj(gcf,'Tag','EditText7'),'Visible','off','BackgroundColor',[1 1 1]);
    axes(b);
    set(h1,'Visible','off');
    set(h2,'Visible','on');
    set(h3,'Visible','off');
    set(h4,'Visible','off');
    set(h5,'Visible','off');
    
elseif Value == 3,
    set(findobj(gcf,'Tag','StaticText1'),'String','k (in microns):');
    set(findobj(gcf,'Tag','StaticText2'),'String','Standard deviation:');
    set(findobj(gcf,'Tag','StaticText9'),'Visible','off');
    set(findobj(gcf,'Tag','StaticText10'),'Visible','off');
    set(findobj(gcf,'Tag','EditText1'),'Visible','on','BackgroundColor',[1 1 1]);
    set(findobj(gcf,'Tag','EditText2'),'Visible','on','BackgroundColor',[1 1 1]);
    set(findobj(gcf,'Tag','EditText6'),'Visible','off','BackgroundColor',[1 1 1]);
    set(findobj(gcf,'Tag','EditText7'),'Visible','off','BackgroundColor',[1 1 1]);
    axes(c);
    set(h1,'Visible','off');
    set(h2,'Visible','off');
    set(h3,'Visible','on');
    set(h4,'Visible','off');
    set(h5,'Visible','off');
    
    
elseif Value == 4,
    set(findobj(gcf,'Tag','StaticText1'),'String','k (in microns):');
    set(findobj(gcf,'Tag','StaticText2'),'String','n (-):');
    set(findobj(gcf,'Tag','StaticText9'),'Visible','off');
    set(findobj(gcf,'Tag','StaticText10'),'Visible','off');
    set(findobj(gcf,'Tag','EditText1'),'Visible','on','BackgroundColor',[1 1 1]);
    set(findobj(gcf,'Tag','EditText2'),'Visible','on','BackgroundColor',[1 1 1]);
    set(findobj(gcf,'Tag','EditText6'),'Visible','off','BackgroundColor',[1 1 1]);
    set(findobj(gcf,'Tag','EditText7'),'Visible','off','BackgroundColor',[1 1 1]);
    axes(d);
    set(h1,'Visible','off');
    set(h2,'Visible','off');
    set(h3,'Visible','off');
    set(h4,'Visible','on');
    set(h5,'Visible','off');
    
    
elseif Value == 5,
    set(findobj(gcf,'Tag','StaticText1'),'String','x (median):');
    set(findobj(gcf,'Tag','StaticText2'),'String','sigma (median):');
    set(findobj(gcf,'Tag','StaticText9'),'String','x (mean):','Visible','on','ForegroundColor',[0 0 0]);
    set(findobj(gcf,'Tag','StaticText10'),'String','sigma (mean):','Visible','on','ForegroundColor',[0 0 0]);
    set(findobj(gcf,'Tag','EditText6'),'Visible','on','BackgroundColor',[1 1 1]);
    set(findobj(gcf,'Tag','EditText7'),'Visible','on','BackgroundColor',[1 1 1]);
    set(findobj(gcf,'Tag','EditText1'),'Visible','on','BackgroundColor',[1 1 1]);
    set(findobj(gcf,'Tag','EditText2'),'Visible','on','BackgroundColor',[1 1 1]);
    axes(e);
    set(h1,'Visible','off');
    set(h2,'Visible','off');
    set(h3,'Visible','off');
    set(h4,'Visible','off');
    set(h5,'Visible','on');
    
    
end


% --------------------------------------------------------------------
function varargout = EditText1_Callback(h, eventdata, handles, varargin)


valeur=str2num(get(findobj(gcf,'Tag','EditText1'),'String'));
set(findobj(gcf,'Tag','EditText1'),'Value',valeur);
Value=get(findobj(gcf,'Tag','PopupMenu1'),'Value');
if Value==5
    set(findobj(gcf,'Tag','EditText6'),'Visible','on','BackgroundColor',[.8 .8 .8]);
    set(findobj(gcf,'Tag','EditText7'),'Visible','on','BackgroundColor',[.8 .8 .8]);
    set(findobj(gcf,'Tag','EditText1'),'Visible','on','BackgroundColor',[1 1 1]);
    set(findobj(gcf,'Tag','EditText2'),'Visible','on','BackgroundColor',[1 1 1]);
    
    xg=get(findobj(gcf,'Tag','EditText1'),'Value');
    sg=get(findobj(gcf,'Tag','EditText2'),'Value');
    xbar=xg*exp(1/2*log(sg)^2);
    sbar=sqrt((exp(log(sg)^2)-1)*(xg^2*exp(log(sg)^2)));
    set(findobj(gcf,'Tag','EditText6'),'String',num2str(xbar));
    set(findobj(gcf,'Tag','EditText7'),'String',num2str(sbar));
    set(findobj(gcf,'Tag','EditText6'),'Value',xbar);
    set(findobj(gcf,'Tag','EditText7'),'Value',sbar);
end



% --------------------------------------------------------------------
function varargout = EditText2_Callback(h, eventdata, handles, varargin)

valeur=str2num(get(findobj(gcf,'Tag','EditText2'),'String'))
set(findobj(gcf,'Tag','EditText2'),'Value',valeur)

Value=get(findobj(gcf,'Tag','PopupMenu1'),'Value')

if Value==5
    set(findobj(gcf,'Tag','EditText6'),'Visible','on','BackgroundColor',[.8 .8 .8]);
    set(findobj(gcf,'Tag','EditText7'),'Visible','on','BackgroundColor',[.8 .8 .8]);
    set(findobj(gcf,'Tag','EditText1'),'Visible','on','BackgroundColor',[1 1 1]);
    set(findobj(gcf,'Tag','EditText2'),'Visible','on','BackgroundColor',[1 1 1]);
    
    xg=get(findobj(gcf,'Tag','EditText1'),'Value')
    sg=get(findobj(gcf,'Tag','EditText2'),'Value')
    xbar=xg*exp(1/2*log(sg)^2);
    sbar=sqrt((exp(log(sg)^2)-1)*(xg^2*exp(log(sg)^2)));
    
    set(findobj(gcf,'Tag','EditText6'),'String',num2str(xbar));
    set(findobj(gcf,'Tag','EditText7'),'String',num2str(sbar));
    set(findobj(gcf,'Tag','EditText6'),'Value',xbar);
    set(findobj(gcf,'Tag','EditText7'),'Value',sbar);
end



% --------------------------------------------------------------------
function varargout = EditText3_Callback(h, eventdata, handles, varargin)

valeur=str2num(get(findobj(gcf,'Tag','EditText3'),'String'));
set(findobj(gcf,'Tag','EditText3'),'Value',valeur);
Value=get(findobj(gcf,'Tag','PopupMenu1'),'Value');


% --------------------------------------------------------------------
function varargout = EditText5_Callback(h, eventdata, handles, varargin)

valeur=str2num(get(findobj(gcf,'Tag','EditText5'),'String'));
set(findobj(gcf,'Tag','EditText5'),'Value',valeur);
Value=get(findobj(gcf,'Tag','PopupMenu1'),'Value');


% --------------------------------------------------------------------
function varargout = EditText4_Callback(h, eventdata, handles, varargin)

valeur=str2num(get(findobj(gcf,'Tag','EditText4'),'String'));
set(findobj(gcf,'Tag','EditText4'),'Value',valeur);


% --------------------------------------------------------------------
function varargout = EditText12_Callback(h, eventdata, handles, varargin)

valeur=str2num(get(findobj(gcf,'Tag','EditText12'),'String'));
set(findobj(gcf,'Tag','EditText12'),'Value',valeur);
%Value=get(findobj(gcf,'Tag','PopupMenu1'),'Value');


% --------------------------------------------------------------------
function varargout = EditText13_Callback(h, eventdata, handles, varargin)

valeur=str2num(get(findobj(gcf,'Tag','EditText13'),'String'));
set(findobj(gcf,'Tag','EditText13'),'Value',valeur);
%Value=get(findobj(gcf,'Tag','PopupMenu1'),'Value');


% --------------------------------------------------------------------
function varargout = EditText16_Callback(h, eventdata, handles, varargin)

valeur=str2num(get(findobj(gcf,'Tag','EditText16'),'String'));
set(findobj(gcf,'Tag','EditText16'),'Value',valeur);
%Value=get(findobj(gcf,'Tag','PopupMenu1'),'Value');


% --------------------------------------------------------------------
function varargout = Pushbutton1_Callback(h, eventdata, handles, varargin)
global fig1 axehdl fich
figure(fig1)
k=get(findobj(gcf,'Tag','EditText1'),'Value');
n=get(findobj(gcf,'Tag','EditText2'),'Value');
deb=get(findobj(gcf,'Tag','EditText3'),'Value');
fin=get(findobj(gcf,'Tag','EditText4'),'Value');
inter=get(findobj(gcf,'Tag','EditText5'),'Value');
Value=get(findobj(gcf,'Tag','PopupMenu1'),'Value');
Vlog=get(findobj(gcf,'Tag','Checkbox1'),'Value');
Vgrid=get(findobj(gcf,'Tag','Checkbox2'),'Value');
rho=get(findobj(gcf,'Tag','EditText12'),'Value');
if rho==0
    rho=2710; 
    set(findobj(gcf,'Tag','EditText12'),'Value',rho);  
end,

set(gcf,'CurrentAxes',axehdl)
hold off;

x=deb:inter:fin;
if Value == 1,
    y=(x.^n/k^n)*100; 
elseif Value == 2,
    y=(1-(1-x/k).^n)*100;
elseif Value == 3,
    y=erf(log(x./k)/n)*100;
elseif Value == 4,
    y=(1-exp(-(x.^n/k^n)))*100;
elseif Value == 5,
    Color=get(findobj(gcf,'Tag','EditText1'),'BackgroundColor');
    if Color==[1 1 1]
        %fprintf(1,'using xg and sg\n');
        xg=get(findobj(gcf,'Tag','EditText1'),'Value');
        sg=get(findobj(gcf,'Tag','EditText2'),'Value');
        xbar=xg*exp(1/2*log(sg)^2);
        sbar=sqrt((exp(log(sg)^2)-1)*(xg^2*exp(log(sg)^2)));
        set(findobj(gcf,'Tag','EditText6'),'String',num2str(xbar));
        set(findobj(gcf,'Tag','EditText7'),'String',num2str(sbar));
        set(findobj(gcf,'Tag','EditText6'),'Value',xbar);
        set(findobj(gcf,'Tag','EditText7'),'Value',sbar);
    else
        %fprintf(1,'using xbar and sbat\n');
        xbar=get(findobj(gcf,'Tag','EditText6'),'Value');
        sbar=get(findobj(gcf,'Tag','EditText7'),'Value');
        out=lognormal(xbar,sbar);
        xg=out(1);
        sg=out(2);
        set(findobj(gcf,'Tag','EditText1'),'String',num2str(xg));
        set(findobj(gcf,'Tag','EditText2'),'String',num2str(sg));
        set(findobj(gcf,'Tag','EditText1'),'Value',xg);
        set(findobj(gcf,'Tag','EditText2'),'Value',sg);
    end
    y=1/2*(1+erf(log(x/xg)/(sqrt(2)*log(sg))))*100;
end,

if Vlog ==1,
    semilogx(x,y,'Parent',axehdl);
else,
    plot(x,y,'Parent',axehdl);
end,

try,
    taille=size(fich,1);
    if taille ~= 0,
        x=fich(:,1);
        y=fich(:,2);
        hold on;
        plot(x,y,'r+')
        ,if Value == 1,
            y2=(x.^n/k^n)*100;           
        elseif Value == 2,
            y2=(1-(1-x/k).^n)*100;           
        elseif Value == 3,
            y2=erf(log(x./k)/n)*100;            
        elseif Value == 4,
            y2=(1-exp(-(x.^n/k^n)))*100;           
        elseif Value == 5,
            y2=1/2*(1+erf(log(x/xg)/(sqrt(2)*log(sg))))*100;            
        end,
        erreur=(y-y2).^2;
        somerr=sum(erreur);
        set(findobj(gcf,'Tag','EditText20'),'String',somerr);
        Vspline=get(findobj(gcf,'Tag','Checkbox3'),'Value');      
        
        if Vspline ==1,xx=deb:inter:fin;
            yy=INTERP1(x,y,xx,'cubic');
            plot(xx,yy,'r-'),
        end,
    end,
catch,
end,
    
%D(%)and D median
pcum=str2num(get(findobj(gcf,'Tag','EditText17'),'String'));
pcum=pcum/100;
if isempty(pcum)==1
    pcum=0.025;
    set(findobj(gcf,'Tag','EditText17'),'String',num2str(pcum*100));
end,
if Value == 1,
    Dpcum=k*(pcum^(1/n));
    Dmed=k*(0.5^(1/n));
elseif Value == 2,
    Dpcum=k*(1-(1-pcum)^(1/n));
    Dmed=k*(1-(1-0.5)^(1/n));
elseif Value == 3,
    Dpcum=k*exp(n*erfinv(pcum));
    Dmed=k*exp(n*erfinv(0.5));
elseif Value == 4,    
    Dpcum=k*(-log(1-pcum))^(1/n);
    Dmed=k*(-log(1-0.5))^(1/n);
elseif Value == 5,
    Dpcum=xg*exp(sqrt(2)*log(sg)*erfinv((2*pcum)-1)); 
    Dmed=xg*exp(sqrt(2)*log(sg)*erfinv((2*0.5)-1));
end,
set(findobj(gcf,'Tag','EditText16'),'String',num2str(Dpcum));
set(findobj(gcf,'Tag','EditText16'),'Value',Dpcum);
set(findobj(gcf,'Tag','edit7'),'String',num2str(Dmed));

if Vgrid ==1,
    grid on;
else,
    
    grid off;
end,

axis([deb fin 0 100]);
xlabel('Particle Diameter (microns)'),
ylabel('Cumulative Mass (%)'),
hold off;

%Surface Spécifique
deb=deb*10^-6;
fin=fin*10^-6;
inter=inter*10^-6;
k=k*10^-6;
So=intSS(deb,fin,inter,k,n,Value);
Dmeangeo=intDm1(deb,fin,inter,k,n,Value);
Dmean=intDm2(deb,fin,inter,k,n,Value);

SS=So/(10^6);
surf=get(findobj(gcf,'Tag','Checkbox4'),'Value');
if surf ==1
    SS=So/rho/1000;
end
set(findobj(gcf,'Tag','EditText13'),'String',num2str(SS));
set(findobj(gcf,'Tag','EditText13'),'Value',SS);
Dss=6/SS;
set(findobj(gcf,'Tag','edit10'),'String',num2str(Dss));
set(findobj(gcf,'Tag','edit9'),'String',num2str(Dmeangeo*10^6));
set(findobj(gcf,'Tag','edit8'),'String',num2str(Dmean));


hold off;



% --------------------------------------------------------------------
function varargout = Pushbutton2_Callback(h, eventdata, handles, varargin)

loadpsddata,
set(findobj(gcf,'Tag','EditText20'),'Visible','on');
set(findobj(gcf,'Tag','StaticText20'),'Visible','on');


% --------------------------------------------------------------------
function varargout = Pushbutton3_Callback(h, eventdata, handles, varargin)
global axehdl fich
try,
    clear global fich;
    k=get(findobj(gcf,'Tag','EditText1'),'Value');
    n=get(findobj(gcf,'Tag','EditText2'),'Value');
    deb=get(findobj(gcf,'Tag','EditText3'),'Value');
    fin=get(findobj(gcf,'Tag','EditText4'),'Value');
    inter=get(findobj(gcf,'Tag','EditText5'),'Value');
    Value=get(findobj(gcf,'Tag','PopupMenu1'),'Value');
    Vlog=get(findobj(gcf,'Tag','Checkbox1'),'Value');
    Vgrid=get(findobj(gcf,'Tag','Checkbox2'),'Value');
    axes(axehdl)
    reset(gca);
    x=deb:inter:fin;
    if Value == 1,
        y=(x.^n/k^n)*100;
    elseif Value == 2,
        y=(1-(1-x/k).^n)*100;
    elseif Value == 3,
        y=erf(log(x./k)/n)*100;
    elseif Value == 4,
        y=(1-exp(-(x.^n/k^n)))*100;
    elseif Value == 5,
    Color=get(findobj(gcf,'Tag','EditText1'),'BackgroundColor');
    if Color==[1 1 1]
        xg=get(findobj(gcf,'Tag','EditText1'),'Value');
        sg=get(findobj(gcf,'Tag','EditText2'),'Value');
        xbar=xg*exp(1/2*log(sg)^2);
        sbar=sqrt((exp(log(sg)^2)-1)*(xg^2*exp(log(sg)^2)));
    else
        xbar=get(findobj(gcf,'Tag','EditText6'),'Value');
        sbar=get(findobj(gcf,'Tag','EditText7'),'Value');
        out=lognormal(xbar,sbar);
        xg=out(1);
        sg=out(2);
        set(findobj(gcf,'Tag','EditText1'),'String',num2str(xg));
        set(findobj(gcf,'Tag','EditText2'),'String',num2str(sg));
        set(findobj(gcf,'Tag','EditText1'),'Value',xg);
        set(findobj(gcf,'Tag','EditText2'),'Value',sg);
    end
        y=1/2*(1+erf(log(x/xg)/(sqrt(2)*log(sg))))*100;
end,
    if Vlog ==1,
        semilogx(x,y),
    else,
        plot(x,y),
    end,
    if Vgrid ==1,
        grid on;
    else,
        grid off;
    end,
    axis([deb fin 0 100]);
    xlabel('Particle Diameter (microns)'),
    ylabel('Cumulative Mass (%)'),
    hold off;
    set(findobj(gcf,'Tag','EditText20'),'Visible','off');
    set(findobj(gcf,'Tag','StaticText20'),'Visible','off');
catch,
end


% --------------------------------------------------------------------
function varargout = Pushbutton4_Callback(h, eventdata, handles, varargin)

test


% --------------------------------------------------------------------
function varargout = Pushbutton5_Callback(h, eventdata, handles, varargin)

pagedlg2


% --------------------------------------------------------------------
function varargout = Fig1_ResizeFcn(h, eventdata, handles, varargin)




% --------------------------------------------------------------------
function varargout = EditText6_Callback(h, eventdata, handles, varargin)

valeur=str2num(get(findobj(gcf,'Tag','EditText6'),'String'));
set(findobj(gcf,'Tag','EditText6'),'Value',valeur);
Value=get(findobj(gcf,'Tag','PopupMenu1'),'Value');
if Value==5
    set(findobj(gcf,'Tag','EditText1'),'Visible','on','BackgroundColor',[.8 .8 .8]);
    set(findobj(gcf,'Tag','EditText2'),'Visible','on','BackgroundColor',[.8 .8 .8]);
    set(findobj(gcf,'Tag','EditText6'),'Visible','on','BackgroundColor',[1 1 1]);
    set(findobj(gcf,'Tag','EditText7'),'Visible','on','BackgroundColor',[1 1 1]);
end
% --------------------------------------------------------------------
function varargout = EditText7_Callback(h, eventdata, handles, varargin)

valeur=str2num(get(findobj(gcf,'Tag','EditText7'),'String'));
set(findobj(gcf,'Tag','EditText7'),'Value',valeur);
Value=get(findobj(gcf,'Tag','PopupMenu1'),'Value');
if Value==5
    set(findobj(gcf,'Tag','EditText1'),'Visible','on','BackgroundColor',[.8 .8 .8]);
    set(findobj(gcf,'Tag','EditText2'),'Visible','on','BackgroundColor',[.8 .8 .8]);
    set(findobj(gcf,'Tag','EditText6'),'Visible','on','BackgroundColor',[1 1 1]);
    set(findobj(gcf,'Tag','EditText7'),'Visible','on','BackgroundColor',[1 1 1]);
end




% --------------------------------------------------------------------
function varargout = PushButton6_Callback(h, eventdata, handles, varargin)

out=PSDFitting;
xg=out(1);
sg=out(2);
if imag(xg)~=0|imag(sg)~=0
    warn=sprintf('Warning:  Optimization containing imaginary parts. \n Imaginary parts of complex arguments ignored')
    h=warndlg(warn,'Optimization Unsuccessful')
    uiwait(h)
    xg=real(out(1))
    sg=real(out(2))
end
        set(findobj(gcf,'Tag','EditText1'),'String',num2str(xg));
        set(findobj(gcf,'Tag','EditText2'),'String',num2str(sg));
        set(findobj(gcf,'Tag','EditText1'),'Value',xg);
        set(findobj(gcf,'Tag','EditText2'),'Value',sg);
        
Value=get(findobj(gcf,'Tag','PopupMenu1'),'Value')

if Value==5
    xbar=xg*exp(1/2*log(sg)^2);
    sbar=sqrt((exp(log(sg)^2)-1)*(xg^2*exp(log(sg)^2)));
    set(findobj(gcf,'Tag','EditText6'),'String',num2str(xbar));
    set(findobj(gcf,'Tag','EditText7'),'String',num2str(sbar));
    set(findobj(gcf,'Tag','EditText6'),'Value',xbar);
    set(findobj(gcf,'Tag','EditText7'),'Value',sbar);
end

global fig1 axehdl fich
figure(fig1)
k=get(findobj(gcf,'Tag','EditText1'),'Value');
n=get(findobj(gcf,'Tag','EditText2'),'Value');
deb=get(findobj(gcf,'Tag','EditText3'),'Value');
fin=get(findobj(gcf,'Tag','EditText4'),'Value');
inter=get(findobj(gcf,'Tag','EditText5'),'Value');
Value=get(findobj(gcf,'Tag','PopupMenu1'),'Value');
Vlog=get(findobj(gcf,'Tag','Checkbox1'),'Value');
Vgrid=get(findobj(gcf,'Tag','Checkbox2'),'Value');



set(gcf,'CurrentAxes',axehdl)
hold off;

x=deb:inter:fin;
if Value == 1,
    y=(x.^n/k^n)*100;
elseif Value == 2,
    y=(1-(1-x/k).^n)*100;
elseif Value == 3,
    y=erf(log(x./k)/n)*100;
elseif Value == 4,
    y=(1-exp(-(x.^n/k^n)))*100;
elseif Value == 5,
    y=1/2*(1+erf(log(x/xg)/(sqrt(2)*log(sg))))*100;
end,

if Vlog ==1,
    semilogx(x,y,'Parent',axehdl);
else,
    plot(x,y,'Parent',axehdl);
end,

try,
    taille=size(fich,1);
    if taille ~= 0,
        x=fich(:,1);
        y=fich(:,2);
        hold on;
        plot(x,y,'r+')
        ,if Value == 1,
            y2=(x.^n/k^n)*100;
        elseif Value == 2,
            y2=(1-(1-x/k).^n)*100;
        elseif Value == 3,
            y2=erf(log(x./k)/n)*100;
        elseif Value == 4,
            y2=(1-exp(-(x.^n/k^n)))*100;
        elseif Value == 5,
            y2=1/2*(1+erf(log(x/xg)/(sqrt(2)*log(sg))))*100;
        end,
        erreur=(y-y2).^2;
        somerr=sum(erreur);
        set(findobj(gcf,'Tag','EditText20'),'String',somerr);
        Vspline=get(findobj(gcf,'Tag','Checkbox3'),'Value');
        
        if Vspline ==1,xx=deb:inter:fin;
            yy=INTERP1(x,y,xx,'cubic');
            plot(xx,yy,'r-'),
        end,
    end,
catch,
end,

if Vgrid ==1,
    grid on;
else,
    
    grid off;
end,

axis([deb fin 0 100]);
xlabel('Particle Diameter (microns)'),
ylabel('Cumulative Mass (%)'),
hold off;


% --- Executes during object creation, after setting all properties.
function EditText12_CreateFcn(hObject, eventdata, handles)
% hObject    handle to EditText12 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes during object creation, after setting all properties.
function EditText13_CreateFcn(hObject, eventdata, handles)
% hObject    handle to EditText13 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end

% --- Executes during object creation, after setting all properties.
function EditText16_CreateFcn(hObject, eventdata, handles)
% hObject    handle to EditText16 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end





function EditText17_Callback(hObject, eventdata, handles)
% hObject    handle to EditText17 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of EditText17 as text
%        str2double(get(hObject,'String')) returns contents of EditText17 as a double


% --- Executes during object creation, after setting all properties.
% function EditText17_CreateFcn(hObject, eventdata, handles)
% % hObject    handle to EditText17 (see GCBO)
% % eventdata  reserved - to be defined in a future version of MATLAB
% % handles    empty - handles not created until after all CreateFcns called
% 
% % Hint: edit controls usually have a white background on Windows.
% %       See ISPC and COMPUTER.
% if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
%     set(hObject,'BackgroundColor','white');
% end




% --- Executes during object creation, after setting all properties.
%function EditText17_CreateFcn(hObject, eventdata, handles)
% hObject    handle to EditText17 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
% %       See ISPC and COMPUTER.
% if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
%     set(hObject,'BackgroundColor','white');
% end




% --- Executes during object creation, after setting all properties.
function EditText17_CreateFcn(hObject, eventdata, handles)
% hObject    handle to EditText17 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end





function edit7_Callback(hObject, eventdata, handles)
% hObject    handle to edit7 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit7 as text
%        str2double(get(hObject,'String')) returns contents of edit7 as a double


% --- Executes during object creation, after setting all properties.
function edit7_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit7 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function edit8_Callback(hObject, eventdata, handles)
% hObject    handle to edit8 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit8 as text
%        str2double(get(hObject,'String')) returns contents of edit8 as a double


% --- Executes during object creation, after setting all properties.
function edit8_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit8 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function edit9_Callback(hObject, eventdata, handles)
% hObject    handle to edit9 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit9 as text
%        str2double(get(hObject,'String')) returns contents of edit9 as a double


% --- Executes during object creation, after setting all properties.
function edit9_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit9 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function edit10_Callback(hObject, eventdata, handles)
% hObject    handle to edit10 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit10 as text
%        str2double(get(hObject,'String')) returns contents of edit10 as a double


% --- Executes during object creation, after setting all properties.
function edit10_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit10 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


