import utils.Input

class Day04 private constructor() {
  companion object {
    private fun prepNumbersAndBoards(
      input: Input,
    ): Pair<Sequence<Int>, MutableList<Board>> {
      val lineIterator =
        input.lineSequence().filter(String::isNotBlank).iterator()
      val numberSequence =
        lineIterator.next().splitToSequence(',').map(String::toInt)
      val boards =
        lineIterator.asSequence().windowed(5, 5).map(::Board).toMutableList()
      return Pair(numberSequence, boards)
    }

    fun part1(input: Input): Int {
      val (numberSequence, boards) = prepNumbersAndBoards(input)
      for (number in numberSequence) {
        for (board in boards) {
          if (board.offer(number)) {
            return number * board.sumRemaining
          }
        }
      }
      throw AssertionError("No bingo!")
    }

    fun part2(input: Input): Int {
      val (numberSequence, boards) = prepNumbersAndBoards(input)
      for (number in numberSequence) {
        val lastBoard = boards.first();
        boards.removeAll { it.offer(number) }
        if (boards.isEmpty()) {
          return number * lastBoard.sumRemaining
        }
      }
      throw AssertionError("Not all boards got a bingo")
    }
  }

  class Board(serializedBoard: List<String>) {
    private val board = Array(5) { IntArray(5) }
    private val numbers = HashMap<Int, Pair<Int, Int>>()
    var sumRemaining: Int = 0
      private set

    init {
      serializedBoard.forEachIndexed { row, serialisedRow ->
        serialisedRow.splitToSequence(' ').filter { it.isNotBlank() }
          .map { it.toInt() }.forEachIndexed { col, n ->
            sumRemaining += n
            numbers[n] = Pair(row, col)
            board[row][col] = n
          }
      }
    }

    fun offer(n: Int): Boolean {
      return numbers[n]?.let { (row, col) ->
        board[row][col] = -1
        sumRemaining -= n
        (0..4).all { board[row][it] == -1 } || (0..4).all { board[it][col] == -1 }
      } ?: false
    }
  }
}

fun main() {
  val input = Input("day04")
  println(Day04.part1(input))
  println(Day04.part2(input))
}