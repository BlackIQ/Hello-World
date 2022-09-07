package sample api;

fn Fibonacci(n: i32, a: i32, b: i32) -> i32 {
    Print("{0} ", a);
    if (n == 0) {
        return a;
    }
    return Fibonacci(n - 1, b, a + b);
}


fn Main() -> i32 {
    var n: i32 = 6;
    let nthFibNumber : auto = Fibonacci(n, 1, 1);
    Print("*****");
    Print("(N+1)th fibonacci number : {0}", nthFibNumber);
    return nthFibNumber;
}