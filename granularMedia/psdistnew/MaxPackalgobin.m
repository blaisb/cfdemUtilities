function [L,p]=algobin(N,dmin,dmax,mode,lastL,lastP,botequa,n,k,Vave,a,d)
%p=0; % USELESS RIGHT NOW

%Define relative tolerance for the L precision
error=1e-6;
maxtrapeze=500;

%botequa=sum(a.*d.^2) % A REFAIRE
Lmin=dmin;
Lmax=lastL; % Since we go in decreasing size of rod

F=2*(1/N); % Random value just to start the while loop
counts=1;

   
   switch mode
       
       case 'Data fitting'
           %For this case, we will solve equation 24 using equation 30 of
           %the 2013 article "Random close packing fractions of lognormal
           %distribution of hard spheres
           
           %value=1-(2*N-2*botequa+1)/(2*N); %for this case, botequa=i  
           value=1/N;
           Ntot=length(a);
           F=value; %To initiate loop only
           botequa;
           Lmin=0; %dmin/1e3;
           Lmax=1*lastL;
           
           counter=0;
           % Counter useful in case the L value is around a particle value
           % because it will not stop otherwise
           while ((abs(F/value)>error) && (counter<1000))  
               Lmid=(Lmin+Lmax)/2;
               
               F=0;
               somme=0;
               sum4p=zeros(1,Ntot);
               sum5p=zeros(1,Ntot);
               sum4=0;
               sum5=0;

               for i=1:Ntot
                   if d(i)>Lmid
                       sum4p(i)=sum4+a(i);
                   else
                       sum4p(i)=0;
                   end
                   sum5p(i)=sum5+a(i)*d(i)^2;
               end
                     
                       
               sum4=sum(sum4p);
               sum5=sum(sum5p);
               somme=2*Lmid*sum4/sum5; % c'est une probabilité/distance (m^-1)
               % Le F ici c'est l'integrale de p sur l'intervale L(i-1) à
               % L(i) et doit donner 1/N
               F=(somme+lastP)/2*(lastL-Lmid)-value; 

               L=Lmid;

               if (F<0)
                   Lmax=Lmid; %search on lower bound
               else
                   Lmin=Lmid; %search on higher bound
               end
               counter=counter+1;
           end

           p=(2/N)/(lastL-L)-lastP;
           
 %------------------------END OF PROGRAM IN USE --------------------------
 
 % Rest of the program was to be used with every model without
 % discretization (using the equations and integrals)
 
 % But discretization works really well and is quicker, so the models were
 % not finalized 
 
 
 
 
 %------------------------------------------------------------------------
 
 
           %------------------------------------------
           %                USELESS
           %------------------------------------------
       case 'Gates-Gaudin-Schumann'
           m=n;
           
           %----------------------------------------
           while (abs((F-1/N)/(1/N))>error)  
           Lmid=(Lmin+Lmax)/2;
%                if counts==1
%                     disp ('NOOOO')
%                     topequa=0;
%                     deltad=abs(dmax-Lmin)/maxtrapeze;
%                     l(1)=Lmin;
%                     for i=1:maxtrapeze-1
%                         l(i+1)=l(i)+deltad;
%                         topequa=topequa+(6*Vave/pi)*0.5*deltad*(r/k)*((1-l(i+1)/k)^(r-1)/l(i+1)^3+(1-l(i)/k)^(r-1)/l(i)^3);
%                %topequa=topequa+(6*Vave/pi)*0.5*deltad*(r/k)*((1-l(i+1)/k)^(r-1)+(1-l(i)/k)^(r-1));
%                     end
%                     adjuster=topequa;
%                 end
           
                itetrapeze=round(maxtrapeze/2)+round(0.5*maxtrapeze*(abs(dmax-Lmid)/(dmax-dmin)));
                deltad=abs(dmax-Lmid)/itetrapeze;
                
                l(1)=Lmid;
                topequa=0; %Reinitialize
                for i=1:itetrapeze-1
                    l(i+1)=l(i)+deltad;
                    topequa=topequa+(6*Vave/pi)*0.5*deltad*(m/k^m)*(l(i+1)^(m-4) + l(i)^(m-4));
                end

                %topequa=topequa/adjuster;
                %F=2*Lmid*topequa/botequa
                F=((2*Lmid*topequa/botequa)+lastP)/2*abs(lastL-Lmid);
                %F(counts)=F;
                counts=counts+1;
                
                L=Lmid;
                if (F<1/N)
                    Lmax=Lmid;
                else
                    Lmin=Lmid;
                end
           end
       case 'Gaudin-Meloy'
           r=n;
           
           while ((abs((F-2/N)/(2/N))>error) && (counter<1000))  
           Lmid=(Lmin+Lmax)/2
%                 if counts==1
%                     topequa=0;
%                     deltad=abs(dmax-Lmin)/maxtrapeze;
%                     l(1)=Lmin;
%                     for i=1:maxtrapeze-1
%                         l(i+1)=l(i)+deltad;
%                         topequa=topequa+(6*Vave/pi)*0.5*deltad*(r/k)*((1-l(i+1)/k)^(r-1)/l(i+1)^3+(1-l(i)/k)^(r-1)/l(i)^3);
%                %topequa=topequa+(6*Vave/pi)*0.5*deltad*(r/k)*((1-l(i+1)/k)^(r-1)+(1-l(i)/k)^(r-1));
%                     end
%                     adjuster=topequa;
%                 end
           
                itetrapeze=round(maxtrapeze/2)+round(0.5*maxtrapeze*(abs(dmax-Lmid)/(dmax-dmin)));
                deltad=abs(dmax-Lmid)/itetrapeze;
                l(1)=Lmid;
                topequa=0; %Reinitialize
                for i=1:itetrapeze-1
                    l(i+1)=l(i)+deltad;
                    topequa=topequa+(6*Vave/pi)*0.5*deltad*(m/k^m)*(l(i+1)^(m-4) + l(i)^(m-4));
                end

                %topequa=topequa/adjuster;
                %F=real(2*Lmid*topequa/botequa)
                F=((2*Lmid*topequa/botequa)+lastP)/2*abs(lastL-Lmid);
                counts=counts+1
                
                L=Lmid;
                if (F<1/N)
                    Lmax=Lmid;
                else
                    Lmin=Lmid;
                end
           end
            %-------------------------------------------------------------
            
           case 'Log-normal'
               
               D0=n;
               sigma=k;
               
               counts=0;
               part1=exp(-2*sigma^2)/(D0^2); %used in the loop for intP1D for calculation speed (eq22)


               F=2*(2/N); %Initiate the while
               
               while (((abs(abs(F)-1/N)/(1/N))>error) && (counts<1000))
                    Lmid=(Lmin+Lmax)/2;
                    
%                     presentP=1+0.5*Lmid^2*part1*erfc(log(Lmid/D0)/(sigma*sqrt(2)));
%                     presentP=presentP-erfc(log(Lmid/D0)/(sigma*sqrt(2))-sqrt(2)*sigma);
%                     F=(presentP+lastP)/2*(lastL-Lmid);
           

                    
                    
%                     presentP=Lmid*part1*erfc(log(Lmid/D0)/(sigma*sqrt(2)));
%                     F=(presentP+lastP)/2*(lastL-Lmid);
                    if botequa==60
                        disp('stop')
                    end
                    
                    itetrapeze=round(maxtrapeze/2)+round(0.5*maxtrapeze*(abs(lastL-Lmid)/(lastL-dmin)));
                    deltad=abs(lastL-Lmid)/itetrapeze;
                    %l(1)=Lmid;
                    intP1D=zeros(1,itetrapeze+1); %Reinitialize
                    integral=0;
                    l=zeros(1,itetrapeze+1);
                    %l(end)=Lmax;
                    
                    
                    
                    for i=1:itetrapeze+1;
                        l(i)=Lmid+(i-1)*deltad;
                        intP1D(i)=l(i)*part1*erfc(log(l(i)/D0)/(sigma*sqrt(2))); %Equation 22
                        %part1 put to simplify calculus
                    end
                    integral=(intP1D(1)+2*sum(intP1D(2:end-1))+intP1D(end))*deltad/2;
                    F=integral;
                    %F=(integral+lastP)/2*abs(lastL-Lmid);
%                     
                    counts=counts+1;
                
                    L=Lmid;
                    if (abs(F)<1/N)
                        Lmax=Lmid;
                    else
                        Lmin=Lmid;
                    end
                   
               end
               p=L*part1*erfc(log(L/D0)/(sigma*sqrt(2)))
%        
               
 % -------------------------- END OF USELESS PART -------------------------
 
 
 
 
 %-------------------------------------------------------------------------
 
   end

