//Baratheon: 16
//Lannister: 229
//Stark: 362
//Targaryen: 378
var id=0;
$('img').click(function(){
    switch(this.id){
        case "stark":       id=362; break;
        case "targaryen":   id=378; break;
        case "lannister":   id=229; break;
        case "baratheon":   id=16; break;
    }
    console.log(id);

    $.get(`https://anapioficeandfire.com/api/houses/${id}`, function(result){
        $('#house_details').html(
            `<p>Name: ${result.name}</p>
            <p>Words: ${result.words}</p>
            <p>Region: ${result.region}</p>
            <p>Coat of Arms: ${result.coatOfArms}</p>
            
            `
        );
    },
    "json"); 
});

/* var found=false;
var count=1;

$.get(`https://anapioficeandfire.com/api/houses?name="house%20algood"`, function(result){
    console.log(result);
},
"json");

var houseString = "";
for(var i=1;i<=400;i++){
    // console.log("First");
    // console.log(i);
    $.get(`https://anapioficeandfire.com/api/houses/${i}`, function(result){
        if(result.name.startsWith("House Stark"))
            console.log("The id is: + )
    },
    "json");
    // console.log("Third");
}
console.log(houseString);
 */

//Baratheon: 16
//Lannister: 229
//Stark: 362
//Targaryen: 378