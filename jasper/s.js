//sectioning
//grouping
//boundering
console.log()
let debug


//mater
let vertColColor = '"plastic {tr 0.3 re 0.0}" 0 0 255 0'
let longBeamColor = '"plastic {tr 0.3 re 0.0}" 100 0 255 0 '
let crossBeamColor = '"plastic {tr 0.3 re 0.0}" 0 100 255 0'
let baseColor = '"plastic {tr 0.0 re 0.0}" 0 0 100 0'
let boundaryBoxColor = '"plastic {tr 0.3 re 0.0}" 0 0 100 0'



//take civil diminsion(long , traverse, or plans) specifications object
//and return array of axesses interpolated 
//{count: 7, abs: {'6':23000},off: {'3': 3500}, def: 3000, start: 0},
//absolute offsets default-offset

function interpolate(interObj) {
	//interpolated array to be returned
	let inter = Array(interObj.count)	

	//looping over count
	for(let i = 0; i < interObj.count; i++) {
		
		//use start if it is defined at first
		if (i == 0 && interObj.start != undefined ) { 
			inter[i] = interObj.start; continue
		}
		
		//lets determine the i-th axess coordinate value
		//if absolute is given it pioritized over others
		//if not we look for dedicated offset
		//if not we look for the dfault offset
		//and add the offset determind to previous axcess value
		//or to zero if it is first
		inter[i]= interObj.abs[i] || (interObj.off[i]||interObj.def) + (i>0 ? inter[i-1] : 0)
	}	
	return inter
}



function inSph(data){
	console.log(`in ${data.name} sph ${data.vertex.join(' ')} ${data.radius}`)
}

function inRCC(data){
	if(data.vertex2 != undefined && data.vector == undefined){
		data.vector = [data.vertex.length]
		for (let i=0; i < data.vertex.length ; i++){ data.vector[i] = data.vertex2[i] - data.vertex[i] }
	}
	console.log(`in ${data.name} rcc ${data.vertex.join(' ')} ${data.vector.join(' ')} ${data.radius}`)
}

function inRPP(data){
	console.log(`in ${data.name} rpp ${data.xmin} ${data.xmax}  ${data.ymin} ${data.ymax}  ${data.zmin} ${data.zmax}` )

}


function inBeam(data){
	let lowerFlangeData={
		name: data.name+ 'LowerFlange.s', 
		xmin: 0,
		xmax: data.length,
		ymin: -data.flangeWidth/2,
		ymax: data.flangeWidth/2,
		zmin: 0,
		zmax: data.flangeThick
	}

	let webData={
		name: data.name+ 'Web.s',
		xmin: 0,
		xmax: data.length,
		ymin: -data.webThick/2,
		ymax: data.webThick/2,
		zmin: data.flangeThick,
		zmax: data.totalHeight-data.flangeThick
	}
	
	let upperFlangeData={
		name: data.name+ 'UpperFlange.s',
		xmax: data.length,
		xmin: 0,
		ymin: -data.flangeWidth/2,
		ymax: data.flangeWidth/2,
		zmin: data.totalHeight-data.flangeThick,
		zmax: data.totalHeight
	}
	let cenHandleData = {
		name: data.name+ 'Cen.s',
		vertex: [0,0,data.totalHeight/2],
		radius: data.webThick,
	}
	let tosHandleData = {
		name: data.name+ 'Tos.s',
		vertex: [0,0,data.totalHeight],
		radius: data.webThick,
	}


	inRPP(lowerFlangeData)
	inRPP(webData)
	inRPP(upperFlangeData)
	inSph(cenHandleData)
	inSph(tosHandleData)
	//let members = [lowerFlangeData,webData,upperFlangeData].map((e)=>e.name+'.s').join(' u ')
	let members = [lowerFlangeData,webData,upperFlangeData].map((e)=>e.name).join(' u ')
	//let handels = [cenHandleData,tosHandleData].map((e)=>e.name+'.s').map((e)=>e= e+' - '+ e).join(' u ')
	let handels = [cenHandleData,tosHandleData].map((e)=>e.name).map((e)=>e= e+' - '+ e).join(' u ')
	let regionName = data.name+'Beam.c'
	let handle = ''
	switch (data.handle) {
		case 'cen':
		handle = cenHandleData.name
		break
		case 'tos':
		handle = tosHandleData.name
		break
	}

	console.log(`comb ${regionName} u ${members} u ${handels}`)
	console.log(`mater ${regionName} ${data.mater}`)
	console.log(`B ${regionName}`)
	console.log(`oed / ${regionName}/${handle}`)
	console.log(`rot ${data.rot.join(' ')}`)
	console.log(`translate ${data.vertex.join(' ')}`)
	console.log(`accept`)
//echo "translate $vx $vy $vz"
//echo "orot $ax $ay $az"
	
	
	//mkComb()
	//mkReg()


}

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

	get icolls() {return interpolate(this.colls)},
	get irows() {return interpolate(this.rows)},
	get iplans() {return interpolate(this.plans)},
	get iall() { return [this.icolls, this.irows, this.iplans] },

	walk(callback) { 
		let [colls, rows, plans] = this.iall
		for(let ci=0; ci < colls.length; ci++){
			for(let ri=0; ri < rows.length; ri++){
				for(let pi=0; pi < plans.length; pi++){
					callback(ci, ri, pi, colls, rows, plans)		
				}
			}

		}
	
	},	




	inFloorSlab(){
	let iall = this.iall
	let colls = iall[0]
	let rows = iall[1]
	let data = {
		name: 'floorSlab.s',
		xmin: -this.margin,
		xmax: colls.at(-1) + this.margin,
		ymin: -this.margin,
		ymax: rows.at(-1) + this.margin,
		zmin: -this.floorDepth,
		zmax: 0,
	}
	inRPP(data)
	},
	drawRules() { 
		let all = []
		let res = 1000
		//TODO: utilize iall()
		let [xmax, ymax, zmax] = [this.icolls.at(-1), this.irows.at(-1), this.iplans.at(-1)]
		for(let i=0; i<= xmax; i+=res){
			let  name = `x${i}.s`
			inSph({name:name ,vertex: [i,-res,0] , radius:100})
			all.push(name)
		}
		for(let i=0; i<= ymax; i+=res){
			let  name = `y${i}.s`
			inSph({name: name,vertex: [-res,i,0] , radius:100})
			all.push(name)
		}
		for(let i=0; i<= zmax; i+=res){
			let  name = `z${i}.s`
			inSph({name: name,vertex: [-res,-res,i] , radius:100})
			all.push(name)
		}

		console.log(`g rule.g ${all.join(' ')}`)
	}
}
/////////////////////////////////////////
function callback (ci,ri,pi,colls,rows,plans){
	debug && console.log('#',ci,colls[ci],ri,rows[ri],pi,plans[pi])
	//console.log(`in node${[ci,ri,pi].join('-')}.s sph ${colls[ci]} ${rows[ri]} ${plans[pi]} 500`)

	let nameString = 'node_' + [ci,ri,pi].join('_') 
	let radiusIn = 200
	let vertexIn = [colls[ci], rows[ri], plans[pi]]
	let vertexIn2y = [colls[ci], rows[ri+1], plans[pi]]
	let vertexIn2x = [colls[ci+1], rows[ri], plans[pi]]
	let vertexIn2z = [colls[ci], rows[ri], plans[pi+1]]
	///---
	inSph({name: nameString+'.s', vertex: vertexIn , radius: radiusIn }) 
	///---
	if (ci+1 < colls.length){
		inRCC({name: nameString+'CenX.s', vertex: vertexIn , vertex2 :vertexIn2x,radius: 50 }) 
		///---
		let span = colls[ci+1] - colls[ci]
		let vertex = [colls[ci], rows[ri], plans[pi]]
		let beamSpec = this.longBeam
		beamSpec.name = nameString+'Long'
		beamSpec.length = span
		beamSpec.vertex = vertex
		beamSpec.mater = longBeamColor
		inBeam(beamSpec)
	}
	if (ri+1 < rows.length){
		inRCC({name: nameString+'CenY.s', vertex: vertexIn , vertex2 :vertexIn2y,radius: 50 }) 
		///---
		let span = rows[ri+1] - rows[ri]
		let vertex = [colls[ci], rows[ri], plans[pi]]
		let beamSpec = this.crossBeam
		beamSpec.name = nameString+'Cross'
		beamSpec.length = span
		beamSpec.vertex = vertex
		beamSpec.mater = crossBeamColor
		inBeam(beamSpec)
	}
	if (pi+1 < plans.length){
		inRCC({name: nameString+'CenZ.s', vertex: vertexIn , vertex2 :vertexIn2z,radius: 50 }) 
		///---
		let span = plans[pi+1] - plans[pi]
		let vertex = [colls[ci], eows[ri], plans[pi]]
		let beamSpec = this.vertColl
		beamSpec.name = nameString+'VertColl'
		beamSpec.length = span
		beamSpec.vertex = vertex
		beamSpec.mater = longBeamColor
		inBeam(beamSpec)
	}
}
//elegant code
//resist continue
//arrow function destroy readability

let boundCallback = callback.bind(data_sample)
data_sample.walk(boundCallback)
data_sample.inFloorSlab()
data_sample.drawRules()


//////trash
//getColls() {return interpolate(this.colls)},
//console.log(data_sample.getColls())
//:w|!node % > site.tcl;rm site.g ;cat site.tcl| mged -c site.g
//console.log('#', interpolate(data_sample.colls))
//console.log('#', data_sample.icolls)
//console.log('#', data_sample.irows)
//console.log('#', data_sample.iplans)
//console.log('#_________')
//beamSample= data_sample.longBeam
//beamSample.name= 'ssss'
//beamSample.length = 5000
//inBeam(beamSample)
	//////eq
	//pressiure vessle designer
	//expoprt datafile
	//skirt|leg|C/L|lug|saddle

let eq1 = {
	shellDiameter: 2000,
	shellLength: 2000,
	shellThick:10,
	ShellDiameterType: 'outer',
	firstEndType: 'ts',
	secondEndType: 'same',
	firstEndThick: 12,
	secondEndThick: 'same',
	orientation: 'vertical',
	supports: {
		type: 'leg',
		legShape: 'pipe',
		legsNumber: 5,
	},
	nozzles: {
		fluidSuction:{
			size:100,
			overLenth: 200,
		},
		fluidEntreance:{},
		vent:{},
		manHole:{}
	}
}
