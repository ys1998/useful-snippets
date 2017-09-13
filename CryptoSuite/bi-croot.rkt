#lang racket
(define state 0)
(define (bi-croot n)
  (bi-croot-helper n 1 n))
(define (bi-croot-helper n left right)
  (set! state (+ state 1))
  (displayln state)
  (let* [(mid (floor (/ (+ left right) 2)))]
    (if(<= (abs (- right left)) 1) (floor mid)
       (let [(res (* mid mid mid))]
         (cond [(< res n) (bi-croot-helper n mid right)]
               [else (bi-croot-helper n left mid)])))))
