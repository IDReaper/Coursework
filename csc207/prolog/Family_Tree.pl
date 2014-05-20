% Family Tree Program 

% parent(X,Y) - X is a parent of Y
parent(pete,ian). 	
parent(ian,peter). 
parent(ian,lucy). 
parent(lou,pete). 
parent(lou,pauline). 
parent(cathy,ian).

% female(X) - X is female     
female(cathy).		 
female(lucy).
female(pauline).
female(lou).

% male(X) - X is male
male(ian).		 
male(pete).
male(peter).

% mother(X,Y) - X is the mother of Y
mother(X,Y) :- parent(X,Y), female(X).

% father(X,Y) - X is the father of Y
father(X, Y) :- parent(X, Y), male(X).

% grandparent(X,Z) - X is the grandparent of Z
grandparent(X,Z) :- parent(X,Y), parent(Y,Z).

% sibling(X,Y) - X is a sibling of Y
sibling(X,Y) :- parent(Z,X), parent(Z,Y), X \= Y.

% predecessor(X,Z) - X is a predecessor of Z
predecessor(X, Z) :- parent(X, Z).
predecessor(X, Z) :- parent(X, Y), predecessor(Y, Z).