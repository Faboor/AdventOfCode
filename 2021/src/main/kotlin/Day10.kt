import utils.Input
import java.util.*

class Day10 private constructor() {
  companion object {

    private val opening = mapOf(
      '(' to ')',
      '[' to ']',
      '{' to '}',
      '<' to '>',
    )

    fun part1(input: Input) = input.lineSequence()
      .map {
        val stack = Stack<Char>()
        for (c in it) {
          if (c in opening) {
            stack.push(opening[c])
          } else if (stack.pop() != c) {
            return@map c
          }
        }
        ' '
      }
      .sumOf {
        when (it) {
          ')' -> 3
          ']' -> 57
          '}' -> 1197
          '>' -> 25137
          else -> 0
        } as Int
      }

    fun part2(input: Input) = input.lineSequence()
      .map {
        val stack = Stack<Char>()
        for (c in it) {
          if (c in opening) {
            stack.push(opening[c])
          } else if (stack.pop() != c) {
            return@map listOf()
          }
        }
        stack
      }.filter { it.isNotEmpty() }
      .map {
        it.foldRight(0L) { c, acc ->
          acc * 5 + when (c) {
            ')' -> 1
            ']' -> 2
            '}' -> 3
            '>' -> 4
            else -> 0
          }
        }
      }.sorted()
      .toList()
      .let { it[it.size / 2] }
  }
}

fun main() {
  val input = Input("day10")
  println(Day10.part1(input))
  println(Day10.part2(input))
}