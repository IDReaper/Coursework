Welcome to DrScheme, version 4.1 [3m].
Language: Essentials of Programming Languages (3rd ed.); memory limit: 128 megabytes.
> (define cube-all(lambda(LS)
                    (if (null? LS)
                        '()
                        (* LS LS LS))))
> (cube-all '())
()
> (cube-all '(3))
. . *: expects type <number> as 1st argument, given: (3); other arguments were: (3) (3)
> (define cube-all(lambda(LS)
                    (if (null? LS)
                        '()
                        ((* LS (* LS LS))))))
> (cube-all '(3))
. . *: expects type <number> as 1st argument, given: (3); other arguments were: (3)
> (define cube-all(lambda(LS)
                    (if (null? LS)
                        '()
                        (cons (cube-all (cdr LS)) (* (car LS)(* (car LS) (car LS)))))))
> (cube-all '())
()
> (cube-all '(3))
(() . 27)
> (define cube-all(lambda(LS)
                    (if (null? LS)
                        '()
                        (list (cube-all (cdr LS)) (* (car LS)(* (car LS) (car LS)))))))
> (cube-all '(3))
(() 27)
> (define cube-all(lambda(LS)
                    (and 
                     (if (null? LS) LS) 
                     (if (null? LS) LS))
                        (list (cube-all (cdr LS)) (* (car LS)(* (car LS) (car LS)))))))
. read: unexpected `)'
> (define cube-all(lambda(LS)
                    (and 
                     (if (null? LS) LS) 
                     (if (null? LS) LS)
                        (list (cube-all (cdr LS)) (* (car LS)(* (car LS) (car LS)))))))
> (cube-all '(3))
. . cdr: expects argument of type <pair>; given ()
> (define cube-all(lambda(LS)
                    (if 
                     (and 
                      (not (null? LS))
                      (not (null? (cdr LS))))
                     LS
                     (list (cube-all (cdr LS)) (* (car LS)(* (car LS) (car LS)))))))
> (cube-all '(3))
. . cdr: expects argument of type <pair>; given ()
> (define cube-all(lambda(LS)
                    (if (null? LS)
                        '()
                        (list (cube-all (cdr LS)) (* (car LS)(* (car LS) (car LS)))))))
> (cube-all '(3))
(() 27)
> (define cube-all(lambda(LS)
                    (if
                     (and
                      (null? LS)
                      (null? (cdr LS)))
                        '()
                        (list (cube-all (cdr LS)) (* (car LS)(* (car LS) (car LS)))))))
> (cube-all '(3))
. . cdr: expects argument of type <pair>; given ()
> (define cube-all(lambda(LS)
                    (if
                     (and
                      (not (null? LS))
                      (not (null? (cdr LS))))
                        (list (cube-all (cdr LS)) (* (car LS)(* (car LS) (car LS))))) LS))
> (cube-all '(3))
(3)
> (cube-all '(3 6))
(3 6)
> (define cube-all(lambda(LS)
                    (if
                     (and
                      (not (null? LS))
                      (not (null? (cdr LS))))
                        (list (cube-all (cdr LS)) (* (car LS) (* (car LS) (car LS))))) LS))
> (cube-all '(3 6))
(3 6)
> (cube-all '(3 6 8))
(3 6 8)
> (define cube-all(lambda(LS)
                    (if
                     (and
                      (not (null? LS))
                      (not (null? (cdr LS))))
                        (list (cube-all (cdr LS)) (* (car LS) (* (car LS) (car LS)))))))
> (cube-all '(3 6 8))
((#<void> 216) 27)
> (define power(lambda(x n)
	(if (= n 0)
	    1
	(* (power x (- n 1)) x))))
> (define cube-all(lambda(LS)
                    (if
                     (and
                      (not (null? LS))
                      (not (null? (cdr LS))))
                        (list (cube-all (cdr LS)) (power((car LS) 3))))))
> (cube-all '(3 6 8))
. . procedure application: expected procedure, given: 6; arguments were: 3
> (define cube-all(lambda(LS)
                    (if
                     (and
                      (not (null? LS))
                      (not (null? (cdr LS))))
                        (list (cube-all (cdr LS)) (power((car LS) 3))))))
> (cube-all '(3 6 8))
. . procedure application: expected procedure, given: 6; arguments were: 3
> (power 2 3)
8
> (define cube-all(lambda(LS)
                    (if
                     (and
                      (not (null? LS))
                      (not (null? (cdr LS))))
                        (list (cube-all (cdr LS)) (power (car LS) 3)))))
> (cube-all '(3 6 8))
((#<void> 216) 27)
> (define cube-all(lambda(LS)
                    (if
                     (and
                      (not (null? LS))
                      (not (null? (cdr LS))))
                        (cons (cube-all (cdr LS)) (power (car LS) 3)) LS)))
> (cube-all '(3 6 8))
(((8) . 216) . 27)
> (define cube-all(lambda(LS)
                    (if
                     (and
                      (not (null? LS))
                      (not (null? (cdr LS))))
                        (append (cube-all (cdr LS)) (power (car LS) 3)) LS)))
> (cube-all '(3 6 8))
. . append: expected argument of type <proper list>; given (8 . 216)
> (define cube-all(lambda(LS)
                    (if
                     (and
                      (not (null? LS))
                      (not (null? (cdr LS))))
                        (cons (cube-all (cdr LS)) (power (car LS) 3)) LS)))
> (cube-all '(3 6 8))
(((8) . 216) . 27)
> 
> 
> (define sumListHelper (lambda(LS Acc)
                          (if
                           (null? LS)
                           Acc
                           (sumListHelper(cdr LS)(+ (car LS) Acc)))))
> (sumList '(1 4 2))
. . reference to undefined identifier: sumList
> (sumListHelper '(1 4 2) 0)
7
> (sumListHelper '(4 4 2) 0)
10
> (sumListHelper '(4 4 2) 0)