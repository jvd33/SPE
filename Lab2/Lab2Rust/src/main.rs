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

fn super_digit_recursive(mut n: i64, k: i32) -> i64 { 
    n = n.to_string().repeat(k as usize).parse::<i64>().unwrap();
    if n.to_string().len() <= 1 { 
        return n
    }
    let mut x = 0;
    for c in n.to_string().chars() { 
        x += c as i64 - '0' as i64
    }
    super_digit_recursive(x, 1)
}

fn super_digit_stack(mut n: i64, k: i32) -> i64 { 
    n = n.to_string().repeat(k as usize).parse::<i64>().unwrap();
    let mut result = 0;
    let mut stack = vec![n];
    while stack.len() > 0 { 
        let x = stack.pop().unwrap();
        if x.to_string().len() <= 1 { 
            result += x;
        } else { 
            for c in x.to_string().chars() { 
                result += c as i64 - '0' as i64
            }
            stack.push(result);
            result = 0;
        }
    }
    result
}

fn main() {
    let f = 40;
    let s = 12345;
    let x = 3;
    
    //let mut start = PreciseTime::now();
    //println!("{}", recursive_fib(f));
    //let mut end = PreciseTime::now();
    //println!("{}", start.to(end));
    
    let mut start = PreciseTime::now();
    println!("{}", stack_fib(f));
    let mut end = PreciseTime::now();
    println!("{}", start.to(end));
    
    //start = PreciseTime::now();
    //println!("{}", super_digit_recursive(s, x));
    //end = PreciseTime::now();
    //println!("{}", start.to(end));
    
    //start = PreciseTime::now();
    //println!("{}", super_digit_stack(s, x));
    //end = PreciseTime::now();
    //println!("{}", start.to(end));
}
