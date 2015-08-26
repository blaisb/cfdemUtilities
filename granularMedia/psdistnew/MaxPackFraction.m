% -------------------------------------------------------------------------
%              Program: Max Pack Fraction
%              Programmed by Hicham Khelladi and David Vidal
%              Finalized on July 4th, 2014
%             --------------------------------
% This program can predict the maximal packing fraction you can get with a
% packing (following a model, or a discretization)
% Models are defined in psdist2 

% ---------------------------! IMPORTANT !---------------------------------
% You HAVE to put this m.file (MaxPackFraction) along with MaxPackalgobin and
% MassToNumbDist in the psdist2 file ! 
%          ------------------------------------------

%------------------------------------------------------------------------
%Algorithm is based on the following article:
% Robert S. Farr and Robert D. Groot
% Close Packing Density of Polydisperse Hard Spheres (December 4th, 2009)
% of hard spheres (2013)

%------------------------------------------------------------------------

%Ask for the rod number
prompt = {'Enter the number of rods for the algorithm'};
dlg_title = 'Input for algorithm precision';
num_lines = 1;
def = {'2000'};
answer = inputdlg(prompt,dlg_title,num_lines,def);

NbSiRod=str2num(answer{1}); % Number of rod size to use
%-------------------------------------------

%NbSiRod=2000; %Number of rod size to use 
NbPop=20; % Number of particle size to use from a model

NbPart=NbSiRod; %Total number of rod to spread among the distribution (if model used)
f=0.7654; %Free volume parameter: Adjusting factor for greedy algorithm

wait=waitbar(0,'Calculating...')%,'WindowStyle','modal','CreateCancelBtn','setappdata(gcbf,''canceling'',1)')
%setappdata(wait,'canceling',0);

%suggested values min and max for discretization
themin=5e-3;
themax=0.5;
%--------
%Switchmode: put value 1 to try bidispere, 2 for mass weighted distribution
% and 3 for regular / 4 for manual values
switchmode=3;
%n.b: all modes (except 3) require manual change in the code

l=zeros(1,NbPart); % Since we discretize, the diameter value correspond to the L value
p=zeros(1,NbPart); %Probability of rod size

%Fig with different models and plot:1
%Fig with discretization:2

% DistType=0; %
% DistType=get(findobj(figure(2),'Tag','PopupMenu1'),'Value');
% if DistType==1
%     DistType='Model';
% elseif DistType==2
%     DistType='Data fitting';
% else  % that means the "discretization" window was not opened, it can only be the model
%     DistType='Model'
%     disp('________________IMPORTANT__________________________________')
%     disp('Discretization window not opened: will calculate using the model !')
%     disp('___________________________________________________________')
%     %disp ('Open the discretization box to choose "model" or "data fitting"')
% end

DistType='Data fitting';
fprintf('\nNumber of rods to calculate: %u\n',NbSiRod)

        disp ('Calculating with: ''Data fitting''')
        %Initialize matrix size with number of size
        
        % --------------------REMOVED FOR TEST-----------------
        Ntot=str2num(get(findobj(figure(2),'Tag','EditText1'),'String')); %Number of sizes
        d=zeros(1,Ntot); % Particle diameters
        a=zeros(1,Ntot); %Particle size respective probability in number 
        numUnsort=zeros(1,Ntot); % Particle respective number ( num(i)) particle of diameter d(i)
        num=zeros(1,Ntot); %Same as numUnsort, but used after we put
        %diameters in order

        
        
        %Read the values
        for i=1:Ntot
            d(i)=str2num(get(findobj(figure(2),'Tag',[ 'EditText' num2str(i+49) ] ),'String'));
            numUnsort(i)=str2num(get(findobj(figure(2),'Tag',[ 'EditText' num2str(i+4) ] ),'String'));
        end
%         
        %------------ UNTIL HERE---------------------------

        %Maximal and minimal diameter taken as the extreme value (infinite
        %and zero) for the distribution integration
        
        
 % --------------------
        if switchmode==4
            
        d=0.5*[0.002:0.00025:0.004];
        ac=(0.2/0.94)*[0.02 0.1 0.4 1.05 2.25 3.3 4.2 4.5 0.94/0.2];
        a=zeros(1,length(d));
        a(1)=ac(1);
        for i=2:length(d)
            a(i)=ac(i)-ac(i-1);
        end
        end
        disp(sum(a))
 %-------------------------------------------------------------------
        % FOR BIDISPERSE TEST USING THE RESULT TABLE OF ORIGINAL ALGORITHM
        
        if switchmode==1
        Y2=0.2;%D2/D1
        w=0.8;
        
        Y=1/Y2;
        d=[5 Y2*1];
         
        [d,index]=sort(d,'ascend');
        
        a=zeros(1,length(index));
        a2=[w/(Y^3-w*(Y^3-1)) 1-w/(Y^3-w*(Y^3-1))];
        for i=1:length(d)
            a(i)=a2(index(i));
        end
        
        end

%---------------------------------------------------------------
        
        %CASE WITH MASS FRACTION (enter matrix manually)
        if switchmode==2
        d=[2.605 2.19 1.84 1.545 1.3];
        w=0.01*[15.1 36.6 32.3 15.1 0.9];
        a2=MassToNumbDist(d,w); %Created function (a2: number fraction)
        
        a=zeros(1,length(d));
        [d,index]=sort(d,'ascend');
        for i=1:length(d)
            a(i)=a2(index(i));
        end
        
        end
        
        %----------------------------------------------------------

        
        % ---------- REGULAR CASE HERE -----------------
        if switchmode==3
        
        %small algorithm to sort the particles and their number
        %(num and numUnsort)
        [d,index]=sort(d,'ascend');
        num=zeros(1,length(numUnsort));
        for i=1:length(num)
            num(i)=numUnsort(index(i));
        end
        SumNum=sum(num); %Number of particles
        a=num/SumNum; %Probability in number per respective diameter
        end
        
  %-------------------------------------------------------------
        
        Vave=sum(a.*d.^3)*pi/6;
        botequa=0;
        dmax = d(end); 
        dmin= d(1);
        
        % We start the algorithm here, the first value of l, dmax, is not
        % considered as a rod, but is used to initiate
        l(1)=dmax;
        p(1)=0;
                %Integral from Ln to infinite gives 1/(2N), while from Ln-1 to Ln it gives 1/N
                %Thus we initiate manually the first value, then use the
                %loop
                
        count=2;
        
        [l(count),p(count)]=MaxPackalgobin(2*(NbPart),dmin,dmax,DistType,l(count-1),p(count-1),NbPart,0,0,Vave,a,d);
        count=3;
        %there we calculate all the rods
        for i=NbPart-1:-1:1

            waitbar(count/NbPart); %loading progression
            %In this data fitting case, argument "i" will be used to count
            %(2N-2i+1)/2N
            [l(count),p(count)]=MaxPackalgobin((NbPart),dmin,dmax,DistType,l(count-1),p(count-1),i,0,0,Vave,a,d);
            count=count+1;
        end
        %[l(count),p(count)]=MaxPackalgobin(2*(NbPart),dmin,dmax,DistType,l(count-1),p(count-1),0,0,0,Vave,a,d);
%         for i=1:NbPart-1
%             ii=i
%             [l(i+1),p(i+1)]=MaxPackalgobin(NbPart,dmin,dmax,DistType,l(i),p(i),i+1,0,0,Vave,a,d);
%         end
            

%----------------- Rod creation based from models only ------------------
if strcmp(DistType,'Model')==1
    
    a=MassToNumbDist(d,w);
    if (sum(a)<0.999)
        disp('WARNING: results may not be accurate because dmax is not big enough for this distribution (not 100% cumulative probability)')
    end %does not work yet ...
                
    a=a./sum(a); %adjust the sum of fraction to one, in case dmax is not at 100% cumul. prob. exactly

    Vave=sum(a.*d.^3)*pi/6;
    botequa=0;

        
    l(1)=dmax;
    p(1)=0;
    %Integral from Ln to infinite gives 1/(2N), while from Ln-1 to Ln it gives 1/N
    %Thus we initiate manually the first value, then use the
    %loop
                
    count=2;
        
    [l(count),p(count)]=MaxPackalgobin(2*(NbPart),dmin,dmax,'Data fitting',l(count-1),p(count-1),NbPart,0,0,Vave,a,d);
    count=3;
    for i=NbPart-1:-1:1

        wait=waitbar(count/NbPart);
        %In this data fitting case, argument "i" will be used to solve
        %(2N-2i+1)/2N
        [l(count),p(count)]=MaxPackalgobin((NbPart),dmin,dmax,'Data fitting',l(count-1),p(count-1),i,0,0,Vave,a,d);
        count=count+1;
    end
    
end 
%-------------------------- End of Rod creation -----------------------

% End of the equations, we then calculate the rod probability and can start
% the greedy algorithm

%In case of discrete, the "L" value are the same than the D values
%In case of continuous, we already defined NbSiRod different size or
%possible rod
%We consider the probability of having a rod the largest possible size
%(biggest particle diameter)
% for i=1:length(topequa) 
%     pl(i)=2*l(i)*topequa(i)/botequa;
% end
%Check that sum(pl)=1
% disp (sum(pl))

% Rod creation using the length probability
% rodunsort=zeros(length(l))
% rodunsort=NbRod*pl % total number of particle* probability of length L = rod number of length L

% Ordering algorithm (ALREADY DONE WITH NEW METHOD)
% rod=sort(rodunsort,'descend')
% Gaps matrix (size of number of rod inserted, but we create the maximal size)
gaps=zeros(1,length(l)-1);
lambda=0; %Total length containing rods and gaps, will increase with greedy algorithm
addgaps=1; % increment to add a new gap into the full sized matrix, will be incremented after adding a new gap
gmax=0;
    gaps(1)=f*l(2); %first gap
    rodnum=1; % Identifier to know the "real" size of the matrix, excluding the 0 created for the max size
for i=3:length(l)

    [gmax,gmaxpo]=max(gaps); %Identify the biggest gap (gmax) and its position in matrix gaps
    gaps(gmaxpo)=f*l(i); %remove the biggest gap and replace by f*L
    choice(1)=(gmax-(1+f)*l(i));
    choice(2)=f*l(i);
    gaps(rodnum+1)=max(choice); % the second gap created
    rodnum=rodnum+1; %Increment before looping again !
end

%We can now simply calculate the void fraction !
MaxFraction=(sum(sum(l))/(sum(sum(l))+sum(sum(gaps))));

if strcmp(DistType,'Data fitting')==1
    method='Data fitting';
else
    method=ModName;
end
fprintf('--------------------- Results -----------------------------\n')
fprintf('Calculated for %u sizes with %s\n',NbPart,method)
fprintf('Maximal Packing Fraction = %1.6g\n',MaxFraction)
fprintf('\n-------------- End of program MaxPackFraction -----------\n')

set(findobj(gcf,'Tag','edit304'),'String',num2str(MaxFraction));
delete(wait); %End of the waiting bar



% ----------- TESTING TOOLS, USELESS FOR SOFTWARE -------------------
% if dmax~=dmin
%     ww=a(end)*dmax^3/(a(1)*dmin^3+a(end)*dmax^3);
%     packmax=min([0.6435/(1-ww*(1-0.6435)),0.6435/ww])
% end
mistake=0;
deltac=(l(1)-l(end))/(NbPart-1);
ptot=0;
pmat=zeros(NbPart-1,1);

for i=1:length(l)-1
    pmat(i)=(l(i)-l(i+1))*(p(i)+p(i+1))/2;
    
    if (l(i+1)-l(i))>0
        mistake=mistake+1;
        errorvalue(mistake)=i;
    end
end
prob=sum(pmat);
if mistake>0
    fprintf('--------WARNING-------\n')
    fprintf('Beware, there is %d rods with wrong size\n',mistake)
    fprintf('----------------------\n')
end
ptot=sum(pmat);
        
% ----------------------- End of Testing tools -------------------------