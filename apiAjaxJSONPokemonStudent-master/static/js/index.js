$('#flexbox_display').click(function(){
  console.log("Flexbox display clicked");
  removeButtons();

  displayInfo("flexbox");
});

$('#bootstrap_display').click(function(){
  console.log("Bootstrap display clicked");
  removeButtons();
  $('main').append(`<div class="card-columns">`);
  displayInfo("bootstrap");
});

function removeButtons(){
  console.log("Removing buttons");
  $('button').remove();
}

function displayInfo(cardType){

  console.log("DisplayInfo: " + cardType);

  pokemon.forEach(poke =>{
    var movesList = "";
    for( var i=0; i<`${poke.moves.length}`; i++ )
      movesList+=("<li>" + `${poke.moves[i]}` + "</li>");

    var infoTable = 
    `<table>
        <tr>
            <td>ID:</td>
            <td>${poke.id}</td>
        </tr>
        <tr>
            <td>Height:</td>
            <td>${poke.height}</td>
        </tr>
        <tr>
            <td>Weight:</td>
            <td>${poke.weight}</td>
        </tr>
        <tr>
            <td>Moves:</td>
            <td>
                <ul>`
                  + movesList + 
                `</ul>
            </td>
        </tr>
    </table>
      `;

    if(cardType=="flexbox"){
      $('main').append(
        `<div class="column">
                    <img src="${poke.image}">
                    <h4>${poke.name}</h4>
                    <br>
                    <table>`
                    + infoTable +
                `</div>`
      );
    }
    else if(cardType=="bootstrap"){
      console.log("Else if triggered");

      $('.card-columns').append(
        `<div class="card">
          <img class="card-img-top" src="${poke.image}">
          <div class="card-body">
            <h4 class="card-title">${poke.name}</h4>
            <p class="card-text">`
                + infoTable + 
            `</p>
          </div>
        </div>`
      );
    }
  });
}