import utils.Input
import kotlin.text.StringBuilder

class Day13 private constructor() {
  companion object {

    private enum class Fold {
      HORIZONTAL, VERTICAL
    }

    private fun getDotsAndFolds(
      input: Input,
      foldLimit: Int,
    ): Pair<Iterable<Pair<Int, Int>>, Sequence<Pair<Fold, Int>>> {
      val lineIterator = input.lineSequence().iterator()
      val dots = lineIterator.asSequence().takeWhile { it.isNotBlank() }
        .map { it.split(',') }.map { Pair(it[0].toInt(), it[1].toInt()) }
        .toList()
      val folds = lineIterator.asSequence().take(foldLimit)
        .map { it.removePrefix("fold along ").split("=") }.map {
          Pair(
            if (it[0] == "x") Fold.HORIZONTAL else Fold.VERTICAL, it[1].toInt()
          )
        }
      return Pair(dots, folds)
    }

    private fun doFolds(input: Input, nFolds: Int): Set<Pair<Int, Int>> {
      val (dots, folds) = getDotsAndFolds(input, nFolds)
      return folds.fold(dots) { leftOverDots, (direction, n) ->
        leftOverDots.map {
          val (x, y) = it
          when (direction) {
            Fold.HORIZONTAL -> if (x > n) Pair(n - (x - n), y) else it
            Fold.VERTICAL -> if (y > n) Pair(x, n - (y - n)) else it
          }
        }
      }.toSet()
    }

    fun part1(input: Input) = doFolds(input, 1).size

    fun part2(input: Input) =
      doFolds(input, Int.MAX_VALUE).groupBy { it.second }.entries
        .sortedBy { it.key }.asSequence()
        .map { Pair(it.key, it.value.map { dot -> dot.first }.sorted()) }
        .fold(StringBuilder()) { sb, (lineNum, positions) ->
          sb.appendLine(
            positions.fold(StringBuilder()) { lineSb, current ->
              lineSb.append(" ".repeat(current - lineSb.length)).append("#")
            }
          )
        }.toString()
  }
}

fun main() {
  val input = Input("day13")
  println(Day13.part1(input))
  println(Day13.part2(input))
}