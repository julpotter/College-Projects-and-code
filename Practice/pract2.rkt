;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname pract2) (read-case-sensitive #t) (teachpacks ((lib "universe.rkt" "teachpack" "2htdp") (lib "image.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #t #t none #f ((lib "universe.rkt" "teachpack" "2htdp") (lib "image.rkt" "teachpack" "2htdp")) #f)))
; map

(define x (list 1 3 5 2 4 6 1))

; square all entries
(define (sqrall lon)
  (cond
    [(empty? lon) empty]
    [else (cons (sqr (first lon)) (sqrall (rest lon)))]))

; All of that can be replaced by
(map sqr x)
