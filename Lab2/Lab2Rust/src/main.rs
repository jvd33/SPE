extern crate time;
use time::PreciseTime;


fn recursive_fib(x: i32) -> i32 { 
    if x < 2 { 
        return x
    }
    recursive_fib(x - 1) + recursive_fib(x - 2)
}

fn stack_fib(n: i32) -> i32 { 
    let mut stack = vec![n];
    let mut result = 0;
    while stack.len() > 0 { 
        let x = stack.pop().unwrap();
        if x < 2 { 
            result += x
        } else { 
            stack.push(x - 1);
            stack.push(x - 2);
        }
    }
     
    result
}

fn super_digit_recursive(n: i32, k: i32) -> i32 { 
    if n.to_string().len() <= 1 { 
        return n
    }
    let mut x = 0;
    for c in n.to_string().chars() { 
        x += c as i32 - '0' as i32
    }
    super_digit_recursive(x * k, 1)
}

fn super_digit_stack(n: i32, mut k: i32) -> i32 { 
    let mut result = 0;
    let mut stack = vec![n];
    while stack.len() > 0 { 
        let x = stack.pop().unwrap();
        if x.to_string().len() <= 1 { 
            result += x;
        } else { 
            for c in x.to_string().chars() { 
                result += c as i32 - '0' as i32
            }
            stack.push(result * k);
            k = 1;
            result = 0;
        }
    }
    result
}

fn main() {
    let f = 20;
    let s = 12345;
    let x = 3;
    
    let mut start = PreciseTime::now();
    println!("{}", recursive_fib(f));
    let mut end = PreciseTime::now();
    println!("{}", start.to(end));
    
    start = PreciseTime::now();
    println!("{}", stack_fib(f));
    end = PreciseTime::now();
    println!("{}", start.to(end));
    
    start = PreciseTime::now();
    println!("{}", super_digit_recursive(s, x));
    end = PreciseTime::now();
    println!("{}", start.to(end));
    
    start = PreciseTime::now();
    println!("{}", super_digit_stack(s, x));
    end = PreciseTime::now();
    println!("{}", start.to(end));
}
