const app = document.getElementById('root')
const container = document.createElement('div')
container.setAttribute('class', 'container')
app.appendChild(container)

var request = new XMLHttpRequest()
request.open('GET', 'https://mai-uom-19020.herokuapp.com/japanfixtures/', true)
// request.open('GET', 'http://localhost:8000/japanfixtures/', true)
request.onload = function() {
    console.log("HI")
    var data = JSON.parse(this.response)
    if (request.status >= 200 && request.status < 400) {
        data.forEach(fixture => {
            const card = document.createElement('div')
            card.setAttribute('class', 'card')

            const h1 = document.createElement('h1')
            h1.textContent = fixture.hometeam + ' vs ' + fixture.awayteam

            const p = document.createElement('p')
            fixture.hometeam = fixture.hometeam.substring(0, 300)
            p.textContent = `${fixture.homegoals} : ${fixture.awaygoals}`

            container.appendChild(card)
            card.appendChild(h1)
            card.appendChild(p)
        })
    } else {
        const errorMessage = document.createElement('marquee')
        errorMessage.textContent = `It's not working!`
        app.appendChild(errorMessage)
    }
}

request.send()
