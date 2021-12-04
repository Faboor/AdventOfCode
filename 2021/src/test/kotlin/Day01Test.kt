import org.junit.jupiter.api.Test

import org.junit.jupiter.api.Assertions.*
import strikt.api.expectThat
import strikt.assertions.isEqualTo
import utils.Input

internal class Day01Test {

  private val input = Input("day01")

  @Test
  fun part1() {
    expectThat(Day01.part1(input)).isEqualTo(7)
  }

  @Test
  fun part2() {
    expectThat(Day01.part2(input)).isEqualTo(5)
  }
}