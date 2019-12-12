document.getElementById('tdee-form').addEventListener('submit', calculateResults)

function calculateResults(e){

	var bmr = document.getElementById('bmr').value
	var activity = document.getElementById('activity').value
	var tdee = document.getElementById('res')

	if (activity == 'one') {
		tdee.value = parseFloat(bmr)*1.2
	}else if (activity=='two') {
		tdee.value = parseFloat(bmr)*1.375
	}else if (activity=='three') {
		tdee.value = parseFloat(bmr)*1.55
	}else if (activity=='four') {
		tdee.value = parseFloat(bmr)*1.725
	}else{
		tdee.value = parseFloat(bmr)*1.9
	}

	e.preventDefault()
}