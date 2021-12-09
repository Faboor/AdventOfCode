import utils.Input
import kotlin.math.abs
import kotlin.math.ceil
import kotlin.math.floor
import kotlin.math.round

class Day07 private constructor() {
  companion object {
    private fun getPositions(input: Input) = input.lineSequence()
      .single()
      .splitToSequence(',')
      .map { it.toInt() }
      .toList()

    fun part1(input: Input): Int {
      val positions = getPositions(input)
      val median = positions.sorted().let {
        (it[it.size / 2] + it[(it.size - 1) / 2]) / 2
      }
      return positions.sumOf { abs(it - median) }
    }

    private fun calculateFuel(positions: Iterable<Int>, target: Int) =
      positions.sumOf {
        val n = abs(it - target)
        n * (n + 1) / 2
      }

    fun part2(input: Input): Int {
      val positions = getPositions(input)
      val average = positions.average()
      return sequenceOf(floor(average), ceil(average))
        .minOf { calculateFuel(positions, it.toInt()) }
    }
  }
}

fun main() {
  val input = Input("day07")
  println(Day07.part1(input))
  println(Day07.part2(input))
}