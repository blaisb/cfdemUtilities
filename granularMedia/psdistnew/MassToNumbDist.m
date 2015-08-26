%mass distribution into number distribution
function a=MassToNumbDist(d,w)

n=zeros(1,length(d));
if length(d)~=length(w)
    disp('DIAMETER AND MASS FRACTION MATRIX HAVE DIFFERENT SIZES')
end


for i=1:length(d)
    n(i)=w(i)/(d(i)^3);
end
nTot=sum(n);
a=n./nTot;
if ((sum(a)-1)>1e-6)
    disp('ERROR WITH MASS TO NUMBER DISTRIBUTION')
end
end