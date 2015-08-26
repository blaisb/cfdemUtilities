clear all

%Intégration numérique des différentes fonctions de distributions 

% a = borne inférieure de l'intégrale
% b = borne supérieure de l'intégrale
% h = pas de l'intégration voulu
% k, n, r, sg = paramètre de l'équation

%Rosin-Rammler-Bennett

a = 2*10^-10;
b = 3*10^-5;
h = 10^-9;
k = 2*10^-6;
n = 1;

So1 = intrrb(a,b,h,k,n)

%Gates-Gaudin-Schumann

a = 10^-12;
b = 10^-2;
h = 10^-9;
k = 2*10^-6;
n = 2;

%So2 = intggs(a,b,h,k,n)

%Gaudin-Meloy

a = 1*10^-9;
b = 3*10^-6;
h = 10^-8;
k = 2*10^-6;
r = 3;

So3 = intgm(a,b,h,k,r)

%log-normal

a = 1.8*10^-10;
b = 3.4*10^-3;
h = 10^-9;
k = 0.5*10^-6;
sg = 2;

So4 = intln(a,b,h,k,sg)

%probabilité logarithmique

a = 10^-10;
b = 10^-4;
h = 10^-8;
k = 1*10^-6;
sg = 1;

%So5 = intlp(a,b,h,k,sg)







