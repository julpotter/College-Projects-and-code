;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname local) (read-case-sensitive #t) (teachpacks ((lib "universe.rkt" "teachpack" "2htdp") (lib "image.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #t #t none #f ((lib "universe.rkt" "teachpack" "2htdp") (lib "image.rkt" "teachpack" "2htdp")) #f)))
; List of Number -> Number
; finds the max of the list

(define (find-max lon) (cond
                         [(empty? (rest lon)) (first lon)]
                         [(> (first lon) (find-max (rest lon))) (first lon)]
                         [else (find-max (rest lon))]))

(define (max-list x) 0)
; List of Number -> Number
; finds the max of the list

(define (find-max2 lon) 
  (cond
    [(empty? (rest lon)) (first lon)]
    [else (local
            [(define max-list (find-max2 (rest lon)))]
            (if (> (first lon) max-list) (first lon) max-list))]))

(check-expect (find-max2 (list 6 3 1 7 8 4 2)) 8)
(check-expect (max-list 17) 0)

(define (add3 x) (local
                   [(define THREE 3)]
                   (+ x THREE)))

(check-expect (add3 14) 17)

; Posn, Posn -> Number
; Distance function making use of local
; simply to make the function's behavior more transparent
(define (distance p q)
  (local
    [(define dx (- (posn-x p) (posn-x q)))
     (define dy (- (posn-y p) (posn-y q)))]
    (sqrt (+ (sqr dx) (sqr dy)))))

; List of Number -> Number
; Produce the number of times the first element of the list
; appears in the list
(define (count-first lon)
  (local
    [(define FIRST (first lon))
     (define (count-in k lon) (length (filter (lambda (x) (= x k)) lon)))]
  (count-in FIRST lon)))

(check-expect (count-first (list 1 6 34 23 1 6 2 1)) 3)


(local
  [(define x 1)
   (define z (+ x 1))
   (define y (+ z 10))]
  (+ y x))

