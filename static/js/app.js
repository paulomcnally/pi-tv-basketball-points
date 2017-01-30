$.fn.extend({
    animateCss: function (animationName) {
        var animationEnd = 'webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend';
        this.addClass('animated ' + animationName).one(animationEnd, function() {
            $(this).removeClass('animated ' + animationName);
        });
    }
});

var ws = new WebSocket("ws://127.0.0.1:8000/websocket");
ws.onmessage = function (event) {
  // item.team_id
  // item.team_name
  // item.team_points
  // item.access_token
  var item = JSON.parse(event.data);

  //$('.col').height($(window).height());

  var teamATitle = $('#team_a_title');
  var teamBTitle = $('#team_b_title');
  var teamAPoints = $('#team_a_points');
  var teamBPoints = $('#team_b_points');

  if (item.team_id == 0) {
    teamATitle.text(item.team_name);
    teamAPoints.text(item.team_points).animateCss('bounce');
  } else if (item.team_id == 1) {
    teamBTitle.text(item.team_name);
    teamBPoints.text(item.team_points).animateCss('bounce');
  }
};
