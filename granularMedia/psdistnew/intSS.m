function So = intSS(a, b, h, k, n, x)

m = ceil((b-a)/h);
h = (b - a) / m;

%Gates-Gaudin-Schumanns
if x==1
    I = (a^(n-2));
 
    for i = 1 : 2 : m-1
        x = a + h .* i;
        I = I + 4 * (x^(n-2));
    end
 
    for i = 2 : 2 : m-2
        x = a + h .* i;
        I = I + 2 * (x^(n-2));
    end
 
    I = I + (b^(n-2));

    So =6*(n/(k^n))* h * I / 3;

%Gaudin-Meloy
elseif x==2
    I = (1/a)*(abs(1-(a/k))^(n-1));
 
    for i = 1 : 2 : m-1
        x = a + h .* i;
        I = I + 4 * (1/x)*(abs(1-(x/k))^(n-1));
    end
 
    for i = 2 : 2 : m-2
        x = a + h .* i;
        I = I + 2 * (1/x)*(abs(1-(x/k))^(n-1));
    end
 
    I = I + (1/b)*(abs(1-(b/k))^(n-1));

    So = 6*(n/k)*h * I / 3;

%logarithmic probability
elseif x==3
    I = (1/(a^2))*exp(-(log(a/k)/n)^2);
 
    for i = 1 : 2 : m-1
        x = a + h .* i;
        I = I + 4 * (1/(x^2))*exp(-(log(x/k)/n)^2);
    end
 
    for i = 2 : 2 : m-2
        x = a + h .* i;
        I = I + 2 * (1/(x^2))*exp(-(log(x/k)/n)^2);
    end
 
    I = I + (1/(b^2))*exp(-(log(b/k)/n)^2);

    So = 6*(2/(n*sqrt(pi)))* h * I / 3;

%Rosin-Rammler-Benett
elseif x==4
    I = (a^(n-2))*exp(-(a/k)^n);
 
    for i = 1 : 2 : m-1
        x = a + h .* i;
        I = I + 4 * (x^(n-2))*exp(-(x/k)^n);
    end
 
    for i = 2 : 2 : m-2
        x = a + h .* i;
        I = I + 2 * (x^(n-2))*exp(-(x/k)^n);
    end
 
    I = I + (b^(n-2))*exp(-(b/k)^n);

    So = 6*(n/(k^n))* h * I / 3;

%log-normal
elseif x==5
    I = (1/(a^2))*exp(-(1/2)*(log(a/k)/log(n))^2);
 
    for i = 1 : 2 : m-1
        x = a + h .* i;
        I = I + 4 *(1/(x^2))*exp(-(1/2)*(log(x/k)/log(n))^2);
    end
 
    for i = 2 : 2 : m-2
        x = a + h .* i;
        I = I + 2 * (1/(x^2))*exp(-(1/2)*(log(x/k)/log(n))^2);
    end
 
    I = I + (1/(b^2))*exp(-(1/2)*(log(b/k)/log(n))^2);

    So = 6*(1/(sqrt(2*pi)*log(n)))* h * I / 3;
end
