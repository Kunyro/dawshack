$(function(){
    
});

function createAlbum() {
    const newAlbum = $("<div class='albumContainer'></div>");
    const newImage = $("<div class='albumCoverItem'></div>");
    $('.albumMosaicContainer').append(newAlbum).append(newImage);
}