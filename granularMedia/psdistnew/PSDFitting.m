function out=PSDFitting;

global fich xdata ydata;

k=get(findobj(gcf,'Tag','EditText1'),'Value');
n=get(findobj(gcf,'Tag','EditText2'),'Value');
Value=get(findobj(gcf,'Tag','PopupMenu1'),'Value');

%try,
    taille=size(fich,1);
    if taille ~= 0,
        xdata=fich(:,1);
        ydata=fich(:,2);
    end,
    
    if Value == 5,
        Color=get(findobj(gcf,'Tag','EditText1'),'BackgroundColor');
        if Color==[1 1 1]
            %fprintf(1,'using xg and sg\n');
            x0(1)=get(findobj(gcf,'Tag','EditText1'),'Value');
            x0(2)=get(findobj(gcf,'Tag','EditText2'),'Value');
        else
            %fprintf(1,'using xbar and sbat\n');
            xbar=get(findobj(gcf,'Tag','EditText6'),'Value');
            sbar=get(findobj(gcf,'Tag','EditText7'),'Value');
            out=lognormal(xbar,sbar);
            x0(1)=out(1);
            x0(2)=out(2);
        end,
    else
        x0(1)=k;
        x0(2)=n;
    end,

%    options = optimset('Display','iter','TolX',1e-4)
    options = optimset('Display','iter');
    
    [x,resnorm,residual,exitflag,output] = lsqcurvefit(@psdfun,x0,xdata,ydata,[0 0],[1000 1000],options);
  
    output=output
    x=x
    out=x;
%catch,
    %end,

