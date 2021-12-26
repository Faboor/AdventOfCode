import org.junit.jupiter.api.Test
import strikt.api.expectThat
import strikt.assertions.isEqualTo
import utils.Input

internal class Day11Test {

  private val input = Input("day11")

  @Test
  fun part1Test() {
    expectThat(Day11.part1(input)).isEqualTo(1656)
  }

  @Test
  fun part2Test() {
    expectThat(Day11.part2(input)).isEqualTo(195)
  }
}