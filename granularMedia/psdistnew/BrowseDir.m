v=1;
while v==1,
   if idrive == 0,
      clear str;
      d = dir;
      str = {d.name};
      if char(str(:,1)) == '.',
         j=0;
      else
         j=2;
         str(1)={'.'};
         str(2)={'...'};
      end
   else
      idrive =0;
   end
   [s,v] = listdlg('PromptString','Select a data file:',...
                   'Name','Browse',...
                   'SelectionMode','single',...
                   'ListString',str);
   file=char(str(:,s));
   if v == 0,
      fich=strcat(pwd,'\');
   else   
      switch file
         case '...',
            drive ={'a:','b:','c:','d:','e:','f:','g:','h:','i:','j:','k:','l:','m:','n:','o:','p:','q:','r:','s:'};
            rep=pwd;
            l=0;
            clear str;
            for i=1:1:size(drive,2),
               try
                  cd(char(drive(:,i)));
                  l=l+1;
                  str(l)=drive(i);
                  idrive=1;
               catch
               end
            end
            cd(rep);
         case '..',
            cd('..');
         case '.',
            fich=strcat(pwd,'\');
            v=0;   
         otherwise,
            try
               cd(file);     
            catch
               fich=strcat(pwd,'\',file);
               v=0;
             end
       end
   end
end
set(findobj(gcf,'Tag','EditText1'),'String',fich);