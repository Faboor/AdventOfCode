import utils.Input

class Day02 private constructor() {
  companion object {
    fun part1(input: Input) = toDeltaPairSequence(input)
      .reduce { prev, next ->
        Pair(prev.first + next.first, prev.second + next.second)
      }.run { first * second }

    fun part2(input: Input) = toDeltaPairSequence(input)
      .fold(Triple(0, 0, 0)) { acc, delta ->
        Triple(
          acc.first + delta.first,
          acc.second + delta.second,
          acc.third + (acc.first * delta.second)
        )
      }.run { second * third }

    private fun toDeltaPairSequence(input: Input) =
      input.lineSequence()
        .map { it.split(" ") }
        .map { Pair(it[0], it[1].toInt()) }
        .map {
          when (it.first) {
            "forward" -> Pair(0, it.second)
            "down" -> Pair(it.second, 0)
            "up" -> Pair(-it.second, 0)
            else -> throw IllegalArgumentException("Unexpected command '${it.first}'")
          }
        }
  }
}

fun main() {
  val input = Input("day02")
  println(Day02.part1(input))
  println(Day02.part2(input))
}

