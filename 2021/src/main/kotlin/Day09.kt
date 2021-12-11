import utils.Input
import java.util.*
import kotlin.collections.ArrayList

private typealias Board = ArrayList<IntArray>

class Day09 private constructor() {
  companion object {

    private fun <T> Triple(list: List<T>) = Triple(list[0], list[1], list[2])
    private fun <T, R> zip(
      iterables: Iterable<Sequence<T>>, transform: (List<T>) -> R
    ): Sequence<R> {
      val iterators = iterables.map { it.iterator() }
      return sequence {
        while (iterators.all { it.hasNext() }) {
          yield(transform(iterators.map { it.next() }))
        }
      }
    }

    fun part1(input: Input) = sequence {
        yield(generateSequence { 9 }.windowed(3) { Triple(it) })
        yieldAll(input.lineSequence().map { line ->
          sequence {
            yield(9)
            yieldAll(line.asSequence().map { it.digitToInt() })
            yield(9)
          }.windowed(3) { Triple(it) }
        })
        yield(generateSequence { 9 }.windowed(3) { Triple(it) })
      }.windowed(3)
        .flatMap { zip(it) { zipped -> Triple(zipped) } }
        .filter {
          val mid = it.second.second
          mid < it.first.second
              && mid < it.second.first
              && mid < it.second.third
              && mid < it.third.second
        }.sumOf { it.second.second + 1 }

    private fun board(input: Input, width: Int): Board {
      val board = Board()
      board.add(IntArray(width + 2) { 9 })
      input.lineSequence()
        .map { it.asSequence().map { c -> c.digitToInt() } }
        .forEach {
          val array = IntArray(width + 2).apply {
            set(0, 9)
            set(lastIndex, 9)
          }
          it.forEachIndexed { i, digit -> array[i + 1] = digit}
          board.add(array)
        }
      board.add(IntArray(width + 2) { 9 })
      return board
    }

    private fun LinkedList<Pair<Int, Int>>.add(a: Int, b:Int) = add(Pair(a, b))

    private fun floodFill(x0: Int, y0: Int, board: Board): Int {
      val workQueue = LinkedList<Pair<Int, Int>>().apply { add(x0, y0) }
      var count = 0
      while (workQueue.isNotEmpty()) {
        val (x, y) = workQueue.pop()
        if (board[y][x] != 9) {
          count++
          board[y][x] = 9
          with(workQueue) {
            add(x, y - 1)
            add(x - 1, y)
            add(x, y + 1)
            add(x + 1, y)
          }
        }
      }
      return count
    }

    fun part2(input: Input): Int {
      val width = input.lineSequence().first().length
      val board = board(input, width)
      val height = board.size - 2

      return (1..height + 1).asSequence()
        .flatMap { y ->
          (1..width + 1).map { x ->
            floodFill(x, y, board)
          }
        }.sorted()
        .toList()
        .takeLast(3)
        .reduce { acc, elem -> acc * elem }
    }
  }
}


fun main() {
  val input = Input("day09")
  println(Day09.part1(input))
  println(Day09.part2(input))
}