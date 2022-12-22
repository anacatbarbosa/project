const container = document.querySelector('.container');

let post_details = 0;

fetch('/get_posts', {
    method: 'POST'
})
    .then(res => res.json())
    .then(data => console.log(data))

function loadImages (numImages = 9) {
    let i = 0;
    while (i < numImages) {
        const img = document.createElement('img')
        i++;
    }
}

window.addEventListener('scroll', () => {
    if(window.scrollY + window.innerHeight >= document.documentElement.scrollHeight){
        post_details++;
        console.log(post_details)
    }
})

