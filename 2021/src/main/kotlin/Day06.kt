import utils.Input

class Day06 private constructor() {
  companion object {

    fun pprint(cur: Int, spawns: Map<Int, Int>, new: Map<Int, Int>) {
      val s1 = spawns.asSequence()
        .flatMap { (key, value) -> (1..value).map { (key + 7 - cur % 7) % 7 } }
        .joinToString(",") { it.toString() }
      val s2 = new.asSequence()
        .flatMap { (key, value) -> (1..value).map { (key + 7 - cur % 7) % 7 + 7} }
        .joinToString(",") { it.toString() }
      println("After ${cur.toString().padStart(2)} days: $s1-$s2")
    }

    fun part1(input: Input, days: Int = 80): Long {
      val initPairs = (0..6).map { Pair(it, 0L) }
      val spawnsOnDay = hashMapOf<Int, Long>().apply { putAll(initPairs) }
      val newOnDay = hashMapOf<Int, Long>().apply { putAll(initPairs) }

      input.lineSequence()
        .first()
        .splitToSequence(',')
        .map { it.toInt() }
        .forEach { spawnsOnDay[it] = spawnsOnDay[it]!! + 1 }

      (0 until days).asSequence()
        .forEach {
          val day = it % 7
          val spawnsToday = spawnsOnDay[day]!!
          newOnDay[(day + 2) % 7] = spawnsToday
          spawnsOnDay[day] = spawnsToday + newOnDay[day]!!
          newOnDay[day] = 0
        }

      return spawnsOnDay.values.sum() + newOnDay.values.sum()
    }

    fun part2(input: Input): Long {
      return part1(input, 256)
    }
  }
}

fun main() {
  val input = Input("day06")
  println(Day06.part1(input))
  println(Day06.part2(input))
}