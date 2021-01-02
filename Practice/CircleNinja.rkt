;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname CircleNinja) (read-case-sensitive #t) (teachpacks ((lib "universe.rkt" "teachpack" "2htdp") (lib "image.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #t #t none #f ((lib "universe.rkt" "teachpack" "2htdp") (lib "image.rkt" "teachpack" "2htdp")) #f)))
(define GBWIDTH 1200) ; Game board width
(define GBHEIGHT 800) ; Game board height
(define-struct myTri (posn size dx dy))
(define-struct myCirc (posn size dx dy))
(define-struct mySq (posn size dx dy))

; WorldState
; ...
; ...
; triangleList is a list of myTri structures
; scores is a number, giving the current score
; ...
(define-struct WS (circleList squareList triangleList
                              score timer numCircleClicked numSquareClicked numTriClicked))

; WorldState -> Image
(define (render ws)
  (above (render-gameboard ws) (render-statusarea ws)))

; WorldState -> Image
; Draws the shape area of our game
(define (render-gameboard ws)
  (local
    [(define cl (WS-circleList ws))
     (define tl (WS-triangleList ws))
     (define sl (WS-squareListList ws))]
    (draw-triangles
     (draw-squares
      (draw-circle (empty-scene GBWIDTH GBHEIGHT) cl) sl) tl)))

; Image, List of Posn -> Image
; renders the triangles in lotri onto the image img
(define (draw-triangles img lotri) (foldl (lambda (tri img) (underlay/xy img
                                                                         (posn-x (myTri-pos tri))
                                                                         (posn-y (myTri-pos tri))
                                                                         (triangle (myTri-size tri) 'outline 'magenta))) img lotri))

; Image, List of Posn -> Image
; renders the circles in lop locations onto the image img
(define (draw-circles img lop) (foldl (lambda (pos img) (underlay/xy img (posn-x pos) (posn-y pos) (triangle 40 'outline 'blue))) img lop))

; Image, List of Posn -> Image
; renders the squares in lop locations onto the image img
(define (draw-squares img lop) (foldl (lambda (pos img) (underlay/xy img (posn-x pos) (posn-y pos) (triangle 40 'outline 'brown))) img lop))

(define (render-statusarea ws) ws)

(define (tock ws)
  (update-timer (move-triangles (move-circles (move-squares ws))))

  )

; WorldState -> WorldState
; Moves the squares in the WorldState and deletes those that
; have timed out
(define (move-squares ws)
  (local
    [(define los (WS-squareList ws))]
    (make-WS (WS-circleList ws)
             (map tockOneSquare los)
             (WS-triangleList ws) ...)))

(big-bang (to-draw render) (on-tick tock) ) 