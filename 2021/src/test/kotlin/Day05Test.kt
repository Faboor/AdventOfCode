import org.junit.jupiter.api.Test
import strikt.api.expectThat
import strikt.assertions.isEqualTo
import utils.Input

internal class Day05Test {

  private val input = Input("day05")

  @Test
  fun part1Test() {
    expectThat(Day05.part1(input)).isEqualTo(5)
  }

  @Test
  fun part2Test() {
    expectThat(Day05.part2(input)).isEqualTo(12)
  }
}