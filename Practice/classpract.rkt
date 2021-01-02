;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname classpract) (read-case-sensitive #t) (teachpacks ((lib "universe.rkt" "teachpack" "2htdp") (lib "image.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #t #t none #f ((lib "universe.rkt" "teachpack" "2htdp") (lib "image.rkt" "teachpack" "2htdp")) #f)))

; Number -> List of Posns

(define (lop1k k) (cond
                    [(= k 1) (list (make-posn 1 1))]
                    [else (cons (lop1k (- k 1)) (list (make-posn k k)))]))


; Write a function add-last

; List, Item -> List
; Adds item to the end of the list

(define (add-last loi i) (cond
                           [(empty? loi) (list i)]
                           [else (cons (first loi) (add-last (rest loi) i))]))

                       
(check-expect (add-last (list 2 4 6) 3) (list 2 4 6 3))






