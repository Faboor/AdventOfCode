import utils.Input

fun main() {
  val input = Input("day01")
  println(part1(input))
  println(part2(input))
}

fun part1(input: Input, windowSize: Int = 1): Int = input.lineSequence()
  .map { it.toInt() }
  .windowed(windowSize)
  .map { it.sum() }
  .windowed(2)
  // Cast necessary to resolve sumOf return type ambiguity
  .sumOf { if (it[1] > it[0]) 1 else 0 as Int }

fun part2(input: Input) = part1(input, windowSize = 3)