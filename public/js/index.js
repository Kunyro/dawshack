$(function(){
    $.get('/data', function(data) {
        const img = data.img;
        const title = data.title;
        const artist = data.artist;
        createAlbum(img, title, artist);
    })
});

function createAlbum(img, title, artist) {
    // Create new elements
    const newAlbum = $("<div class='albumContainer'></div>");
    const newImage = $("<img class='albumCoverItem'></img>").attr('src', img);
    const albumTitleItem = $("<h1 class='albumTitleItem'></h1>").text(title);
    const albumArtistItem = $("<h2 class='albumArtistItem'></h2>").text(artist);
    
    // append the new elements to the album container
    newAlbum.append(newImage, albumTitleItem, albumArtistItem);

    $('.albumMosaicContainer').append(newAlbum);
};