function gen_table(lines){
    let table = document.getElementsByClassName('rwd-table')
    let tableBody = document.createElement("tbody")
    const MAX_COLS = 5 + 1      //number of processes + kernel

    // CREATE table headers
    let row = document.createElement("tr")
    let cell = document.createElement("th")
    let cellText = document.createTextNode(`Kernel`)
    cell.appendChild(cellText)
    row.appendChild(cell)
    for(let j = 0; j < MAX_COLS - 1; j++){
        let cell = document.createElement("th")
        let cellText = document.createTextNode(`Process ${j}`)
        cell.appendChild(cellText)
        row.appendChild(cell)
    }
    tableBody.appendChild(row)

    // CREATE table rows
    for(var line = 0; line < lines.length; line++){
        // only process lines which start with Process - can modify later!
        if(!lines[line].startsWith('Process')) continue;
        let row = document.createElement("tr")
        console.log(lines[line])

        // Create row for kernel
        let cellText, cell
        if(lines[line].startsWith('Process Kernel')){
            cellText = document.createTextNode(lines[line]) 
            cell = document.createElement("td")
            cell.appendChild(cellText)
            row.appendChild(cell)
            tableBody.appendChild(row)
            continue
        }

        // Create row for process excluding column of kernel
        cell = document.createElement("td")
        cellText = document.createTextNode('')
        cell.appendChild(cellText)
        row.appendChild(cell)
        for(let j = 0; j < MAX_COLS - 1; j++){
            let cell = document.createElement("td")
            let cellText
            // find the process who wrote this line
            if (lines[line].startsWith(`Process ${j}`)){
                cellText = document.createTextNode(lines[line])
            }else{
                cellText = document.createTextNode('')
            }
            cell.appendChild(cellText)
            row.appendChild(cell)
        }
        tableBody.appendChild(row)
    }

    table[0].appendChild(tableBody)
}

fetch('log')
    .then(response => response.text())
    .then(text => { 
        lines = text.split('\n')
        console.log(lines)
        gen_table(lines)
    })

