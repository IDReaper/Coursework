(define reverseHelper (lambda(LS Acc)
                          (if
                           (null? LS)
                           Acc
                           (reverseHelper(cdr LS)(cons (car LS) Acc)))))

(define reverse (lambda (LS) (reverseHelper LS '())))

