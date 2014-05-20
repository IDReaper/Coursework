% Shawn Thompson
% Dr. Almeida
% Project 5

% power(X,N)
power(0, N, 0) :- N>0.
power(X, 0, 1) :- X>0.
power(X, N, Val) :- X>0, N>0, N1 is N-1, power(X ,N1, Val1), Val is Val1*X.

% sumOdd(N, Sum)
sumOdd(N ,1 ) :- N1 is 2*N-1, N1=1.
sumOdd(N, Sum) :- 