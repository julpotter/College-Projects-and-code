;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname tree) (read-case-sensitive #t) (teachpacks ((lib "universe.rkt" "teachpack" "2htdp") (lib "image.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #t #t none #f ((lib "universe.rkt" "teachpack" "2htdp") (lib "image.rkt" "teachpack" "2htdp")) #f)))
; Binary Node Data Structure
; data is the item that the node holds
; left is the left child, also a b-node
; right is the right child, also a b-node
(define-struct b-node (data left right))


; b-node -> Number
; Counts the total number of nodes in the tree below T
(define (count-students T)
  (+ (count-students (b-node-left T))
     (count-students (b-node-right T))
     1))