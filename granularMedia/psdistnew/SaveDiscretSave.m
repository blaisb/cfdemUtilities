%try,
Vsplit=get(findobj(gcf,'Tag','Checkbox1'),'Value');
nbsim=str2num(get(findobj(gcf,'Tag','EditText2'),'String'));
fich1=get(findobj(gcf,'Tag','EditText1'),'String');
currentfig=gcf;
global fig2;
global fig1

figure(fig1)
rho=str2num(get(findobj(gcf,'Tag','EditText12'),'String'));
if isempty(rho)
    rho=get(findobj(gcf,'Tag','EditText12'),'Value');
end

figure(fig2);
nbps=str2num(get(findobj(gcf,'Tag','EditText1'),'String'));
Vang=get(findobj(gcf,'Tag','checkbox2'),'Value');
if Vang~=0
    angdist=1;
    angdev=str2num(get(findobj(gcf,'Tag','EditText142'),'String'));
else 
    angdist=0;
    angdev=0;
end
%   figure(currentfig);
%   nbps=str2num(nbps);
%   nbsim=str2num(nbsim);
clear nd;

Vshape=get(findobj(gcf,'Tag','PopupMenu2'),'Value');
if Vshape==1
    Vparam=1;
    shape=1; %sphere
elseif Vshape==2|Vshape==3
    Vparam=get(findobj(gcf,'Tag','PopupMenu3'),'Value');
    shape=2; %ellipsoid
end
if Vsplit == 1,
    grosse=zeros(nbsim,1);
    matrest=zeros(nbps,nbsim);
    for i = 1:nbps,
        VBox = strcat('EditText', num2str(i+4));
        nbpart(i)=str2num(get(findobj(gcf,'Tag',VBox),'String'));
        rest(i)=nbpart(i)-floor(nbpart(i)/nbsim)*nbsim;
        for j=1:rest(i),
            done=0;
            if i==nbps | i==(nbps-1)
                while done==0 
                    sim=floor(rand*nbsim)+1;
                    if grosse(sim,1) ~= 1 | grosse(:,1)==1
                        done=1;
                    end
                end
                matrest(i,sim)=matrest(i,sim)+1;
                grosse(sim,1)=1;
            else
                sim=floor(rand*nbsim)+1;
                matrest(i,sim)=matrest(i,sim)+1;
            end
            
        end
        VBox = strcat('EditText', num2str(i+49));
        VBox2= strcat('EditText', num2str(i+94));
        if Vshape==1
            %a=b=c=diametre/2
            Dim(i,1)=str2num(get(findobj(gcf,'Tag',VBox),'String'))*1.0e-006/2;
            Dim(i,2)=str2num(get(findobj(gcf,'Tag',VBox),'String'))*1.0e-006/2;
            Dim(i,3)=str2num(get(findobj(gcf,'Tag',VBox),'String'))*1.0e-006/2;
        elseif Vshape==2
            param=str2num(get(findobj(gcf,'Tag',VBox2),'String'));
            if Vparam==1
                Dim(i,1)= param^(1/3)*str2num(get(findobj(gcf,'Tag',VBox),'String'))*1.0e-006/2;
                Dim(i,2)= Dim(i,1);
                Dim(i,3)= Dim(i,1)/param;
            elseif Vparam==2
                Dim(i,1)= ((str2num(get(findobj(gcf,'Tag',VBox),'String'))/2)^3/(param/2))^(1/2)*1.0e-006;
                Dim(i,2)= Dim(i,1);
                Dim(i,3)= param*1.0e-006/2;
            end
        elseif Vshape==3
            param=str2num(get(findobj(gcf,'Tag',VBox2),'String'));
            if Vparam==1
                Dim(i,1)= param^(2/3)*str2num(get(findobj(gcf,'Tag',VBox),'String'))*1.0e-006/2;
                Dim(i,2)= Dim(i,1)/param;
                Dim(i,3)= Dim(i,2);
            elseif Vparam==2
                Dim(i,1)=(str2num(get(findobj(gcf,'Tag',VBox),'String'))/2)^3/(param/2)^2*1e-006;
                Dim(i,2)= param*1.0e-006/2;
                Dim(i,3)= Dim(i,2);
            end
        end
        Vcol=get(findobj(gcf,'Tag',VBox),'BackgroundColor');
    end,
    
    % matrix containing total number of particles in each simulation
    j=0;
    nbtot_sim=zeros(nbsim,1);
    
    
    for i = 1:nbps*nbsim,

        nd(i,1)=floor(nbpart(i-floor((i-1)/nbps)*nbps)/nbsim)+matrest(i-floor((i-1)/nbps)*nbps,floor((i-1)/nbps)+1);
        nd(i,2)=Dim(i-floor((i-1)/nbps)*nbps,1);
        nd(i,3)=Dim(i-floor((i-1)/nbps)*nbps,2);
        nd(i,4)=Dim(i-floor((i-1)/nbps)*nbps,3);
        
        %changing index of matrix every nbps
        if (i-floor((i-1)/nbps)*nbps)==1
            j=j+1;
        end
        nbtot_sim(j,1)=nbtot_sim(j,1)+nd(i,1);
        
    end
    
    
    % no splitting in different simulations       
else
    nbsim=1;
    nbtot_sim=zeros(nbsim,1);
    for i = 1:nbps,
        VBox1 = strcat('EditText', num2str(i+4));
        VBox2= strcat('EditText', num2str(i+94));
        nd(i,1)=str2num(get(findobj(gcf,'Tag',VBox1),'String'));
        
        VBox = strcat('EditText', num2str(i+49));
        if Vshape==1
            %a=b=c=diametre/2
            nd(i,2)=str2num(get(findobj(gcf,'Tag',VBox),'String'))*1.0e-006/2;
            nd(i,3)=str2num(get(findobj(gcf,'Tag',VBox),'String'))*1.0e-006/2;
            nd(i,4)=str2num(get(findobj(gcf,'Tag',VBox),'String'))*1.0e-006/2;
        elseif Vshape==2
            %a=b
            param=str2num(get(findobj(gcf,'Tag',VBox2),'String'));
            if Vparam==1
                nd(i,2)= param^(1/3)*str2num(get(findobj(gcf,'Tag',VBox),'String'))*1.0e-006/2;
                nd(i,3)= nd(i,2);
                nd(i,4)= nd(i,2)/param;
            elseif Vparam==2
                nd(i,2)=((str2num(get(findobj(gcf,'Tag',VBox),'String'))/2)^3/(param/2))^(1/2)*1.0e-006;
                nd(i,3)= nd(i,2);
                nd(i,4)= param*1.0e-006/2;
            end
        elseif Vshape==3
            %b=c
            param=str2num(get(findobj(gcf,'Tag',VBox2),'String'));
            if Vparam==1
                nd(i,2)= param^(2/3)*str2num(get(findobj(gcf,'Tag',VBox),'String'))*1.0e-006/2;
                nd(i,3)= nd(i,2)/param;
                nd(i,4)= nd(i,3);
            elseif Vparam==2
                nd(i,2)=(str2num(get(findobj(gcf,'Tag',VBox),'String'))/2)^3/(param/2)^2*1e-006;
                nd(i,3)= param*1.0e-006/2;
                nd(i,4)=nd(i,3);
            end
        end
        nbtot_sim(1,1)=nbtot_sim(1,1)+nd(i,1);
    end,
end
if  Vsplit == 1
    [fichier,ext] = strtok(fich1,'.');
    for j=1:nbsim
        fsim=strcat(fichier,num2str(j),ext);
        fid=fopen(fsim,'w');
        a=sprintf('%d  %9.0f  %10.4E  %1.0f  %10.4E\n',0,nbtot_sim(j,1),rho,angdist,angdev);
        %if ispc, a = strrep(a, 'E+0', 'E+');   end
        %if ispc, a = strrep(a, 'E-0', 'E-');   end
        fprintf(fid,a);
        for k=1:nbps
            i=k+(j-1)*nbps;
            if nd(i,1)>0
                a=sprintf('%d  %9.0f  %10.4E  %10.4E  %10.4E  %10.4E  %10.4E  %10.4E  %10.4E  %10.4E  %10.4E\n',shape,nd(i,1),nd(i,2),nd(i,3),nd(i,4),0,0,0,0,0,0);   
                %if ispc, a = strrep(a, 'E+0', 'E+');   end
                %if ispc, a = strrep(a, 'E-0', 'E-');   end
                fprintf(fid,a);
            end
        end
        a=sprintf('%d  %9.0f  %10.4E  %10.4E  %10.4E  %10.4E  %10.4E  %10.4E  %10.4E  %10.4E  %10.4E\n',0,0,0,0,0,0,0,0,0,0,0);   
        %if ispc, a = strrep(a, 'E+0', 'E+');   end
        %if ispc, a = strrep(a, 'E-0', 'E-');   end
        fprintf(fid,a);
        fclose(fid);

    end
    
else
    fid=fopen(fich1,'w');
    a=sprintf('%d  %9.0f  %10.4E  %1.0f  %10.4E\n',0,nbtot_sim(1,1),rho,angdist,angdev);
    %if ispc, a = strrep(a, 'E+0', 'E+');   end
    %if ispc, a = strrep(a, 'E-0', 'E-');   end
    fprintf(fid,a)
    for k=1:nbps
        a=sprintf('%d  %9.0f  %10.4E  %10.4E  %10.4E  %10.4E  %10.4E  %10.4E  %10.4E  %10.4E  %10.4E\n',shape,nd(k,1),nd(k,2),nd(k,3),nd(k,4),0,0,0,0,0,0);   
        %if ispc, a = strrep(a, 'E+0', 'E+');   end
        %if ispc, a = strrep(a, 'E-0', 'E-');   end
        fprintf(fid,a);
    end
    a=sprintf('%d  %9.0f  %10.4E  %10.4E  %10.4E  %10.4E  %10.4E  %10.4E  %10.4E  %10.4E  %10.4E\n',0,0,0,0,0,0,0,0,0,0,0);   
    %if ispc, a = strrep(a, 'E+0', 'E+');   end
    %if ispc, a = strrep(a, 'E-0', 'E-');   end
    fprintf(fid,a);
    fclose(fid);
end
close(currentfig);