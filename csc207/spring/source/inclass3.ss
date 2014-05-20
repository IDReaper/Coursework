(define cube-two (lambda (x y) (list (* x x x) (* y y y))))
(define second1 (lambda (LS) (cadr LS)))
(define second2 (lambda (LS) (if (and (not (null? LS)) (not (null? (cdr LS)))) (cadr LS) LS)))



