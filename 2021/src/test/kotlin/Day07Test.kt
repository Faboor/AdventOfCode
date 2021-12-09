import org.junit.jupiter.api.Test
import strikt.api.expectThat
import strikt.assertions.isEqualTo
import utils.Input

internal class Day07Test {

  private val input = Input("day07")

  @Test
  fun part1Test() {
    expectThat(Day07.part1(input)).isEqualTo(37)
  }

  @Test
  fun part2Test() {
    expectThat(Day07.part2(input)).isEqualTo(168)
  }
}