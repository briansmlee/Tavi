* global TrelloPowerUp */

var Promise = TrelloPowerUp.Promise;

var BLACK_ROCKET_ICON = 'https://cdn.glitch.com/1b42d7fe-bda8-4af8-a6c8-eff0cea9e08a%2Frocket-ship.png?1494946700421';

// TrelloPowerUp.initialize({
  // Start adding handlers for your capabilities here!
	// 'card-buttons': function(t, options) {
	// 	return [{
	// 		icon: BLACK_ROCKET_ICON,
	// 		text: 'Estimate Size',
	// callback: function(t) {
	// return t.popup({
	// title: "Estimation",
	// url: 'estimate.html',
	// });
	// }
	// 	}];
	// },
// });

// response for each capability in manifest are here.
// 
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
                    url: 'config.html' 
                })
            }
        }];
    },
});

// make jquery ajax request to run python script.
$.ajax({
    type: "POST",
    url: "~/pythoncode.py", // path
    // need card_id data to get all lists in coor board?
    data: t.getContext() // context of current card
}).done(function( o ) { // when ajax is done, do f'ns
    console.log("done!!!")// do something
});
    
