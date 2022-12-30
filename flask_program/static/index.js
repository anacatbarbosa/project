const container = document.querySelector('#infinity');
// needed in my profile to show only user recipes and not all recipes
let url = String(window.location.href).split('/')
url = url[url.length - 1]
/* number of recipes displayed at first when accessing recipes page */
const firstRecipes = 9

/* number of recipes shown when hitting the end of page and enabling infinity scroll */
const scrollRecipes = 6

/* Check if it has a scroll bar visible*/
function hasScrollBar(element) {
    var el = document.getElementById(element);
    /*var style = window.getComputedStyle(el, null).getPropertyValue('font-size');*/
    var hs = el.scrollWidth > el.clientWidth;
    
    if (hs == true)
    {
        var el2 = document.getElementById("hrSize" + element);
        el2.classList.add("withScrollBar")
    }
}

/* Function to the delete the post if the user or the adm click on it*/
function deletePost(postId){
    fetch("/delete_post", {
        method: "POST",
        body:JSON.stringify({postId: postId}),
    }).then((_res)=>{
        window.location.href = String("/" + url);
    });
}

/* signaling the back end to receive a json file with all the post information to show on page */
async function fetchData(url){
    const adress = '/get_posts/' + url;
    let response = await fetch(adress, {method: 'POST'});
    let data = await response.json();
    data = JSON.stringify(data);
    data = JSON.parse(data);
    return data;
}

let scroll_counter = 0;

/* function to load numImages to show on #infinity div at recipes.html
   post_details contains path, titles and post_id*/
async function loadImages (already_uploaded, numImages = firstRecipes) {
    if (container == null) {
        return false;
    }
    const post_details = await fetchData(url)
    const total_posts = post_details['path'].length /* counts every post */
    let i = already_uploaded;
    numImages += already_uploaded

    /* loop breaks when total posts are reached */
    while (i < numImages && i < total_posts) {
        const buttonEl = document.createElement('a')
        buttonEl.classList.add('col-sm')
        href = "/recipes/"+post_details['titles'][i]+"/"+post_details['post_id'][i]
        buttonEl.href = href
        if (post_details['user_id'][i] == post_details['current_user'] || post_details['adm'] == 1)
        {
            buttonEl.innerHTML = `
                <button type="button" class="close" onClick="deletePost(${post_details['post_id'][i]})">
                    <span aria-hidden="true">&times</span>
                </button>
                <div id="hrSize${post_details['post_id'][i]}" class="hrSize">
                    <h4 id="${post_details['post_id'][i]}" class="h4Title">${post_details['titles'][i]}</h4>
                    <hr class="hrSet">
                </div>
                <div class="imgRatio">
                    <img src=${post_details['path'][i]}>
                </div>
            `
        }
        else{
            buttonEl.innerHTML = `
                <div id="hrSize${post_details['post_id'][i]}" class="hrSize">
                    <h4 id="${post_details['post_id'][i]}" class="h4Title">${post_details['titles'][i]}</h4>
                    <hr class="hrSet">
                </div>
                <div class="imgRatio">
                    <img src=${post_details['path'][i]}>
                </div>
            `
        }
        container.appendChild(buttonEl)
        hasScrollBar(post_details['post_id'][i])
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

