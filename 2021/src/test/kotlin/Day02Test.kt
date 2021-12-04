import org.junit.jupiter.api.Test
import strikt.api.expectThat
import strikt.assertions.isEqualTo
import utils.Input

class Day02Test {

  private val input = Input("day02")

  @Test
  fun part1() {
    expectThat(Day02.part1(input)).isEqualTo(150)
  }

  @Test
  fun part2() {
    expectThat(Day02.part2(input)).isEqualTo(900)
  }
}