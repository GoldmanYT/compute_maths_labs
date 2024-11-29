import kotlin.math.cos
import kotlin.math.sin


fun f(x: Double): Double {
    return cos(0.8 * x * x + 1) / (1.2 + sin(x + 0.5))
}


fun y(x: Double): Double {
    return x * x
}


fun rectInt(
    func: (Double) -> Double,
    a: Double,
    b: Double,
    n: Int
): Double {
    val h = (b - a) / n
    var ans = 0.0
    for (i in 0..<n) {
        val x1 = a + h * i
        val x2 = a + h * (i + 1)
        val c = (x1 + x2) / 2
        ans += func(c) * h
    }
    return ans
}

fun simsonInt(
    func: (Double) -> Double,
    a: Double,
    b: Double,
    n_: Int
): Double {
    val n = n_ + n_ % 2
    val h = (b - a) / n
    val y = mutableListOf<Double>()
    for (i in 0..n) {
        y.add(func(a + i * h))
    }
    val m = n / 2
    var ans = (y[0] + y[2 * m] + 4 * y[1]) * h / 3
    for (i in 2..m) {
        ans += (4 * y[2 * i - 1] + 2 * y[2 * i - 2]) * h / 3
    }
    return ans
}


fun main() {
    println(rectInt(::f, 0.4, 1.4, 20))
    println(simsonInt(::f, 0.4, 1.4, 20))
    println()
    println(rectInt(::y, 0.0, 1.0, 10))
    println(simsonInt(::y, 0.0, 1.0, 10))
}
