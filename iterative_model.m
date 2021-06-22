function [a, k] = iterative_model(G, a, k)
% Graph G: gene interaction network
% a: vector 1, Initial values for authority scores of genes:
% k: vector 2, Initial values for hub scores of genes:

% Define threshold value, when to stop iterating:
t = 1E-3;

n = size(G, 2);

% Keep list of values for authority and hub scores during the iteration:
aValues = zeros(n, 0);
kValues = zeros(n, 0);
numIter = 0;

while 1
    % Old authority and hub scores:
    aOld = a; 
    kOld = k;
    % Update authority and hub scores and scale to unity:
    a = G' * kOld / sqrt(sum((G' * kOld).^2)); 
    k = G * aOld / sqrt(sum((G * aOld).^2));
    aDiff = abs(a - aOld);
    kDiff = abs(k - kOld);
    % Append new authority and hub scores to lists:
    aValues(:, end + 1) = a;
    kValues(:, end + 1) = k;
    if all(aDiff < t) && all(kDiff < t)
        disp(numIter+1); 
        break;
    end
   numIter = numIter + 1;
end

end
