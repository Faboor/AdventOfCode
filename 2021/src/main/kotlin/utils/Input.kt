package utils

import java.io.FileNotFoundException

class Input(day: String) {
  private val filename = "/$day.txt"

  init {
    javaClass.getResource(filename) ?: throw FileNotFoundException(
      "Input file for $day ($filename) does not exist"
    )
  }

  fun lineSequence() =
    javaClass.getResourceAsStream(filename)!!.bufferedReader().lineSequence();

}