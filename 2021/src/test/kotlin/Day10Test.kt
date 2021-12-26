import org.junit.jupiter.api.Test
import strikt.api.expectThat
import strikt.assertions.isEqualTo
import utils.Input

internal class Day10Test {

  private val input = Input("day10")

  @Test
  fun part1Test() {
    expectThat(Day10.part1(input)).isEqualTo(26397)
  }

  @Test
  fun part2Test() {
    expectThat(Day10.part2(input)).isEqualTo(288957)
  }
}