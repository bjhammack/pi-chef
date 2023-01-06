window.onload = function() {
    get_all_recipes()
}

function get_recipe(id) {
    $.ajax({
        type: 'GET',
        url: '/recipe',
        data: {recipe_id: id},
        success: function(recipe) {
            document.getElementById("recipes").style.display = 'none'
            document.getElementById("new-recipe").style.display = 'none'
            document.getElementById("recipe").style.display = 'block'

            $('#recipe-header').text(recipe[0].name)
            $('#ingredients').text(recipe[0].ingredients)
            $('#steps').text(recipe[0].directions)
        }
    })
}

function close_recipe() {
    document.getElementById("recipes").style.display = 'block'
    document.getElementById("new-recipe").style.display = 'none'
    document.getElementById("recipe").style.display = 'none'
}

function get_all_recipes() {
    $.ajax({
        type: 'GET',
        url: '/all_recipes',
        success: function(recipes) {
            document.getElementById("recipes").style.display = 'block'
            document.getElementById("new-recipe").style.display = 'none'
            document.getElementById("recipe").style.display = 'none'

            let recipeCount = recipes.length
            let currentPage = 1
            let pages = {[currentPage]: ''}
            for (var i = 0; i < recipeCount; i++) {
                let html = generate_card_html(recipes[i])
                pages[currentPage] += html
                if ((i+1) % 10 == 0) {
                    currentPage += 1
                    pages[currentPage] = ''
                }
            }
            localStorage.pages = JSON.stringify(pages);
            paginate('dummy-div-1')
            update_recipes_page(1)
        }
    })
}

function update_recipes_page(page) {
    var pages = JSON.parse(localStorage.pages);
    let currentPage = pages[page]
    document.getElementById('recipe-card-holder').innerHTML = currentPage
    
    return Object.keys(pages)
}

function generate_card_html(recipe) {
    let html = ''
    html += '<div class="col">'
    html += '<div id="' + recipe.id + '" class="card recipe-card h-100" onclick="get_recipe(this.id)">'
    html += '<img src="' + recipe.image + '" class="card-img-top recipe-card-img" alt="No Image">'
    html += '<div class="card-body">'
    html += '<h5 class="card-title">' + recipe.name + '</h5>'
    html += '<p class="card-text">' + recipe.description + '</p>'
    html += '</div></div></div>'

    return(html)
}

function paginate(pageId) {
    var page = document.getElementById(pageId).innerHTML
    if (page < 1) {
        page = 1
    }
    var pages = update_recipes_page(page)
    pages.sort(compareNumbers)
    if (page > pages.length) {
        page = pages.length
    }

    var html = generate_paginate_html(page, pages)
    document.getElementById('pagination').innerHTML = html

    var pagiId = ''
    var notPagi1 = ''
    var notPagi2 = ''
    if (page % 3 == 0) {
        pagiId = 'pagi-3'
        notPagi1 = 'pagi-1'
        notPagi2 = 'pagi-2'
    } else if ((page+1) % 3 == 0) {
        pagiId = 'pagi-2'
        notPagi1 = 'pagi-1'
        notPagi2 = 'pagi-3'
    } else {
        pagiId = 'pagi-1'
        notPagi1 = 'pagi-3'
        notPagi2 = 'pagi-2'
    }
    document.getElementById(pagiId).classList.add('active');

    try {
        document.getElementById(notPagi1).classList.remove('active');
    }
    catch(err) {

    }
    try {
        document.getElementById(notPagi2).classList.remove('active');
    }
    catch(err) {

    }

    if (page == 1) {
        document.getElementById('pagi-prev').classList.add('disabled')
    } else {
        document.getElementById('pagi-prev').classList.remove('disabled')
    }
    if (page == pages.length) {
        document.getElementById('pagi-next').classList.add('disabled')
    } else {
        document.getElementById('pagi-next').classList.remove('disabled')
    }
}

function generate_paginate_html(currentPage, pages) {
    currentPage = Number(currentPage)
    var html = ''
    var maxPage = pages.length

    var pageButtons = 0
    if (maxPage >= 3) {
        pageButtons = 3
    } else if (maxPage == 2) {
        pageButtons = 2
    } else {
        pageButtons = 1
    }

    // writing html
    html += '<li class="page-item">'
    html += '<a id="pagi-prev" value="' + (currentPage - 1) + '" class="page-link" onclick="paginate(this.id)" aria-label="Previous">'
    html += '<span aria-hidden="true">&laquo;</span>'
    html += '</a></li>'
    if (currentPage % 3 == 0){
        for (var i = -2; i < pageButtons-2; i++) {
            html += '<li class="page-item">'
            html += '<a id="pagi-'+(i+3)+'" class="page-link" onclick="paginate(this.id)">'+ (currentPage+i) +'</a></li>'
        }
    } else if ((currentPage+1) % 3 == 0) {
        for (var i = -1; i < pageButtons-1; i++) {
            html += '<li class="page-item">'
            html += '<a id="pagi-'+(i+2)+'" class="page-link" onclick="paginate(this.id)">'+ (currentPage+i) +'</a></li>'
        }
    } else {
        for (var i = 0; i < pageButtons; i++) {
            html += '<li class="page-item">'
            html += '<a id="pagi-'+(i+1)+'" class="page-link" onclick="paginate(this.id)">'+ (currentPage+i) +'</a></li>'
        }
    }
    html += '<li class="page-item">'
    html += '<a id="pagi-next" value="' + (currentPage + 1) + '" class="page-link" onclick="paginate(this.id)" aria-label="Next">'
    html += '<span aria-hidden="true">&raquo;</span>'
    html += '</a></li>'
    
    return(html)
}

function compareNumbers(a, b) {
    return a - b;
  }