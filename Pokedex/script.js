console.log("Linked");

for( var i=1; i<=151; i++ ){
    $("#grid").append(`<img id="${i}" src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${i}.png">`);
}

$("#grid img").click(function(){
    $.get( `https://pokeapi.co/api/v2/pokemon/${this.id}`, function(clickedPokemon){
        console.log("Clicked on: " + clickedPokemon.name);
        console.log(clickedPokemon);

        //COMPILE MOVES LIST
        var abilityList = "";
        for( var a=0; a<clickedPokemon.abilities.length; a++){
            abilityList+=`<li>${clickedPokemon.abilities[a].ability.name}</li>`
        }

        $('#focus').html(
            `<img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${clickedPokemon.id}.png">
            <h4>${clickedPokemon.name}</h4>
            <table>
                <tr>
                    <td>ID:</td>
                    <td>${clickedPokemon.id}</td>
                </tr>
                <tr>
                    <td>Height:</td>
                    <td>${clickedPokemon.height}</td>
                </tr>
                <tr>
                    <td>Weight:</td>
                    <td>${clickedPokemon.weight}</td>
                </tr>
                <tr>
                    <td>Abilities:</td>
                    <td><ul>${abilityList}</ul></td>
                </tr>
            </table>
            `
        )
    },
    "json");
});



//pokeapi.co/api/v2/pokemon/1