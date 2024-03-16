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
    
    // append the new elements to the album container
    newAlbum.append(newImage);

    $('.albumMosaicContainer').append(newAlbum);
};