function calculate(){
    var ans = document.getElementById("answer")

    var a = parseFloat(document.getElementById("A-value").value)
    var b = parseFloat(document.getElementById("B-value").value)
    var c = parseFloat(document.getElementById("C-value").value)
    var d = parseFloat(document.getElementById("D-value").value)

    var sludge_volume = 109.91379 - (0.001717 * a) - (0.000237 * b) + (4.05308 * c) - (17.12600 * d) 
    + (0.000000017472 * a * b) - (0.000125 * a * c) + (0.003618 * a * d) - (0.00000236838 * b * c)
    + (0.000261 * b * d) - (4.28208 * c * d) - (0.000000714638 * a * a) - (0.00000000081293 * b * b)
    + (0.095687 * c * c) + (4.29643 * d * d)

    ans.innerText = sludge_volume
}
