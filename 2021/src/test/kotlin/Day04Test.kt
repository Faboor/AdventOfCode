import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.api.Test
import strikt.api.expectThat
import strikt.assertions.isEqualTo
import utils.Input

internal class Day04Test {

  private val input = Input("day04")

  @Test
  fun part1Test() {
    expectThat(Day04.part1(input)).isEqualTo(4512)
  }

  @Test
  fun part2Test() {
    expectThat(Day04.part2(input)).isEqualTo(1924)
  }
}