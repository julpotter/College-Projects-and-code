;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname treepract) (read-case-sensitive #t) (teachpacks ((lib "universe.rkt" "teachpack" "2htdp") (lib "image.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #t #t none #f ((lib "universe.rkt" "teachpack" "2htdp") (lib "image.rkt" "teachpack" "2htdp")) #f)))
; Binary Node Data Structure
; data is the item that the node holds
; left is the left child, also a b-node
; right is the right child, also a b-node
(define-struct b-node (data left right))

; b-Node -> Number
; Counts the total number of nodes in the tree below T
(define (count-nodes T)
  (cond
    [(and (equal? (b-node-left T) NULL) (equal? (b-node-right T) NULL)) 1]
    [(equal? (b-node-right T) NULL) 2]
    [(equal? (b-node-left T) NULL) 2]
    [else (+ (count-nodes (b-node-left T))
             (count-nodes (b-node-right T))
             1)]))
     

(define NULL 0)

(define nG (make-b-node "G" NULL NULL))
(define nD (make-b-node "D" NULL NULL))
(define nF (make-b-node "F" NULL NULL))
(define nE (make-b-node "E" nG NULL))
(define nB (make-b-node "B" nD nE))
(define nC (make-b-node "C" nF NULL))
(define nA (make-b-node "A" nB nC))


(check-expect (count-nodes nA) 7)
(check-expect (count-nodes nG) 1)
(check-expect (count-nodes nB) 4)


;(define (tree-height T)
;  (cond
;    [(and (equal? (b-node-left T) NULL) (equal? (b-node-right T) NULL)) -1]
;    [(equal? (b-node-right T) NULL) 1]
;    [(equal? (b-node-left T) NULL) 1]
;    [else (+ (tree-height (b-node-left T))
;             (tree-height (b-node-right T)))
;             ]))


; B-node -> B-node
; Inserts string str into the proper place
; (alphabetically) into the tree
(define (tree-insert T str)
  (make-b-node ... ... ... ))



