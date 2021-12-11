import org.junit.jupiter.api.Test
import strikt.api.expectThat
import strikt.assertions.isEqualTo
import utils.Input

internal class Day08Test {

  private val input = Input("day08")

  @Test
  fun part1Test() {
    expectThat(Day08.part1(input)).isEqualTo(26)
  }

  @Test
  fun part2Test() {
    expectThat(Day08.part2(input)).isEqualTo(66582)
  }
}