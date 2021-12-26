import utils.Input

class Day05 private constructor() {
  companion object {
    data class Dir(val dx: Int, val dy: Int) {
      operator fun plus(other: Dir) = Dir(dx + other.dx, dy + other.dy)
    }

    data class Point(val x: Int, val y: Int) {
      operator fun plus(dir: Dir) = Point(x + dir.dx, y + dir.dy)
    }

    data class Line(val start: Point, val end: Point) : Iterable<Point> {
      val dir = Dir(
        (end.x - start.x).coerceIn(-1, 1),
        (end.y - start.y).coerceIn(-1, 1),
      )

      override fun iterator() = object : Iterator<Point> {
        var current = start
        override fun hasNext() = current != end + dir
        override fun next() = current.also { current += dir }
      }
    }

    private const val SIZE = 1000

    private fun Input.asLines() = lineSequence()
      .flatMap { it.splitToSequence(" -> ") } // to point strings
      .flatMap { it.splitToSequence(',') } // to individual coors
      .map { it.toInt() }
      .chunked(2) { Point(it[0], it[1]) }
      .chunked(2) { Line(it[0], it[1]) }

    private operator fun Array<IntArray>.get(point: Point) =
      get(point.y)[point.x]

    private operator fun Array<IntArray>.set(point: Point, value: Int) {
      get(point.y)[point.x] = value
    }

    private fun countIntersections(linesSequence: Sequence<Line>): Int {
      val board = Array(SIZE) { IntArray(SIZE) }
      return linesSequence
        .flatMap { it.iterator().asSequence() }
        .onEach { board[it] += 1 }
        .sumOf { if (board[it] == 2) 1 else 0 as Int }
    }

    fun part1(input: Input): Int {
      return countIntersections(
        input.asLines().filter { it.dir.dx == 0 || it.dir.dy == 0 })
    }

    fun part2(input: Input): Int {
      return countIntersections(input.asLines())
    }
  }
}

fun main() {
  val input = Input("day05")
  println(Day05.part1(input))
  println(Day05.part2(input))
}