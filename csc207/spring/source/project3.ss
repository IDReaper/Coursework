(define cube-all(lambda(LS)
                    (if
                      (not (null? LS))
                        (cons (* (car LS) (car LS) (car LS)) (cube-all (cdr LS))) LS)))

(define rdc(lambda(LS)
             (if (null? (cdr LS))
                 '()
                 (cons (car LS) (rdc (cdr LS))))))

