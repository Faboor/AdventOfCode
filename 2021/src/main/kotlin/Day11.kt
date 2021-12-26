import utils.Input
import java.util.*
import kotlin.collections.ArrayList

class Day11 private constructor() {
  companion object {

    fun part1(input: Input): Int {
      val board = Board(input)
      return (0 until 100).sumOf { board.doStep() }
    }

    fun part2(input: Input) =
      generateSequence(Board(input)) { it }
        .takeWhile { board -> board.doStep() < board.width * board.height }
        .count() + 1
  }

  private class Board(input: Input) {
    private val board = ArrayList<IntArray>().apply {
      input.lineSequence().forEach {
        add(it.map(Char::digitToInt).toIntArray())
      }
    }
    val width = board[0].size
    val height = board.size
    private val flashed = mutableSetOf<Pair<Int, Int>>()

    private operator fun ArrayList<IntArray>.get(position: Pair<Int, Int>) =
      get(position.second)[position.first]

    private operator fun ArrayList<IntArray>.set(
      position: Pair<Int, Int>, value: Int
    ) {
      get(position.second)[position.first] = value
    }

    fun doStep(): Int {
      flashed.clear()
      val from = LinkedList<Pair<Int, Int>>()
      val mightFlash = object : Iterator<Pair<Int, Int>> {
        val baseIterator = (0 until height).flatMap { y ->
          (0 until width).map { x -> Pair(x, y) }
        }.iterator()
        val queue = LinkedList<Pair<Int, Int>>()

        override fun hasNext() = queue.isNotEmpty() || baseIterator.hasNext()

        override fun next(): Pair<Int, Int> =
          if (queue.isNotEmpty()) queue.pop() else baseIterator.next()

        fun push(item: Pair<Int, Int>) = queue.push(item)
      }
      for (candidate in mightFlash) {
        if (candidate in flashed) {
          continue
        }
        if (board[candidate] >= 9) {
          flashed.add(candidate)
          board[candidate] = 0
          neighbors(candidate).forEach {
            mightFlash.push(it); from.push(
            candidate
          )
          }
        } else {
          board[candidate] += 1
        }
      }
      return flashed.size
    }

    private fun neighbors(position: Pair<Int, Int>) =
      (position.second + 1 downTo position.second - 1).flatMap { y ->
        (position.first + 1 downTo position.first - 1).map { x -> Pair(x, y) }
      }.filter { it.first in 0 until width && it.second in 0 until height }
  }
}

fun main() {
  val input = Input("day11")
  println(Day11.part1(input))
  println(Day11.part2(input))
}