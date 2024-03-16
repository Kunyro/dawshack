$(function(){
    $.get('/data', { timeout: 30000 }, function(data) {
        // data.forEach((album) => {
        //     const img = album.image;
        //     const link = album.link_to_album;
        //     createAlbum(img, link);
        // });
        console.log(data);
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