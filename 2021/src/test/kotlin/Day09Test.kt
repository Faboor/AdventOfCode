import org.junit.jupiter.api.Test
import strikt.api.expectThat
import strikt.assertions.isEqualTo
import utils.Input

internal class Day09Test {

  private val input = Input("day09")

  @Test
  fun part1Test() {
    expectThat(Day09.part1(input)).isEqualTo(15)
  }

  @Test
  fun part2Test() {
    expectThat(Day09.part2(input)).isEqualTo(1134)
  }
}