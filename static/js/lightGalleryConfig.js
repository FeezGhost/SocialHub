import lightGallery from "https://cdn.skypack.dev/lightgallery@2.1.2";

import lgZoom from "https://cdn.skypack.dev/lightgallery@2.1.2/plugins/zoom";

import lgThumbnail from "https://cdn.skypack.dev/lightgallery@2.1.2/plugins/thumbnail";

import lgShare from "https://cdn.skypack.dev/lightgallery@2.1.2/plugins/share";

import lgRotate from "https://cdn.skypack.dev/lightgallery@2.1.2/plugins/rotate";

import lgAutoplay from "https://cdn.skypack.dev/lightgallery@2.1.2/plugins/autoplay";
import lgFullscreen from "https://cdn.skypack.dev/lightgallery@2.1.2/plugins/fullscreen";

$("#animated-thumbnails-gallery")
  .justifiedGallery({
    captions: false,
    lastRow: "hide",
    rowHeight: 180,
    margins: 5
  })
  .on("jg.complete", function () {
    lightGallery(document.getElementById("animated-thumbnails-gallery"), {
      autoplayFirstVideo: false,
      pager: false,
      galleryId: "nature",
      flipHorizontal: false,
      flipVertical: false,
      rotateLeft: false,
      plugins: [
        lgZoom,
        lgThumbnail,
        lgShare,
        lgRotate,
        lgFullscreen,
        lgAutoplay
      ],
      mobileSettings: {
        controls: false,
        showCloseIcon: false,
        download: false,
        rotate: false
      }
    });
  });