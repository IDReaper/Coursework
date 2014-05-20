(define delete 
  (lambda (elem ls)
    (cond
      ((null? ls)
       ls)
      ((eq? elem (car ls))
       (cdr ls))
      (else
       (cons (car ls) (delete elem (cdr ls)))))))

(define reverse
  (lambda (ls)
    (if
      (null? ls) ls
      (append (reverse (cdr ls)) (list(car ls))))))
                     