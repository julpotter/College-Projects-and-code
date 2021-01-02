;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname FinalProjectpract) (read-case-sensitive #t) (teachpacks ((lib "universe.rkt" "teachpack" "2htdp") (lib "image.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #t #t none #f ((lib "universe.rkt" "teachpack" "2htdp") (lib "image.rkt" "teachpack" "2htdp")) #f)))


(define-struct WS (health-remaining))

; KeyPress -> Number
; Attack with spacebar to remove health
(define (hit ws a-key) (cond
                         [(key=? a-key " ") (make-WS (- (WS-health-remaining ws) (random 5 20)))]))

; Number -> Image
(define (render ws) (overlay/align "left" "middle" (rectangle (WS-health-remaining ws) 15 'solid 'green) (rectangle 100 15 'solid 'red)))


(define initWS (make-WS 100))

; Number -> Boolean
(define (gameOver? ws) (cond
                         [(<= (WS-health-remaining ws) 0) #true]
                         [else #false]))

(define (finalScene ws) (text "DEAD" 15 'red))


(big-bang initWS (to-draw render) (on-key hit) (stop-when gameOver? finalScene))