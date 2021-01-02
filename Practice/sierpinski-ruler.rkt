;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname sierpinski-ruler) (read-case-sensitive #t) (teachpacks ((lib "universe.rkt" "teachpack" "2htdp") (lib "image.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #t #t none #f ((lib "universe.rkt" "teachpack" "2htdp") (lib "image.rkt" "teachpack" "2htdp")) #f)))
; Sumorial
; adds numbers from 1 to n
(define (sumorial n)
  (cond
    [(= n 1) 1]
    [else (+ n (sumorial (- n 1)))]))

(check-expect (sumorial 100) 5050)


; ruler

(define little 30)
(define width 2)
(define (ruler n)
  (cond
    [(= n 1) (rectangle width little 'solid 'black)]
    [else (beside
           (ruler (- n 1))
           (rectangle width (* n little) 'solid
                      (if (even? n) 'red 'blue))
           (ruler (- n 1)))]))




; Sierpinski's triangle
(define T-size 50)
(define SCALE 2)
(define (sierpinski n size shape-fn)
  (cond
    [(= n 1) (shape-fn size 'solid 'black)]
    [else (above
           (sierpinski (- n 1) (/ size 2) shape-fn)
           (beside
            (sierpinski (- n 1) (/ size 2) shape-fn)
            (sierpinski (- n 1) (/ size 2) shape-fn)))]))
           