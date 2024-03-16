$(function(){
    $.get('/data', function(data) {
        console.log(data)
        // data.forEach(element => {
        //     createAlbum(element.image, element.link_to_album);
        // });
    });
});

function createAlbum(img, link) {
    // Create new elements
    const newAlbum = $("<div class='albumContainer'></div>");
    const spotifyLink = $("<a href='" + link + "' target='_blank' rel='noopener noreferrer'></a>");
    const newImage = $("<img class='albumCoverItem'></img>").attr('src', img);
    
    // append the new elements to the album container
    spotifyLink.append(newImage);
    newAlbum.append(spotifyLink);

    $('.albumMosaicContainer').append(newAlbum);
};