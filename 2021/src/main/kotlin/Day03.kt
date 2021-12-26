import utils.Input

class Day03 private constructor() {
  companion object {
    fun part1(input: Input): Int {
      var count = 0
      val length = input.lineSequence().first().length
      val gammaRate = input.lineSequence()
        .onEach { count++ }
        .fold(IntArray(length)) { counts, value ->
          value.forEachIndexed { i, char -> if (char == '1') counts[i]++ }
          counts
        }.map { if (it > count / 2) 1 else 0 }
        .reduce { acc, it -> (acc shl 1) or it }
      val epsilonRate = (gammaRate.inv() and ((1 shl length) - 1))
      return gammaRate * epsilonRate
    }

    fun part2(input: Input): Int {
      val all = input.lineSequence().toList()
      val oxygen = filterDown(all, true)
      val co2 = filterDown(all, false)
      return oxygen * co2
    }

    private fun filterDown(
      initial: List<String>,
      keepMostCommon: Boolean
    ): Int {
      val remaining = initial.toMutableList()
      var position = 0
      while (remaining.size > 1) {
        var countOnes = 0
        remaining.forEach { if (it[position] == '1') countOnes++ }
        val toKeep =
          if (countOnes >= remaining.size / 2.0)
              (if (keepMostCommon) '1' else '0')
          else (if (keepMostCommon) '0' else '1')
        remaining.retainAll { it[position] == toKeep }
        position++
      }
      return remaining.single()
        .fold(0) { acc, it -> (acc shl 1) or it.minus('0') }
    }
  }
}

fun main() {
  val input = Input("day03")
  println(Day03.part1(input))
  println(Day03.part2(input))
}