import utils.Input
import kotlin.collections.ArrayList
import kotlin.collections.HashMap
import kotlin.collections.HashSet

private typealias Cave = String

class Day12 private constructor() {
  companion object {

    private fun Input.asConnectionsMap(): Map<Cave, List<Cave>> =
      HashMap<Cave, MutableList<Cave>>().apply {
        lineSequence()
          .map { it.split("-") }
          .flatMap { listOf(it, it.reversed()) }
          .forEach { getOrPut(it[0]) { ArrayList() }.add(it[1]) }
      }

    private fun Cave.isSmall() = this == lowercase()

    private fun calculatePaths(
      connections: Map<Cave, List<Cave>>,
      cave: Cave = "start",
      visitedCaves: MutableSet<Cave> = HashSet(),
      canVisitTwice: Boolean = false,
    ): Int {
      if (cave == "end") {
        return 1
      }
      var isSecondVisit = false
      if (cave.isSmall() && !visitedCaves.add(cave)) {
        if (!canVisitTwice || cave == "start") {
          return 0
        }
        isSecondVisit = true
      }

      var counter = 0
      for (nextCave in connections.getValue(cave)) {
        counter += calculatePaths(
          connections,
          nextCave,
          visitedCaves,
          canVisitTwice && !isSecondVisit,
        )
      }
      if (!isSecondVisit) {
        visitedCaves.remove(cave)
      }
      return counter
    }

    fun part1(input: Input) = calculatePaths(input.asConnectionsMap())

    fun part2(input: Input) = calculatePaths(
      input.asConnectionsMap(),
      canVisitTwice = true
    )
  }
}

fun main() {
  val input = Input("day12")
  println(Day12.part1(input))
  println(Day12.part2(input))
}