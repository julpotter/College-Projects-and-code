;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname Ball-lists) (read-case-sensitive #t) (teachpacks ((lib "universe.rkt" "teachpack" "2htdp") (lib "image.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #t #t none #f ((lib "universe.rkt" "teachpack" "2htdp") (lib "image.rkt" "teachpack" "2htdp")) #f)))

(define-struct Ball (px py dx dy))
(define WIDTH 1000)
(define HEIGHT 800)
(define RADIUS 13)
(define DX 20)
(define DY 30)
; Ball is a structure holding position
; of a single Ball


(define balls
  (list
   (make-Ball 300 400 DX DY)
   (make-Ball 200 100 4 2)
   (make-Ball 0 0 17 -20)))


; List of Ball -> Image
(define (draw-them lob)
  (cond
    [(empty? lob) (empty-scene WIDTH HEIGHT)]
    [else (underlay/xy (draw-them (rest lob))
                      (Ball-px (first lob)) (Ball-py (first lob))
                      (circle RADIUS 'solid 'red))]))



     

