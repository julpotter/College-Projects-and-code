#[derive(Copy,Clone)]
enum Primitive {
Add,
Multiply,
Subtract,
Number(i32)
}
fn evaluate(array: Vec<Primitive>) -> i32 {
    let element = &array[0];
    let mut iter = array.iter();
    iter.next();

match element {
    Primitive::Add => {iter.fold(0, |total, next|
    total + evaluate(vec![*next]))},
    Primitive::Multiply => {iter.fold(1, |total, next|
    total * evaluate(vec![*next]))},
    Primitive::Number(val) => *val,
    Primitive::Subtract => {
        iter.next();
        iter.fold(evaluate(vec![array[1]]), |total, next|
    total - evaluate(vec![*next]))},
}

}
fn main() {
    let mut primitives = Vec::new();
    primitives.push(Primitive::Subtract);
    primitives.push(Primitive::Number(10));
    primitives.push(Primitive::Number(4));
    primitives.push(Primitive::Number(5));
    let result = evaluate(primitives);
    println!("result was {}", result);
}
