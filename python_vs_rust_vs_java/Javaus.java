import java.time.Instant;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

class TestFunction implements Runnable {
    int threadId;
    public TestFunction(int threadId) {
        this.threadId = threadId;
    }

    @Override
    public void run() {
        List < Long > x = new ArrayList < > ();
        for (int i = 0; i < 1000000; i++) {
            x.add((long) i * i);
        }
        System.out.println("Thread ID: " + threadId);
    }

}
public class Javaus {
    public static void main(String[] args) {
        int numberOfThreads = Runtime.getRuntime().availableProcessors();
        ExecutorService executorService = Executors.newFixedThreadPool(numberOfThreads);
        List < Thread > threads = new ArrayList < > ();
        Instant startTime = Instant.now();
        for (int i = 0; i < numberOfThreads; i++) {
            executorService.execute(new TestFunction(i + 1));
        }
        executorService.shutdown();
        while (!executorService.isTerminated()) {}
        Instant endTime = Instant.now();
        System.out.println("Execution time: " + Long.toString(endTime.toEpochMilli() - startTime.toEpochMilli()) + "ms");
    }
}