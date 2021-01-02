;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname quicksort) (read-case-sensitive #t) (teachpacks ((lib "universe.rkt" "teachpack" "2htdp") (lib "image.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #t #t none #f ((lib "universe.rkt" "teachpack" "2htdp") (lib "image.rkt" "teachpack" "2htdp")) #f)))
(define l1 (build-list 20 (lambda (x) (random 100))))


; List of Number -> List of Number
; Sorts the list into increasing order
(define (my-quicksort lon)
  (cond
    [(empty? lon) empty]
    [(empty? (rest lon)) (list (first lon))]
    [else
     (local
       [(define pivot (first lon))
        (define lower (filter (lambda (x) (< x pivot)) lon))
        (define higher (filter (lambda (x) (> x pivot)) lon))
        (define equal (filter (lambda (x) (= x pivot)) lon))]
       (append (my-quicksort lower) equal (my-quicksort higher))
       )]))
    
(check-expect (my-quicksort l1) (sort l1 <))



