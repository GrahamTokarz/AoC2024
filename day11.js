const fs = require('fs');
fs.readFile('11input.txt', 'utf8', (err, data) => {
//fs.readFile('testcase.txt', 'utf8', (err, data) => {
    lst = data.split(" ");

    col = {}
    for (i = 0; i < lst.length; i++) {
        val = lst[i];
        if (col[val]) {
            col[val] += 1
        } else {
            col[val] = 1
        }
    }

    n = 25
    for (i = 0; i < n; i++) {
        console.log(i)
        ncol = {}
        for (j = 0; j < Object.keys(col).length; j++) {
            v = Object.keys(col)[j]
            if (v == "0") {
                if (ncol["1"])
                    ncol["1"] += col[v]
                else
                    ncol["1"] = col[v]
            } else if (v.length%2 == 0) {
                y = v.substring(0, Math.floor(v.length/2))
                x = parseInt(v.substring(Math.ceil(v.length/2))).toString()
                if (ncol[y])
                    ncol[y] += col[v]
                else
                    ncol[y] = col[v]
                if (ncol[x])
                    ncol[x] += col[v]
                else
                    ncol[x] = col[v]
            } else {
                x = (parseInt(v)*2024).toString()
                if (ncol[x])
                    ncol[x] += col[v]
                else
                    ncol[x] = col[v]
            }
        }
        col = ncol
    }

    out = 0
    for (j = 0; j < Object.keys(col).length; j++) {
        out += col[Object.keys(col)[j]]
    }
    console.log(out)
});