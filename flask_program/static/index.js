const container = document.querySelector('.container');

let post_details = 0;

function loadImages (numImages = 9) {
    

}

fetch('/get_posts', {
    method: 'POST'
})
    .then(res => res.json())
    .then(data => console.log(data))