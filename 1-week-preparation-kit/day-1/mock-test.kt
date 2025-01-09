
fun findMedian(array: Array<Int>): Int {
    val sortedArray = array.sortedArray()
    val middle = sortedArray.size / 2
    return if (sortedArray.size % 2 == 0) {
        (sortedArray[middle] + sortedArray[middle - 1]) / 2
    } else {
        sortedArray[middle]
    }
}

fun main() {
    val array = arrayOf(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    println(findMedian(array))
}