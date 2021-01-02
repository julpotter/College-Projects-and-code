;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname pract4) (read-case-sensitive #t) (teachpacks ((lib "universe.rkt" "teachpack" "2htdp") (lib "image.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #t #t none #f ((lib "universe.rkt" "teachpack" "2htdp") (lib "image.rkt" "teachpack" "2htdp")) #f)))
(define lon1 (list 1 5))

(foldl + 3 lon1)
(foldl - 3 lon1)
(foldr - 3 lon1)

(define lop1 (list (make-posn 20 30)
                   (make-posn 50 20)
                   (make-posn 10 70)
                   (make-posn 90 40)
                   (make-posn 150 50)
                   (make-posn 120 100)
                   (make-posn 160 128)
                   ))

(define FLOWER (square 8 'solid 'magenta))
(define EMPTY-FIELD (empty-scene 200 200))
; Posn, Image -> Image
; Draws a FLOWER at location p atop the image img
(define (flower-render-helper p img)
  (underlay/xy img (posn-x p) (posn-y p) FLOWER))
         
(foldl flower-render-helper (empty-scene 200 200) (filter (lambda (p) (< (posn-y p) (/ (image-height EMPTY-FIELD) 2))) lop1))

; Challenge
; List of Posn -> Image
; Draw a "flower" at each posn location, but only those that are in the top half of the field

; (foldl (lambda (p img) (underlay/xy img (posn-x p) (posn-y p) FLOWER)) (empty-scene 200 200) (filter (< (posn-y p) (/ (height EMPTY-FIELD) 2)) lop1))