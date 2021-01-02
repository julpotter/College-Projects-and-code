(define (sum-of-squares a b)
  (if (> a b)
    0
    (+ ((lambda (x) (* x x)) a) (sum-of-squares (+ a 1) b))))
    
