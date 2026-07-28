import * as fs from 'node:fs'

let data_sample = {
	//colls:{count: 7, abs: {'6':23000},off: {'3': 3500}, def: 3000, start: 0},
	//rows:{count: 7, abs: {'6':23000},off: {'3': 3500}, def: 3000, start:0},
	//plans:{count: 7, abs: {'6':23000},off: {'3': 3500}, def: 3000,start:0},
	colls:{count: 3, abs: {'1':3000},off: {'2': 3500}, def: 2500, start: 0},
	rows:{count: 3, abs: {'1':3000},off: {'2': 3500}, def: 2500, start:0},
	plans:{count: 3, abs: {'1':3000},off: {'2': 3500}, def: 2500,start:0},

	vertColl: {type:'fi',totalHeight:150,flangeWidth:100,webThick:20, flangeThick:10, rot:[0,90,0],handle:'cen'},
	vertColl_0_1_1: {type:'fi',totalHeight:150,flangeWidth:100,webThick:20, flangeThick:10, rot:[0,90,0]},
	longBeam: {type:'fi',totalHeight:150,flangeWidth:100,webThick:20, flangeThick:10,rot: [0,0,0],handle:'tos'},
	crossBeam: {type:'fi',totalHeight:150,flangeWidth:100,webThick:20, flangeThick:10,rot:[0,0,-90],handle:'tos'},

	floorDepth : 2000,
	margin : 5000,
}
fs.writeFileSync('sample_skell.json',JSON.stringify(data_sample))
