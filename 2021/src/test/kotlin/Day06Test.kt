import org.junit.jupiter.api.Test
import strikt.api.expectThat
import strikt.assertions.isEqualTo
import utils.Input

internal class Day06Test {

  private val input = Input("day06")

  @Test
  fun part1Test() {
    expectThat(Day06.part1(input)).isEqualTo(5934)
  }

  @Test
  fun part2Test() {
    expectThat(Day06.part2(input)).isEqualTo(26984457539L)
  }
}