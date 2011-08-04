// oneup.js

function sounds_cb()
{
	var oneuped = ! $(this).is(".eswa");

	bckgrnd_get_oneup_use_sounds(
	function(oneup_use_sounds) {

	if ( ! oneup_use_sounds )
		return;	

	if ( oneuped )
		return;

	var theId = null;

	bckgrnd_get_oneup_use_classic(
	function(oneup_use_classic) {

	if ( oneup_use_classic )
		theId = "oneup_sound_dig";
	else
		theId = "oneup_sound_anlg";

	var snd = document.getElementById(theId);

	snd.play();
	snd.volume = .6;

	console.log("1-up!");

	}); // bckgrnd_get_oneup_use_classic

	}); // bckgrnd_get_oneup_use_sounds
}

function add_style(style_id, style_text) {

	$("#" + style_id).remove();

	$("head").append(
		"<style id='"+style_id+"'>"
			+ style_text +
		"</style>"
	);
}

function main()
{
	console.log("oneup starts...");

	$("body").append(g_oneup_sounds);
	$(".esw").live('click', sounds_cb);

	add_style("rgy_style", g_icon_15rgy)
}


main()

// vim: ts=4:sw=4:
