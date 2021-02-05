fn main(){
	let x = f(5);
	println!("The sum of the squares of a+1 and a*2 is {}", x);
	
}

fn f(a: i32) -> i32{
	let x = a + 1;
	let y = a * 2;
	sum_of_squares(x, y)
}

fn sum_of_squares(x: i32, y: i32) -> i32{
	square(x) + square(y)
}

fn square(x: i32) -> i32{
	x * x
}
