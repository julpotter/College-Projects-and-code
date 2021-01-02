;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname pract3) (read-case-sensitive #t) (teachpacks ((lib "universe.rkt" "teachpack" "2htdp") (lib "image.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #t #t none #f ((lib "universe.rkt" "teachpack" "2htdp") (lib "image.rkt" "teachpack" "2htdp")) #f)))
(define lol1 (list (list 1 2 3) (list ) (list 2 3 4)))

; List of List -> List of List
; Keeps only lists that are not empty
(define (non-empty lol) (filter cons? lol))

(check-expect (non-empty (list (list 1 2 3)
                               (list )
                               (list 2 3 4)))
              (list (list 1 2 3) (list 2 3 4)))


; List of List of Number -> List of List of Number
; Remove all lists that are not of size exactly one
(define (favorite-numbers-checker lol) (filter (lambda (x) (= (length x) 1)) lol))

(define lol2 (list (list 1 2) (list 9) (list) (list 1 29 103)))
(check-expect (favorite-numbers-checker lol2) (list (list 9)))


; List of Number -> List of Number
; Founds each odd number up, leaves even numbers unchanged
(define (rod l) (map (λ (x) (if (odd? x) (+ 1 x) x)) l))

(check-expect (rod (list 1 2 3 4 5 6 7)) (list 2 2 4 4 6 6 8))

(define lon1 (list 1 2 3 4 5 6 7))


