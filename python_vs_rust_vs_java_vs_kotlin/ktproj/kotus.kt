import java.time.Instant
import java.util.concurrent.ExecutorService
import java.util.concurrent.Executors

class TestFunction(private val threadId: Int) : Runnable {
    override fun run() {
        val x = mutableListOf<Long>()
        for (i in 0 until 1000000) {
            x.add(i * i.toLong())
        }
        println("Thread ID: $threadId")
    }
}

fun main() {
    val numberOfThreads = Runtime.getRuntime().availableProcessors()
    val executorService = Executors.newFixedThreadPool(numberOfThreads)
    val startTime = Instant.now()
    for (i in 0 until numberOfThreads) {
        executorService.execute(TestFunction(i + 1))
    }
    executorService.shutdown()
    while (!executorService.isTerminated) {}
    val endTime = Instant.now()
    println("Execution time: ${endTime.toEpochMilli() - startTime.toEpochMilli()}ms")
}
