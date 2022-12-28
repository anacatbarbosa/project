const container = document.querySelector('#infinity');

/* number of recipes displayed at first when accessing recipes page */
const firstRecipes = 9

/* number of recipes shown when hitting the end of page and enabling infinity scroll */
const scrollRecipes = 6

/* Function to the delete the post if the user or the adm click on it*/
function deletePost(postId){
    fetch("/delete_post", {
        method: "POST",
        body:JSON.stringify({postId: postId}),
    }).then((_res)=>{
        window.location.href = "/recipes";
    });
}

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
async function loadImages (already_uploaded, numImages = firstRecipes) {
    const post_details = await fetchData()
    const total_posts = post_details['path'].length /* counts every post */
    let i = already_uploaded;
    numImages += already_uploaded

    /* loop breaks when total posts are reached */
    while (i < numImages && i < total_posts) {
        const buttonEl = document.createElement('button')
        buttonEl.classList.add('col-sm')
        formation_string = "/recipes/"+post_details['titles'][i]+"/"+post_details['post_id'][i]
        buttonEl.formAction = formation_string
        console.log(post_details)
        if (post_details['user_id'][i] == post_details['current_user'] || post_details['adm'] == 1)
        {
            buttonEl.innerHTML = `
                <button type="button" class="close" onClick="deletePost(${post_details['post_id'][i]})">
                    <span aria-hidden="true">&times</span>
                </button>
                <div class="hrSize">
                    <h4 class="h4Title">${post_details['titles'][i]}</h4>
                    <hr class="hrTitle">
                </div>
                <div class="imgRatio">
                    <img src=${post_details['path'][i]}>
                </div>
            `
        }
        else{
            buttonEl.innerHTML = `
                <div class="hrSize">
                    <h4 class="h4Title">${post_details['titles'][i]}</h4>
                    <hr class="hrTitle">
                </div>
                <div class="imgRatio">
                    <img src=${post_details['path'][i]}>
                </div>
            `
        }
        container.appendChild(buttonEl)
        i++;
    }
}
loadImages(0);

/* checking if user got to the end of the page to enable the infinity scroll */
window.addEventListener('scroll', () => {
    if(window.scrollY + window.innerHeight >= document.documentElement.scrollHeight){
        scroll_counter++
        if (scroll_counter == 1) {
            loadImages(firstRecipes, numImages = scrollRecipes)
        }
        else
        {
            loadImages(firstRecipes + scrollRecipes * (scroll_counter - 1), numImages = scrollRecipes)
        }
    }
})

