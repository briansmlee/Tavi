var t = TrelloPowerup.iframe()

window.esimate.addEventListener('submit', function(event){
    // stop browser from trying to submit the form itself.
    event.preventDefault();
    
    // run python script with 
    run_script('/main.py', window.list_id.value, window.space_id.value)
    .then(function(){
        t.closeModal();
    });
    
    // instead of saving data to plugindata field for card,
    // we directly call python script 2. using ajax
    //return t.set('card', 'shared', 'estimate', window.estimateSize.value)
    //.then(function(){
    //    t.closeModal();
    // });
});

/*
 * runs script in path 
 */
function run_script(path, list_id, space_id) {
    // make jquery ajax request to run python script.
    $.ajax({
        type: "POST",
        url: path, // script file path
        data: { 
            "list_id" : list_id,
            "space_id" : space_id }, // context of current card
        // success: function(data) { },
        error: function() {
            alert('Error occured');
        }
    });
}

t.render(function() {
    t.sizeTo('#modal').done();
});
