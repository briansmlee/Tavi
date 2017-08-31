/* client.js
 *
 */

/* global TrelloPowerUp */

var Promise = TrelloPowerUp.Promise;
var script_path = "./modal.py";
var BLACK_ROCKET_ICON = 'https://cdn.glitch.com/1b42d7fe-bda8-4af8-a6c8-eff0cea9e08a%2Frocket-ship.png?1494946700421';

// response for each capability in manifest are initialized here.
TrelloPowerUp.initialize({
    // cap for button on back of card
    'card-buttons': function(t, options) {
        return [{
            // icon and text are immediately displayed.
            icon: 'https://cdn.glitch.com/1b42d7' + 
            'fe-bda8-4af8-a6c8-eff0cea9e08a%2Frocket-ship.png?1494946700421',
            text: 'make Confluence page',

            // callback used when click
            callback: function(t) {
                return t.modal({
                    title: "Configuration",
                    // should call function here to get card or list id
                    url: run_script(script_path, t) //try './config.html' for testing 
                })
            }
        }];
    },
});


/* older func
function run_script(path, t) {
    // make jquery ajax request to run python script.
    $.ajax({
        type: "POST",
        url: path, // script file path
        data: t.getContext() // context of current card
    }).done(function() { // when ajax is done, do f'ns
        console.log("done!!!")// do something
    });
}
*/


/*
 * runs script in path and returns result
 */
function run_script(path, t) {
    var context = t.getContext();
    // console.log(JSON.stringify(context, null, 2));
    var board_id = context['board'];
    // make jquery ajax request to run python script.
    $.ajax({
        type: "POST",
        url: path, // script file path
        data: board_id, // context of current card
        success: function(data) {
            return data;
        },
        error: function() {
            alert('Error occured');
        }
    });
}
