--EarthBound (Archipelago) Sprite Injector--
(Written by Qwnint and Pink Switch)


INSTRUCTIONS:
	- To use this program, run the python script "EarthBoundSpriteInjector.py"

	-	Included with this program is a file named "sprites.json"
		To add custom sprites for use with the injector, open this file and add:
		{"YourSprite": YourPalette}
		to the list of sprites. You can set which characters have access to which sprites by adding them to their list accordingly.
		NOTE: Unless you are injecting a custom sprite which specifically uses a non-default palette, use 5 as the Palette.

	
	-	To add a sprite for use with the injector, you must create a folder in the same directory as this program.
		The name of this folder must be the same as the sprite entry added to the character's table as listed above.
		Inside of this folder must be invididual sprites in PNG format that are to be injected. The names for each file,
		and what it corresponds to in-game, is listed in the FILE GUIDE below. If a sprite is not present,
		it will simply be ignored and the sprite in-game will not be modified. Note that if the sprite was already presently modified,
		it will remain as the previous sprite, not restored to the original sprite.
		NOTE: The PNG MUST use only colors present in the chosen palette. Palettes.png contains all valid palettes.
		NOTE: The PNG MUST be formatted as RGB Color, not Color Indexed.
		NOTE: Palette 4 appears as garbage but uses colors sourced from the current map in game. Usage is not recommended.
		
	-	When running this program, you will be prompted to input the name of your EarthBound ROM file.
		For Archipelago purposes, this must be done after the patch is applied. YOU CANNOT PATCH USING A BASE ROM WITH INJECTED SPRITES.
		When a ROM is selected, you will be prompted to select which character, Ness, Paula, Jeff, or Poo you would like to inject a sprite over.
		When a character is selected, you will be prompted to input which sprite you would like to use. This accepts the names of folders containing sprites
		as loaded in the first step above. You can additionally use -r to select a random valid sprite.


---- FILE GUIDE ----
 - Main:
	---------
	These are the standard sprites for the selected character.
		- MainDown
		- MainDown
		- MainDownWalkFrame
		- MainUp
		- MainSide
		- MainSideWalk
		MainUpSide
		MainUpSideWalk
		MainDownSide
		MainDownSideWalk
	--------
	This is only used by Ness as a downwards walking sprite. Other characters use a mirror of MainDown.
		MainDownWalkFrame
	--------
	These are the unique robot sprites used by Ness in the Cave of the Past.
	Other characters use a generic sprite which cannot be modified individually.
		MainDownBot
        MainDownWalkFrameBot
        MainUpBot
        MainSideBot
        MainSideWalkBot
        MainUpSideBot
        MainUpSideWalkBot
        MainDownSideBot
        MainDownSideWalkBot
	--------
	These are the ghost sprites used when the character is dead.
		GhostDown
        GhostUp
        GhostSide
	--------
	This is used and mirrored wile climbing ladders.
		ClimbLadder
	-------
	These are used alternatingly while climbing ropes.
		ClimbRope
        ClimbRopeFrame
	-------
	These are used for when Ness rides the Bicycle, bike included.
        BikeUp
        BikeSide
        BikeSidePedal
        BikeDown
        BikeUpSide
        BikeUpSidePedal
        BikeDownSide
        BikeDownSidePedal
	-------
	These are used in the Lost Underworld.
		TinyDown
		TinySide
		TinySideWalk
	-------
	These are used by Ness while wearing pajamas. Note that in the AP randomizer, these are only used while Ness is present in Magicant.
        PajamaUp
        PajamaSide
        PajamaSideWalk
        PajamaDown
        PajamaWalkFrame
        PajamaUpSide
        PajamaUpSideWalk
        PajamaDownSide
        PajamaDownSideWalk
	-------
	This is used whenever Ness is present during a Photograph.
        PhotoPose
	-------
	This is used for the broken Ness robot after defeating Giygas. The other characters use generic sprites which cannot be modified individually.
        BrokenBot
	-------
	This is used for characters lying down. In the AP randomizer, this sprite is used if a main character is on the Snow Wood - Bedroom character location
        LieDown
	-------
	This is used on the naming screen and/or some cutscenes.
        Surprised
	-------
	This is used when Poo meditates for the Trial of Mu, as well as on the naming screen.
		Meditate