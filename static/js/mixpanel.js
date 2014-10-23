/**
 * Created by Adam on 10/23/14.
 */
$(document).ready(function() {
    $("#featuredBlog").click(function () {
        mixpanel.track("Blog Footer Clicked");
    });

    $(".sideTag").click(function () {
        mixpanel.track("Blog Footer Clicked");
    });
});