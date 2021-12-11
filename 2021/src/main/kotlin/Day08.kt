import utils.Input
import kotlin.streams.asStream
import kotlin.streams.toList

class Day08 private constructor() {
  companion object {
    fun part1(input: Input) =
      input.lineSequence()
        .map { it.splitToSequence(" | ").last() }
        .flatMap { it.splitToSequence(' ') }
        .count { it.length != 5 && it.length != 6 }

    private fun String.difference(other: String) =
      this.toSet().minus(other.toSet())
    private fun String.intersect(other: String) =
      this.toSet().intersect(other.toSet())

    private fun decode(encryptedNumbers: List<String>): List<Set<Char>> {
      val one = encryptedNumbers.single { it.length == 2}
      val four = encryptedNumbers.single { it.length == 4 }
      val seven = encryptedNumbers.single { it.length == 3 }
      val eight = encryptedNumbers.single { it.length == 7 }

      val zeroSixOrNine = encryptedNumbers.filter { it.length == 6 }
      val nine = zeroSixOrNine.single { it.intersect(four).size == 4 }
      val six = zeroSixOrNine.single { seven.difference(it).isNotEmpty() }
      val zero = zeroSixOrNine.single { it != six && it != nine }

      val e = "abcdefg".single { it !in nine }
      val twoThreeOrFive = encryptedNumbers.filter { it.length == 5 }
      val two = twoThreeOrFive.single { it.contains(e) }
      val three = twoThreeOrFive.single { it.intersect(two).size == 4 }
      val five = twoThreeOrFive.single { it != two && it != three }

      return listOf(zero, one, two, three, four, five, six, seven, eight, nine)
        .map { it.toSet() }
    }

    fun part2(input: Input) =
      input.lineSequence()
        .map { line -> line.split(" | ").map { it.split(' ') } }
        .sumOf {
          val decoded = decode(it.first())
          it.last()
            .map { encrypted -> decoded.indexOf(encrypted.toSet()) }
            .reduce { acc, digit -> acc * 10 + digit }
        }
  }
}

fun main() {
  val input = Input("day08")
  println(Day08.part1(input))
  println(Day08.part2(input))
}