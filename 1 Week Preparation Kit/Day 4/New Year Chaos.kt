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
 * Complete the 'minimumBribes' function below.
 *
 * The function accepts INTEGER_ARRAY q as parameter.
 */
    
fun minimumBribes(q: Array<Int>): Unit {
    // Write your code here
    val mapNumbers = mutableMapOf<Int, Int>()
    var count = 0
    var isCaos = false
    for (current in 1 until q.size){
        var i = current
        while (i>0 && q[i-1] > q[i]) {
            if (mapNumbers.containsKey(q[i-1])){
                if ((mapNumbers[q[i-1]] ?: 0) > 1){
                    println("Too chaotic")
                    isCaos = true
                    break
                }
                mapNumbers[q[i-1]] = (mapNumbers[q[i-1]] ?: 0) + 1 
            } else {
                mapNumbers[q[i-1]] = 1
            }
            val temp = q[i]
            q[i] = q[i-1]
            q[i-1] = temp
            count ++
            i--
        }
        if (isCaos){
            break
        }
    }
    if (!isCaos){
        println(count)   
    }
}


fun main(args: Array<String>) {
    val t = readLine()!!.trim().toInt()

    for (tItr in 1..t) {
        val n = readLine()!!.trim().toInt()

        val q = readLine()!!.trimEnd().split(" ").map{ it.toInt() }.toTypedArray()

        minimumBribes(q)
    }
}
