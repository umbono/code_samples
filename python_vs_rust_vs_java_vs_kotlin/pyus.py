import time
import threading
import psutil

def test_function():
    # A simple function to test
    x = [i**2 for i in range(1000000)]

# if __name__ == '__main__':
#     process = psutil.Process()
#     threads = []
#     start_time = time.time()
#     for i in range(5):
#         t = threading.Thread(target=test_function)
#         threads.append(t)
#         t.start()
#     for t in threads:
#         t.join()
#     end_time = time.time()
#     print("Memory usage:", process.memory_info().rss / 1024 / 1024, "MB")
#     print("CPU usage:", process.cpu_percent(), "%")
#     print("Threads:", process.num_threads())
#     print("Execution time:", end_time - start_time, "seconds")

if __name__ == '__main__':
    process = psutil.Process()
    start_time = time.time()
    test_function()
    end_time = time.time()
    print("Memory usage:", process.memory_info().rss / 1024 / 1024, "MB")
    print("CPU usage:", process.cpu_percent(), "%")
    print("Threads:", process.num_threads())
    print("Execution time:", (end_time - start_time) * 1000, "milliseconds")

