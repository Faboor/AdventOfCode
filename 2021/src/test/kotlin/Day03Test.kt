import org.junit.jupiter.api.Test
import strikt.api.expectThat
import strikt.assertions.isEqualTo
import utils.Input

class Day03Test {

  private val input = Input("day03")

  @Test
  fun part1() {
    expectThat(Day03.part1(input)).isEqualTo(198)
  }

  @Test
  fun part2() {
    expectThat(Day03.part2(input)).isEqualTo(230)
  }
}