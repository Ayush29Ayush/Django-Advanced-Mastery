import multiprocessing
import threading
import time

#! 1. What problem do threads solve?
# Threads solve the problem of concurrent execution of multiple tasks, allowing a program to perform multiple operations simultaneously.


#! 2. How to create a thread with available methods like run, start, join
class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print(f"{self.name} started")
        time.sleep(2)  # Simulate work
        print(f"{self.name} finished")


# Create threads
thread1 = MyThread("Thread 1")
thread2 = MyThread("Thread 2")

# Start threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()


#! 3. How to pass arguments to a thread
def worker(name, delay):
    print(f"{name} is working for {delay} seconds")


thread_with_args = MyThread("Worker Thread")
thread_with_args.run = lambda: worker("Worker", 3)


#! 4. Difference between threads and processes
def cpu_bound_task():
    result = 0
    for i in range(10**8):
        result += i


thread1 = threading.Thread(target=cpu_bound_task)
process1 = multiprocessing.Process(target=cpu_bound_task)

thread1.start()
process1.start()

thread1.join()
process1.join()

print("Threads vs Processes")


#! 5. Difference between run and start of a thread
class ThreadWithRunAndStart(threading.Thread):
    def run(self):
        print("Thread run method called")

    def start(self):
        print("Thread start method called")


thread = ThreadWithRunAndStart()
thread.start()


#! 6. How to create threads using classes
class WorkerThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print(f"{self.name} is working")


worker_threads = [
    WorkerThread("Thread 1"),
    WorkerThread("Thread 2"),
    WorkerThread("Thread 3"),
]

for thread in worker_threads:
    thread.start()

# Wait for all threads to finish
for thread in worker_threads:
    thread.join()

print("All threads finished")


#! Additional comparison of threads and processes
def io_bound_task():
    time.sleep(2)  # Simulate I/O operation


# Using threads for IO-bound task
thread_io = threading.Thread(target=io_bound_task)
thread_io.start()
thread_io.join()

# Using process for IO-bound task (same performance as threads for IO-bound tasks)
process_io = multiprocessing.Process(target=io_bound_task)
process_io.start()
process_io.join()

print("Threads vs Processes for IO-bound tasks:")
print("Both threads and processes perform similarly for IO-bound tasks.")

# CPU-bound tasks show better parallelism with processes
cpu_result = multiprocessing.cpu_count()
print(f"Number of CPUs: {cpu_result}")

if cpu_result > 1:
    # Create multiple processes to utilize multiple CPUs
    processes = []
    for i in range(cpu_result):
        p = multiprocessing.Process(target=cpu_bound_task)
        processes.append(p)
        p.start()

    # Wait for all processes to complete
    for p in processes:
        p.join()

    print("Processes completed successfully.")
else:
    print("Only one CPU available, cannot demonstrate multi-CPU parallelism.")
