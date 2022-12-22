const container = document.querySelector('#infinity');
/* signaling the back end to receive a json file with all the post information to show on page */
async function fetchData(){
    let response = await fetch('/get_posts', {method: 'POST'});
    let data = await response.json();
    data = JSON.stringify(data);
    data = JSON.parse(data);
    return data;
}

let scroll_counter = 0;

/* function to load numImages to show on #infinity div at recipes.html 
   post_details contains path, titles and post_id*/
async function loadImages (already_uploaded, numImages = 2) {
    const post_details = await fetchData()
    const total_posts = post_details['path'].length /* counts every post */
    let i = already_uploaded;
    numImages += already_uploaded
    /* loop breaks when total posts are reached */
    while (i < numImages && i < total_posts) {
        const img = document.createElement('img')
        img.src = post_details["path"][i]
        container.appendChild(img);
        i++;
    }
}
loadImages(0);

/* checking if user got to the end of the page to enable the infinity scroll */
window.addEventListener('scroll', () => {
    if(window.scrollY + window.innerHeight >= document.documentElement.scrollHeight){
        scroll_counter++
        loadImages(scroll_counter * 2);
    }
})

