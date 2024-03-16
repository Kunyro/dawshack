$(function(){
    // $.get('/data', function(data) {
    //     const img = data.img;
    //     const title = data.title;
    //     const artist = data.artist;
    //     createAlbum(img, title, artist);
    // })
    createAlbum("https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Jamie_Kalven_%28cropped%29.jpg/210px-Jamie_Kalven_%28cropped%29.jpg", "https://open.spotify.com/album/71O60S5gIJSIAhdnrDIh3N");
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