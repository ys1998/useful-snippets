#lang racket
(define (croot n)
  (croot-helper n (expt 10 300)))

(define (croot-helper num val)
  (if(< (abs (- (* val val val) num)) 1) (floor val)
     (croot-helper num (/ (+ (* 2 val) (/ num (* val val))) 3))
     ))