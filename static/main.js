console.log('Hello World')

console.log(document)

const test = document.getElementById('test')
const posts2 = document.getElementById('posts2')
const spinner = document.getElementById('spinner-box')
console.log(test)

setTimeout(()=>{
    test.textContent = "How are you doing?"
}, 2000)

$.ajax({
    type: 'GET',
    url: '/posts-json/',
    success: function(response){
        console.log(response.data)
        const data = JSON.parse(response.data)
        console.log(data)
        setTimeout(()=>{
            data.forEach(el=>{
                posts2.innerHTML += `${el.fields.body} <br>`
            })
            spinner.classList.add('not-visible')
        }, 2000)
        
    },
    error: function(error){
        console.log(error)
    }
})
