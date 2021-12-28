import org.junit.jupiter.api.Test
import strikt.api.expectThat
import strikt.assertions.isEqualTo
import utils.Input

internal class Day13Test {

  private val input = Input("day13")

  @Test
  fun part1Test() {
    expectThat(Day13.part1(input)).isEqualTo(17)
  }

  @Test
  fun part2Test() {
    expectThat(Day13.part2(input)).isEqualTo("""
      #####
      #   #
      #   #
      #   #
      #####
      
    """.trimIndent())
  }
}