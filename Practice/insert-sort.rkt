;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname insert-sort) (read-case-sensitive #t) (teachpacks ((lib "universe.rkt" "teachpack" "2htdp") (lib "image.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #t #t none #f ((lib "universe.rkt" "teachpack" "2htdp") (lib "image.rkt" "teachpack" "2htdp")) #f)))
; ListOfString -> ListOfString
; Sorts the list
(define (my-quicksort los)
  (cond
    [(empty? los) empty]
    [else
     (local [(define pivot (first los))
             (define lesslist    (filter (lambda (s) (string<? s pivot)) los))
             (define equallist   (filter (lambda (s) (string=? s pivot)) los))
             (define greaterlist (filter (lambda (s) (string>? s pivot)) los))]
       (append (my-quicksort lesslist) equallist (my-quicksort greaterlist)))]))




; ListOfString -> ListOfString
; Sorts the list

(define (insert-sort los)
  (cond
    [(empty? los) empty]
    [else (insert (first los) (insert-sort (rest los)))]))

; String, ListOfString -> ListOfString
; inserts the item into the list, which must already be sorted
(define (insert item los)
  (cond
    [(empty? los) (list item)]
    [(string<? item (first los)) (cons item los)]
    [else (cons (first los) (insert item (rest los)))]))


(define l1 (list "happy" "birthday" "to" "you" "happy" "dear" "wilbur" "to" "happy" "happy"))
(define l2 (list 2 1 4 1 5 9 2 6 5 3 5 8 9 7 9))
