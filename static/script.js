const app = document.getElementById('root')

const logo = document.createElement('img')
logo.src = 'logo.png'

const container = document.createElement('div')
container.setAttribute('class', 'container')

app.appendChild(logo)
app.appendChild(container)

var request = new XMLHttpRequest()
request.open('GET', 'https://a-recoba.herokuapp.com/fixtures', true)
// request.open('GET', 'http://127.0.0.1:8000/fixtures', true)
request.onload = function() {
    // Begin accessing JSON data here
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
        errorMessage.textContent = `Gah, it's not working!`
        app.appendChild(errorMessage)
    }
}

request.send()