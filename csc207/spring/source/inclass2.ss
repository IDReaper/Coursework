(require scheme/math)

(define cube(lambda(x)(* x x x)))
(define sphere(lambda(r)(* (/ 4 3) pi (* r r r))))
(define pizza-cost(lambda(price diameter)(/ price (* pi (* (/ diameter 2) (/ diameter 2))))))



