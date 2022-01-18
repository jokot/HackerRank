import java.io.*
import java.math.*
import java.security.*
import java.text.*
import java.util.*
import java.util.concurrent.*
import java.util.function.*
import java.util.regex.*
import java.util.stream.*
import kotlin.collections.*
import kotlin.comparisons.*
import kotlin.io.*
import kotlin.jvm.*
import kotlin.jvm.functions.*
import kotlin.jvm.internal.*
import kotlin.ranges.*
import kotlin.sequences.*
import kotlin.text.*

/*
 * Complete the 'timeConversion' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

fun timeConversion(s: String): String {
    // Write your code here
    val time = s.split(":")
    val hour = time[0]
    val minute = time[1]
    val second = time[2]
    val ampm = second.substring(second.length - 2, second.length)
    val newSecond = second.substring(0, second.length - 2)
    val newTime = "$hour:$minute:$newSecond"
    return if (ampm == "PM") {
        if (hour == "12") {
            newTime
        } else {
            val newHour = (hour.toInt() + 12).toString()
            "$newHour:$minute:$newSecond"
        }
    } else {
        if (hour == "12") {
            "00:$minute:$newSecond"
        } else {
            newTime
        }
    }
}

fun main(args: Array<String>) {
    val s = readLine()!!

    val result = timeConversion(s)

    println(result)
}
