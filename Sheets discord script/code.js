// Code for google apps script, paste into the script editor and execute the trigger function
// Personal project

var app = SpreadsheetApp;

var shAvail = app.getActive().getSheetByName('sheet_name');

function collect_data() {
  var message = ""
  var weekday = ((new Date(Date.now())).getDay() + 6) % 7; //0 - monday etc.
  var todayColour = shAvail.getRange(3, 4 + weekday).getBackground();
  var todayStrike = shAvail.getRange(4, 4 + weekday).getFontLine();
  var scrimTime = shAvail.getRange(4, 4 + weekday).getValue();
  var enemy = shAvail.getRange(5, 4 + weekday).getValue();
  var pregameBlank = shAvail.getRange(3, 4 + weekday);
  var pregameTime = shAvail.getRange(3, 4 + weekday).getValue();
  var names = getPlayers().toString();
  var offi = shAvail.getRange(7, 4 + weekday).getValue();
  var offiBlank = shAvail.getRange(7, 4 + weekday);
  if (todayColour == "#ffffff") {
    //pass
  } else {
    if (todayStrike != "line-through") {
      var pregameString = pregameTime.toString();
      if (pregameBlank.isBlank() || pregameString.indexOf("<") >= 0) {
        message += "@everyone\nWe have a game today at " + scrimTime + " against " + enemy + "\n" + names
        send_message(message);
      }
      else if (offiBlank.isBlank()) {
        message += "@everyone\nWe have a pregame/maptalk at " + pregameTime + "\n" + "Game against " + enemy + " at " + scrimTime + "\n" + names
        send_message(message);
      }
      else {
        message += "@everyone\nWe have a pregame/maptalk at " + pregameTime + "\n" + offi + " against " + enemy + " at " + scrimTime + "\n" + names
        send_message(message);}
      }
    else {
      message += "@everyone\nScrim has been cancelled";
      send_message(message);}
  }
}

function getPlayers() {
  var weekday = ((new Date(Date.now())).getDay() + 6) % 7;
  var playerNames = shAvail.getRange(10, 3, 9).getValues();
  var names = ["Gamers:"];
  for (var [index, name] of playerNames.entries()) {
    var playerColor = shAvail.getRange(10+ index, 4 + weekday).getBackground();
    if (playerColor == "#b6d7a8") {
      names.push(":green_square: "+name);
    }
    else if (playerColor == "#ffe599") {
      names.push(":yellow_square: "+name);
    }
    else if (playerColor == "#e06666") {
      names.push(":red_square: "+name);
    }
    else {names.push(":clown: "+name) }
  }
  var list = names.join("\n");
  return list
}

function send_message(message) {
  
  message = message

  var discordUrl = "https://discord.com/api/webhooks/981681562837983282/rmwhhxW06M8WifpHjUk_Z6U6h3nzSEAbAWEkH0EeLAOVRj36slPpxjIteo_dqNwe_ABD";

  var payload = JSON.stringify({
    "avatar_url": "https://avatars.cloudflare.steamstatic.com/dbabbd8bab7ccf6d27a9d4ca2e73a76e085bb201_full.jpg",
    "content": message,
  });

  var params = {
  method: "POST",
  payload: payload,
  muteHttpExceptions: true,
  contentType: "application/json"
  };

  var response = UrlFetchApp.fetch(discordUrl, params);

  Logger.log(response.getContentText());

}