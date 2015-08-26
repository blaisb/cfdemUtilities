function So = intDm1(a, b, h, k, n, x)

m = ceil((b-a)/h);
h = (b - a) / m;

%Gates-Gaudin-Schumanns
if x==1
    I = (a^(n));
 
    for i = 1 : 2 : m-1
        x = a + h .* i;
        I = I + 4 * (x^(n));
    end
 
    for i = 2 : 2 : m-2
        x = a + h .* i;
        I = I + 2 * (x^(n));
    end
 
    I = I + (b^(n));

    So =(n/(k^n))* h * I / 3;

%Gaudin-Meloy
elseif x==2
    I = (a)*(abs(1-(a/k))^(n-1));
 
    for i = 1 : 2 : m-1
        x = a + h .* i;
        I = I + 4 * (x)*(abs(1-(x/k))^(n-1));
    end
 
    for i = 2 : 2 : m-2
        x = a + h .* i;
        I = I + 2 * (x)*(abs(1-(x/k))^(n-1));
    end
 
    I = I + (b)*(abs(1-(b/k))^(n-1));

    So = (n/k)*h * I / 3;

%logarithmic probability
elseif x==3
    I = exp(-(log(a/k)/n)^2);
 
    for i = 1 : 2 : m-1
        x = a + h .* i;
        I = I + 4 * exp(-(log(x/k)/n)^2);
    end
 
    for i = 2 : 2 : m-2
        x = a + h .* i;
        I = I + 2 * exp(-(log(x/k)/n)^2);
    end
 
    I = I + exp(-(log(b/k)/n)^2);

    So = (2/(n*sqrt(pi)))* h * I / 3;

%Rosin-Rammler-Benett
elseif x==4
    I = (a^(n))*exp(-(a/k)^n);
 
    for i = 1 : 2 : m-1
        x = a + h .* i;
        I = I + 4 * (x^(n))*exp(-(x/k)^n);
    end
 
    for i = 2 : 2 : m-2
        x = a + h .* i;
        I = I + 2 * (x^(n))*exp(-(x/k)^n);
    end
 
    I = I + (b^(n))*exp(-(b/k)^n);

    So = (n/(k^n))* h * I / 3;

%log-normal
elseif x==5
    I = exp(-(1/2)*(log(a/k)/log(n))^2);
 
    for i = 1 : 2 : m-1
        x = a + h .* i;
        I = I + 4 *exp(-(1/2)*(log(x/k)/log(n))^2);
    end
 
    for i = 2 : 2 : m-2
        x = a + h .* i;
        I = I + 2 * exp(-(1/2)*(log(x/k)/log(n))^2);
    end
 
    I = I + exp(-(1/2)*(log(b/k)/log(n))^2);

    So = (1/(sqrt(2*pi)*log(n)))* h * I / 3;
end
