$(function(){
    $.get('/data', function(data) {
        const img = data.img;
        const title = data.title;
        const artist = data.artist;
        createAlbum(img, title, artist);
    });
});

export function createAlbum(img, title, artist) {
    const newAlbum = $("<div class='albumContainer'></div>");
    const newImage = $("<img class='albumCoverItem'></img>");
    newImage.attr('src', img);
    const albumTitleItem = $("<h1 class='albumTitleItem'></h1>");
    albumTitleItem.text(title);
    const albumArtistItem = $("<h2 class='albumArtistItem'></h2>");
    albumArtistItem.text(artist);
    
    // append the new elements to the album container
    newAlbum.append(newImage);
    newAlbum.append(albumTitleItem);
    newAlbum.append(albumArtistItem);

    $('.albumMosaicContainer').append(newAlbum);
}