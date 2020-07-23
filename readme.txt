I. Installation:
- install packages from requirements(use virtualenv)
- instal scrot (yum install scrot)
- install tesseract (yum install tesseract)

II. Before runing any script
Before run any script activate virtualenv

III Scripts
 a) Miner
  - option w - wall
	 before start activate pickaxed, then start script and hoover a cave wall
	 if cursour is not over a cave wall then the script will suspend

  - option v - vein
  	@TODO

 b) Mixer - Script to mix automatically herbs
 	Before start move all alchemy products into a backpack then open the backpack,
	shuffle products by clicking on "QL" table header and run script

 c) Stone cutter - Script to automatically turn stone shards to stone bricks
 	Before start script place all your stone shards into a bsb named [source] and open it
	You should also have one bsb named [target] and the window of it should be also opened
	Lastly, open a crafting window, place stone chisel into right ingedient place
	and fire the script!

 d) Smither
 	@TODO

III. Modules
 a) lib/craft - module to manage all actions related to crafting window
 b) lib/window - module to manage all actions with containers windows
 c) lib/events - module which allows to lookup game events @TODO
