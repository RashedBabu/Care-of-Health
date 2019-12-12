document.getElementById('bmr-form').addEventListener('submit', calculateResults)

function calculateResults(e){
	var age = document.getElementById('age').value
	var weight = document.getElementById('weight').value
	var h_in_ft  = document.getElementById('ft').value
	var h_in_inch  = document.getElementById('inch').value
	var height = parseFloat(h_in_ft*30.48) + parseFloat(h_in_inch*2.54)

	var calculated_bmr = document.getElementById('res')
	var gender = document.getElementById('gender').value

	var bmrOfMen =parseFloat((10*weight) + (6.25*height)-(5*age)+5)
	var bmrOfWomen = parseFloat((10*weight) + (6.25*height)-(5*age)+161)

	if (gender=='male') {
		calculated_bmr.value = parseInt(bmrOfMen)
	}else {
		calculated_bmr.value = parseInt(bmrOfWomen)
	}

	e.preventDefault()
}