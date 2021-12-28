import org.junit.jupiter.api.Test
import strikt.api.expectThat
import strikt.assertions.isEqualTo
import utils.Input

internal class Day12Test {

  @Test
  fun part1SmallTest() {
    expectThat(Day12.part1(Input("day12_0"))).isEqualTo(10)
  }

  @Test
  fun part1MediumTest() {
    expectThat(Day12.part1(Input("day12_1"))).isEqualTo(19)
  }

  @Test
  fun part1LargeTest() {
    expectThat(Day12.part1(Input("day12_2"))).isEqualTo(226)
  }

  @Test
  fun part2SmallTest() {
    expectThat(Day12.part2(Input("day12_0"))).isEqualTo(36)
  }

  @Test
  fun part2MediumTest() {
    expectThat(Day12.part2(Input("day12_1"))).isEqualTo(103)
  }
}