function varargout = Subgrid(varargin)

% SUBGRID M-file for Subgrid.fig
%      SUBGRID, by itself, creates a new SUBGRID or raises the existing
%      singleton*.
%
%      H = SUBGRID returns the handle to a new SUBGRID or the handle to
%      the existing singleton*.
%
%      SUBGRID('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in SUBGRID.M with the given input arguments.
%
%      SUBGRID('Property','Value',...) creates a new SUBGRID or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before Subgrid_OpeningFunction gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to Subgrid_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help Subgrid

% Last Modified by GUIDE v2.5 22-Jun-2010 12:49:33


if nargin == 0  % LAUNCH GUI

    fig = openfig(mfilename,'new');
    pg={};
    global fig2;
    global fig1;
    global fich;
    global fig3;
    global pg;
    fig3=gcf;
    

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

% Begin initialization code - DO NOT EDIT

gui_Singleton = 0;
gui_State = struct('gui_Name',       mfilename, ...
    'gui_Singleton',  gui_Singleton, ...
    'gui_OpeningFcn', @Subgrid_OpeningFcn, ...
    'gui_OutputFcn',  @Subgrid_OutputFcn, ...
    'gui_LayoutFcn',  [] , ...
    'gui_Callback',   []);
if nargin & isstr(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end



% --- Executes just before Subgrid is made visible.
function Subgrid_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to Subgrid (see VARARGIN)


% Choose default command line output for Subgrid
handles.output = hObject;
% clear global
% global fig1
% global pg
% 
% 
% fig1=hObject;
% % Update handles structure
guidata(hObject, handles);

% UIWAIT makes Subgrid wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = Subgrid_OutputFcn(hObject, eventdata, handles)
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes during object creation, after setting all properties.
function listbox1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to listbox1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: listbox controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc
    set(hObject,'BackgroundColor','white');
else
    set(hObject,'BackgroundColor',get(0,'defaultUicontrolBackgroundColor'));
end


% --- Executes on selection change in listbox1.
function listbox1_Callback(hObject, eventdata, handles)
% hObject    handle to listbox1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = get(hObject,'String') returns listbox1 contents as cell array
%        contents{get(hObject,'Value')} returns selected item from listbox1


% --- Executes on button press in pushbutton1.
function varargout = pushbutton1_Callback(h, eventdata, handles, varargin)
% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global pg
global fig3
global fig2
global infoarray
if size(pg,1)==0
    pg =cell(1, 1);
    d=0;
else
    d=size(pg,1);
end

%[FILES, PATHNAMES] = uigetfiles('*.*','Open Files'); OLD VERSION
%
%Multiple Selection in uigetfile in R14
%The uigetfile function can now create a dialog that enables the user to select and retrieve multiple files using the Shift and Ctrl keys. You can turn this capability on or off using the new 'MultiSelect' parameter. The default setting is off

[FILES, PATHNAMES,FilterIndex] = uigetfile({'*.pg1;*.pg2;*.pg3;*.pg4;*.pg5;*.pg6;*.pg7;*.pg8;*.pg9','PG files (*.pg*)'; ...
'*.*',  'All Files (*.*)'}, ...
'Pick PG files', ...
'MultiSelect', 'on');

if iscell(FILES),
else
    FFILES=FILES;
    clear FILES;
    FILES=cell(1,1);
    FILES(1)=cellstr(FFILES);
end

FILES=FILES
for i=1:size(FILES,2)
    pg(d+i,1)={PATHNAMES};
    pg(d+i,2)=FILES(i);
end
set(findobj(gcf,'Tag','listbox1'),'String',pg(:,2));

clear temp;
n=0;
p=1;
size(pg,1);
for i=1:size(pg,1)
    if pg{i,1}==0
        figure(fig2)
        nbsize=str2num(get(findobj(gcf,'Tag','EditText1'),'String'));
        for i = 5:nbsize+4
            nbr=strcat('EditText',num2str(i));
            dia=strcat('EditText',num2str(i+45));
            temp(i-4,1)=1;
            temp(i-4,2)=str2num(get(findobj(gcf,'Tag',nbr),'String'));
            temp(i-4,3)=str2num(get(findobj(gcf,'Tag',dia),'String'))*10^-6*(1/2);
        end
        info=temp;
        clear temp
        m=size(info,1); 
        figure(fig3)
        for k=1:m
            temp(k+n,1)=p;  %particle type
            temp(k+n,2)=info(k,2); %number of particle
            temp(k+n,3)=info(k,3) ; %large axis
        end
        n=n+k;
        clear info
        p=p+1;
        
    else
        filename=[pg{i,1} pg{i,2}];
        info= dlmread(filename);    %info= DLMREAD(filename,' ',1, 0)
        if size(info,1)>2
            m=size(info,1)-2;
        else
            m=size(info,1)-1;
        end
        for k=1:m
            temp(k+n,1)=p;  %particle type
            temp(k+n,2)=info(k+1,2); %number of particle
            temp(k+n,3)=info(k+1,3) ; %large axis
        end
        n=n+k;
        clear info
        p=p+1;
    end
end

[Y,S] = sort(temp(:,3));
stringlist =cell(1, 1);
stringlist(1,1)={'Large Axis(µm)      Qty'};
infoarray=zeros(size(S,1),3);
for i=1:size(S,1)
    infoarray(i,:)=temp(S(i),:);
    a=num2str(2*infoarray(i,3)*1000000);
    b=num2str(infoarray(i,2));
    stringlist(i+1,1)={sprintf('%6.3f                   %6.0f', infoarray(i,3)*1000000, infoarray(i,2))};
end

set(findobj(gcf,'Tag','listbox2'),'String',stringlist);
% --- Executes during object creation, after setting all properties.
function edit1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc
    set(hObject,'BackgroundColor','white');
else
    set(hObject,'BackgroundColor',get(0,'defaultUicontrolBackgroundColor'));
end



function edit1_Callback(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit1 as text
%        str2double(get(hObject,'String')) returns contents of edit1 as a double


% --- Executes during object creation, after setting all properties.
function edit2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc
    set(hObject,'BackgroundColor','white');
else
    set(hObject,'BackgroundColor',get(0,'defaultUicontrolBackgroundColor'));
end



function edit2_Callback(hObject, eventdata, handles)
% hObject    handle to edit2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit2 as text
%        str2double(get(hObject,'String')) returns contents of edit2 as a double


% --- Executes during object creation, after setting all properties.
function edit3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc
    set(hObject,'BackgroundColor','white');
else
    set(hObject,'BackgroundColor',get(0,'defaultUicontrolBackgroundColor'));
end



function edit3_Callback(hObject, eventdata, handles)
% hObject    handle to edit3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit3 as text
%        str2double(get(hObject,'String')) returns contents of edit3 as a double

% --- Executes during object creation, after setting all properties.
function edit4_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc
    set(hObject,'BackgroundColor','white');
else
    set(hObject,'BackgroundColor',get(0,'defaultUicontrolBackgroundColor'));
end



function edit4_Callback(hObject, eventdata, handles)
% hObject    handle to edit4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit4 as text
%        str2double(get(hObject,'String')) returns contents of edit4 as a double


% --- Executes during object creation, after setting all properties.
function listbox2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to listbox2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: listbox controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc
    set(hObject,'BackgroundColor','white');
else
    set(hObject,'BackgroundColor',get(0,'defaultUicontrolBackgroundColor'));
end


% --- Executes on selection change in listbox2.
function listbox2_Callback(hObject, eventdata, handles)
% hObject    handle to listbox2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = get(hObject,'String') returns listbox2 contents as cell array
%        contents{get(hObject,'Value')} returns selected item from listbox2


% --- Executes during object creation, after setting all properties.
function edit5_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc
    set(hObject,'BackgroundColor','white');
else
    set(hObject,'BackgroundColor',get(0,'defaultUicontrolBackgroundColor'));
end



function edit5_Callback(hObject, eventdata, handles)
% hObject    handle to edit5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit5 as text
%        str2double(get(hObject,'String')) returns contents of edit5 as a double


% --- Executes during object creation, after setting all properties.
function edit6_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit6 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc
    set(hObject,'BackgroundColor','white');
else
    set(hObject,'BackgroundColor',get(0,'defaultUicontrolBackgroundColor'));
end



function edit6_Callback(hObject, eventdata, handles)
% hObject    handle to edit6 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit6 as text
%        str2double(get(hObject,'String')) returns contents of edit6 as a double


% --- Executes on button press in pushbutton2.
function varargout = pushbutton2_Callback(h, eventdata, handles, varargin)
% hObject    handle to pushbutton2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global infoarray;
global fig1;
global fig2;
global fig3;

%Obtain input values
figure(fig1)
rho=get(findobj(gcf,'Tag','EditText12'),'Value');

figure(fig2)
area=str2num(get(findobj(gcf,'Tag','EditText4'),'String'));
cw=str2num(get(findobj(gcf,'Tag','EditText3'),'String'));
% nbsize=str2num(get(findobj(gcf,'Tag','EditText1'),'String'));
% for i = 5:nbsize+4
%     nbr=strcat('EditText',num2str(i));
%     dia=strcat('EditText',num2str(i+45));
%     infoarray(i-4,1)=1;
%     infoarray(i-4,2)=str2num(get(findobj(gcf,'Tag',nbr),'String'));
%     infoarray(i-4,3)=str2num(get(findobj(gcf,'Tag',dia),'String'))*10^-6;
% end

figure(fig3)
sol_frac=str2num(get(findobj(gcf,'Tag','edit2'),'String'))/100;
if sol_frac == 0 
    sol_frac = 70;
    set(findobj(gcf,'Tag','edit2'),'String',num2str(sol_frac));
end

vol_frac = sol_frac*1000/(((1-sol_frac)*rho)+(sol_frac*1000));
poro =(1-vol_frac)*100;
t = cw*1000/(rho*vol_frac);
vol=t*area/((1E6)^3);

set(findobj(gcf,'Tag','edit11'),'String',num2str(poro));
set(findobj(gcf,'Tag','edit10'),'String',num2str(t));

total=sum(infoarray(:,2));
vol=(t*area/((1E6)^3));
part_density=total/vol;

%Initialize arrays for calculations
nbgrosses=zeros(size(infoarray(:,2),1),1);
nbcase=zeros(size(infoarray(:,2),1),1);


nbgrosses(size(infoarray(:,2),1),1)=infoarray(size(infoarray(:,2),1),2);
for i=size(infoarray(:,2),1)-1:-1:1
    nbgrosses(i,1)=nbgrosses(i+1,1)+infoarray(i,2);
end

temp=(2*infoarray(:,3)).^3;  %N column   =(2*E2)^3*$E$25
nbcase=temp.*part_density;
clear temp
temp=27*nbcase;
temp2=temp+nbgrosses;

for i=1:size(temp2,1)
averifier(i,1)=(temp2(i,1)*(total-nbgrosses(i))+nbgrosses(i)*total)/total;
end

Rmax=infoarray(size(infoarray,1),3);
plot(infoarray(:,3).*1E6*2,averifier(:,1),'s-b');
 if max(averifier(:,1))>20000
     axis([0 Rmax*2E6 0 20000]) ;
end
xlabel('Grid size (µm)');
ylabel('Average Number of possible collisions');
hold on;
pos=find(averifier(:,1)==min(averifier(:,1)));
Dmin=infoarray(pos,3)*2;

W=sqrt(area)*1E-6;
mult=floor(W/Dmin);
grid=W/mult;

N=spline(infoarray(:,3),averifier(:,1),grid/2);

plot(grid*1E6,N,'-mo',...
                'LineWidth',2,...
                'MarkerEdgeColor','r',...
                'MarkerFaceColor','r',...
                'MarkerSize',6)
hold off;

set(findobj(gcf,'Tag','edit13'),'String',num2str(grid*1E6));
pos=find(infoarray(:,3)>=grid/2);
Nlarge=sum(infoarray(pos(:),2));
set(findobj(gcf,'Tag','edit14'),'String',num2str(Nlarge));


% --- Executes during object creation, after setting all properties.
function edit8_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit8 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc
    set(hObject,'BackgroundColor','white');
else
    set(hObject,'BackgroundColor',get(0,'defaultUicontrolBackgroundColor'));
end



function edit8_Callback(hObject, eventdata, handles)
% hObject    handle to edit8 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit8 as text
%        str2double(get(hObject,'String')) returns contents of edit8 as a double


% --- Executes on button press in pushbutton3.
function varargout = pushbutton3_Callback(h, eventdata, handles, varargin)
% hObject    handle to pushbutton3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

global pg
global fig1
if size(pg,1)==0
    
else
    
    index_selected = get(findobj(gcf,'Tag','listbox1'),'Value');
    pg(index_selected,:)=[];
    set(findobj(gcf,'Tag','listbox1'),'String',pg(:,2));
    
    clear temp;
    n=0;
    p=1;
    if size(pg,1)>0
        for i=1:size(pg,1)
            filename=[pg{i,1} pg{i,2}];
            info= DLMREAD(filename,' ',1, 0);
            
            if size(info,1)>1
                m=size(info,1)-1;
            else
                m=size(info,1);
            end
            
            for k=1:m
                temp(k+n,1)=p;  %particle type
                temp(k+n,2)=info(k,2);  %number of particle
                temp(k+n,3)=info(k,3);  %large axis
            end
            n=n+k;
            clear info
            p=p+1;
        end
        
        [Y,S] = sort(temp(:,3));
        stringlist =cell(1, 1);
        stringlist(1,1)={'Large Axis(µm)    Qty'};
        infoarray=zeros(size(S,1),3);
        for i=1:size(S,1)
            infoarray(i,:)=temp(S(i),:);
            a=num2str(2*infoarray(i,3)*1000000);
            b=num2str(infoarray(i,2));
            stringlist(i+1,1)={sprintf('%6.3f               %6.3f', infoarray(i,3)*1000000, infoarray(i,2))};
        end
        set(findobj(gcf,'Tag','listbox2'),'String',stringlist);
    else
        clear stringlist
        set(findobj(gcf,'Tag','listbox2'),'String','');
    end
end
set(findobj(gcf,'Tag','listbox1'),'Value',1);


% --- Executes during object creation, after setting all properties.
function edit9_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit9 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc
    set(hObject,'BackgroundColor','white');
else
    set(hObject,'BackgroundColor',get(0,'defaultUicontrolBackgroundColor'));
end



function edit9_Callback(hObject, eventdata, handles)
% hObject    handle to edit9 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit9 as text
%        str2double(get(hObject,'String')) returns contents of edit9 as a double





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



function edit11_Callback(hObject, eventdata, handles)
% hObject    handle to edit11 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit11 as text
%        str2double(get(hObject,'String')) returns contents of edit11 as a double


% --- Executes during object creation, after setting all properties.
function edit11_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit11 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in pushbutton4.
function varargout = pushbutton4_Callback(h, eventdata, handles, varargin)
% hObject    handle to pushbutton4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global fig2
global fig3
global fig1
global pg
global infoarray
if size(pg,1)==0
    pg =cell(1, 1);
    d=0;
else
    d=size(pg,1);
end

%[FILES, PATHNAMES] = uigetfiles('*.*','Open Files'); OLD VERSION
%
%Multiple Selection in uigetfile in R14
%The uigetfile function can now create a dialog that enables the user to select and retrieve multiple files using the Shift and Ctrl keys. You can turn this capability on or off using the new 'MultiSelect' parameter. The default setting is off

% [FILES, PATHNAMES,FilterIndex] = uigetfile({'*.pg1;*.pg2;*.pg3;*.pg4;*.pg5;*.pg6;*.pg7;*.pg8;*.pg9','PG files (*.pg*)'; ...
% '*.*',  'All Files (*.*)'}, ...
% 'Pick PG files', ...
% 'MultiSelect', 'on');

FILES='Discretization';

if iscell(FILES),
else
    FFILES=FILES;
    clear FILES;
    FILES=cell(1,1);
    FILES(1)=cellstr(FFILES);
end

FILES=FILES
for i=1:size(FILES,2)
    pg(d+i,1)={0};
    pg(d+i,2)=FILES(i);
end
set(findobj(gcf,'Tag','listbox1'),'String',pg(:,2));

figure(fig2)
nbsize=str2num(get(findobj(gcf,'Tag','EditText1'),'String'));
for i = 5:nbsize+4
    nbr=strcat('EditText',num2str(i));
    dia=strcat('EditText',num2str(i+45));
    temp(i-4,1)=1;
    temp(i-4,2)=str2num(get(findobj(gcf,'Tag',nbr),'String'));
    temp(i-4,3)=str2num(get(findobj(gcf,'Tag',dia),'String'))*10^-6*(1/2);
end

discr=temp;
clear temp;
n=0;
p=1;
size(pg,1);
for i=1:size(pg,1)
    if pg{i,1} == 0
        info=discr;
        m=size(info,1);
        for k=1:m
            temp(k+n,1)=p;  %particle type
            temp(k+n,2)=info(k,2); %number of particle
            temp(k+n,3)=info(k,3) ; %large axis
        end
        n=n+k;
        clear info
        p=p+1;
    else
        filename=[pg{i,1} pg{i,2}];
        info= dlmread(filename);    %info= DLMREAD(filename,' ',1, 0)
        if size(info,1)>2
            m=size(info,1)-2;
        else
            m=size(info,1)-1;
        end
        for k=1:m
            temp(k+n,1)=p;  %particle type
            temp(k+n,2)=info(k+1,2); %number of particle
            temp(k+n,3)=info(k+1,3) ; %large axis
        end
        n=n+k;
        clear info
        p=p+1;
    end    
end

figure(fig3)
[Y,S] = sort(temp(:,3));
stringlist =cell(1, 1);
stringlist(1,1)={'Large Axis(µm)      Qty'};
infoarray=zeros(size(S,1),3);
for i=1:size(S,1)
    infoarray(i,:)=temp(S(i),:);
    a=num2str(2*infoarray(i,3)*1000000);
    b=num2str(infoarray(i,2));
    stringlist(i+1,1)={sprintf('%6.3f                   %6.0f', infoarray(i,3)*1000000, infoarray(i,2))};
end

set(findobj(gcf,'Tag','listbox2'),'String',stringlist);



function edit13_Callback(hObject, eventdata, handles)
% hObject    handle to edit13 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit13 as text
%        str2double(get(hObject,'String')) returns contents of edit13 as a double


% --- Executes during object creation, after setting all properties.
function edit13_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit13 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function edit14_Callback(hObject, eventdata, handles)
% hObject    handle to edit14 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit14 as text
%        str2double(get(hObject,'String')) returns contents of edit14 as a double


% --- Executes during object creation, after setting all properties.
function edit14_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit14 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


