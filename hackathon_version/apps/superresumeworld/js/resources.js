game.resources = [
	/**
	 * Graphics.
	 */
	// the main player spritesheet
	//{name: "gripe_run_right",     type:"image",	src: "data/img/sprite/gripe_run_right.png"},
	{name: "gripe_run_right",     type:"image",	src: "data/img/sprite/tux_run_right.png"},
	// the spinning coin spritesheet
	{name: "spinning_coin_gold",  type:"image",	src: "data/img/sprite/spinning_coin_gold.png"},
	// our enemty entity
	{name: "wheelie_right",       type:"image",	src: "data/img/sprite/wheelie_right.png"},
	// game font
	{name: "32x32_font",          type:"image",	src: "data/img/font/32x32_font.png"},
	// title screen
	{name: "title_screen",        type:"image",	src: "data/img/gui/title_screen.png"},
	// the parallax background
	{name: "area01_bkg0",         type:"image",	src: "data/img/area01_bkg0.png"},
	{name: "area01_bkg1",         type:"image",	src: "data/img/area01_bkg1.png"},
	// our level tileset
	{name: "area01_level_tiles",  type:"image",	src: "data/img/map/area01_level_tiles.png"},
	//load our new tiles
	{name: "Tiles_32x32",  type:"image",	src: "data/img/map/Tiles_32x32.png"},
	
	/* 
	 * Maps. 
 	 */
	{name: "area01",              type: "tmx",	src: "data/map/area01.tmx"},
	{name: "area02",              type: "tmx",	src: "data/map/area02.tmx"},
	{name: "area03",              type: "tmx",	src: "data/map/area03.tmx"},

	/* 
	 * Background music. 
	 */	
	//{name: "dst-inertexponent", type: "audio", src: "data/bgm/", channel : 1},
	
	{name: "resumeworld", type: "audio", src: "data/bgm/", channel : 1},
	
	/* 
	 * Sound effects. 
	 */
	{name: "cling", type: "audio", src: "data/sfx/", channel : 1},
	{name: "stomp", type: "audio", src: "data/sfx/", channel : 1},
	{name: "jump",  type: "audio", src: "data/sfx/", channel : 1}
];
