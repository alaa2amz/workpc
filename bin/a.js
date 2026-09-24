function a(vn,fn){
	s=await JSON.stringify(vn)
	b=new Blob([s])
	a=document.createElement('a')
	a.href = URL.createObjectURL(b) 
	a.download = true
	a.click()
}


function sv(vn,fn){
	let s=JSON.stringify(vn)
	let b=new Blob([s])
	let a=document.createElement('a')
	a.href = URL.createObjectURL(b)
	a.download = fn
	a.click()
}
