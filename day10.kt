import java.io.File
import java.io.InputStream

fun main() {
    // val file_name = "day10_simple.input"
    // val file_name = "day10_test.input"
    val file_name = "day10.input"
    val inputStream: InputStream = File(file_name).inputStream()
    val lineList = mutableListOf<String>()

    inputStream.bufferedReader().forEachLine { lineList.add(it) }

    var cycle: Int = 0
    var x: Int = 1
    var cycle_values = mutableListOf<Pair<Int, Int>>()

    lineList.forEach {
        var instruction = it
        var value = 0
        if (it.contains(" ")) {
            val parts = it.split(" ")
            instruction = parts[0]
            value = parts[1].toInt()
        }

        when (instruction) {
            "noop" -> {
                cycle++
                cycle_values.add(Pair(cycle, x))
            }
            "addx" -> {
                cycle++
                cycle_values.add(Pair(cycle, x))
                cycle++
                cycle_values.add(Pair(cycle, x))
                x += value
            }
        }
    }

    var i = 20
    var total_signal_strength = 0
    while (i < cycle_values.size) {
        val (cycle_number, value) = cycle_values.get(i-1)
        val signal_strength = cycle_number * value
        // println("$cycle_number, $value, $signal_strength")
        total_signal_strength += signal_strength
        i += 40
    }
    println(total_signal_strength)
}
