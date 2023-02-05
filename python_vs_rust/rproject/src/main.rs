use std::thread;
use std::time::Instant;
use num_cpus;

fn test_function() {
    // A simple function to test
    let x = (0..1000000).map(|x| x as u64 * x as u64).collect::<Vec<_>>();
}

fn main() {
    let number_of_threads = num_cpus::get();
    let mut threads = vec![];

    for i in 0..number_of_threads {
        let i = i;
        threads.push(thread::spawn(move || {
            let start_time = Instant::now();
            test_function();
            let end_time = Instant::now();

            let execution_time = end_time - start_time;
            println!("Thread ID: {}", i);
            println!("Execution time: {:?}", execution_time);
        }));
    }

    for thread in threads {
        let _ = thread.join();
    }
}
