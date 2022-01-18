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
 * Complete the 'plusMinus' function below.
 *
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

fun Double.roundFormat(digits: Int) = String.format("%.${digits}f", this)

fun plusMinus(arr: Array<Int>): Unit {
    // Write your code here
    var positive = 0.0
    var negative = 0.0
    var zero = 0.0
    for (a in arr){
        if (a == 0){
            zero += 1
        } else if (a > 0) {
            positive += 1
        } else {
            negative += 1
        }
    }
    println((positive/arr.size).roundFormat(6))
    println((negative/arr.size).roundFormat(6))
    println((zero/arr.size).roundFormat(6))
}

fun main() {
    val n = readLine()!!.trim().toInt()
    
    val arr = readLine()!!.trimEnd().split(" ").map{ it.toInt() }.toTypedArray()

    plusMinus(arr)
}
