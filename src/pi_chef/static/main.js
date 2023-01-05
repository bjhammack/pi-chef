function get_recipe(id) {
    $.ajax({
        type: 'GET',
        url: '/recipe',
        data: {recipe_id: id},
        success: function(response) {
            document.getElementById("recipes").style.display = 'none'
            document.getElementById("new-recipe").style.display = 'none'
            document.getElementById("recipe").style.display = 'block'

            $('#recipe-header').text(response[0].name)
            $('#ingredients').text(response[0].ingredients)
            $('#steps').text(response[0].steps)
        }
    })
}

function close_recipe() {
    document.getElementById("recipes").style.display = 'block'
    document.getElementById("new-recipe").style.display = 'none'
    document.getElementById("recipe").style.display = 'none'
}