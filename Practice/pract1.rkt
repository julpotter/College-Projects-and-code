;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname pract1) (read-case-sensitive #t) (teachpacks ((lib "universe.rkt" "teachpack" "2htdp") (lib "image.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "universe.rkt" "teachpack" "2htdp") (lib "image.rkt" "teachpack" "2htdp")) #f)))
(define (k-n l) (cond
                 [(= 0 (first (rest l))) empty]
                 [else (cons (first l) (k-n (cons (+ 1 (first l)) (cons (- (first (rest l)) 1) empty))))]))


(check-expect (k-n (list 7 8)) (list 7 8 9 10 11 12 13 14))

;Group 2
; List of Numbers -> List of two Posn
; The first posn is made from the first two numbers in the list,
; The second is made from the last two numbers in the list
; You may assume the list has at least two numbers in it

(define (make-two-posn lof) (list
                             (make-posn (list-ref lof 0) (list-ref lof 1))
                             (make-posn (list-ref lof (- (length lof) 2)) (list-ref lof (- (length lof) 1)))))
                             


(check-expect (make-two-posn (list 1 2)) (list (make-posn 1 2) (make-posn 1 2)))
(check-expect (make-two-posn (list 1 2 3)) (list (make-posn 1 2) (make-posn 2 3)))
(check-expect (make-two-posn (list 1 2 3 4 5)) (list (make-posn 1 2) (make-posn 4 5)))
(check-expect (make-two-posn (list 1 2 3 4 5 6 7 8)) (list (make-posn 1 2) (make-posn 7 8)))

