(define sumlist
    (lambda (ls)
    (cond
      ((null? ls)
       0)
      ((pair? (car ls))
       (+ (sumlist(car ls)) (sumlist(cdr ls))))
      (else
       (+ (car ls) (sumlist (cdr ls)))))))

(define sumOdd
  (lambda (N)
    (if (= N 1) 1
        (+ (sumOdd (- N 1)) (- (* 2 N) 1) ))))

(define getNth
  (lambda (N LS)
    (cond 
     ((eq? N 0) 
      (car LS))
     ((null? LS)
      '())
     (else
        (getNth (- N 1) (cdr LS))))))
        

